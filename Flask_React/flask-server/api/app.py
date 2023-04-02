from flask import Flask, render_template, url_for, redirect , request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_manager, UserMixin, login_user, LoginManager, login_required,logout_user,current_user
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemySessionUserDatastore, roles_accepted, login_required
from datetime import datetime,date
  
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from models import db
from models import Patient,Doctor,User,Role,user_roles, Request

# To create the db:
# python
# from models import db, Doctor, Patient 
# from app import app
# db.create_all()
# quit()/exit()

# To get PATH of sqlite3:
# $env:PATH += ';C:\SQLite3'
# & sqlite3.exe

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/GitHub/EmoCare/Flask_React/flask-server/api/emocare.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURIT_PASSWORD_SALT']='thisisasecretsalt'
app.config['SECURITY_REGISTERABLE']= True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

# db = SQLAlchemy(app)
db.init_app(app)
bcrypt = Bcrypt(app)
app.app_context().push()
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "UserLogIn"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# load users, roles for a session
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def home():
    return render_template('home.html')
 

@app.route('/patient/dashboard')
@roles_accepted('Patient')
def patientDashboard():
    return "Welcome to patient dashboard"

@app.route('/all/doctors', methods=['GET','POST'])
def all_doctors():
    doctors = []
    role_doctors = db.session.query(user_roles).filter_by(role_id =1)
    for doctor in role_doctors:
        user = User.query.filter_by(id=doctor.user_id).first()
        doctors.append({'Doctor_id' : user.id, 'Doctor name' : user.name , 'Doctor email': user.email})
    return jsonify ({'doctors': doctors})

# for patients to send requests to doctors
@app.route('/request/<selected_doctor_id>', methods =['GET','POST'])
def createRequest(selected_doctor_id):
    if request.method == 'POST':    
        if current_user.is_authenticated:
            patient_id = request.form.get('patient_id')
            date = request.form.get('meeting_date')
            time = request.form.get('meeting_time')
            new_request = Request(doctor_id=selected_doctor_id,patient_id=patient_id, meeting_date=date, meeting_time=time)
            db.session.add(new_request)
            db.session.commit()
            return redirect(url_for('patientDashboard'))
        else:
            return redirect(url_for('UserLogIn'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            patient_id = current_user.id
        else:
            return redirect(url_for('UserLogIn'))
    return render_template('request.html', doctor_id=selected_doctor_id, patient_id=patient_id)

# To view requests made by a patient
@app.route('/my/requests')
def myRequests():
    requests = []
    if current_user.is_authenticated:
        my_requests = Request.query.filter_by(patient_id=current_user.id)
        for request in my_requests:
            requests.append({'Request ID ': request.id , 'Patient ID ': request.patient_id, 'Doctor ID ' : request.doctor_id})
        return jsonify({'My Requests ': requests})
    else:
        return redirect(url_for('UserLogIn'))


# A logged in doctor to see the requests recieved
@app.route('/view/requests')
def viewRequest():
    requests = []
    if current_user.is_authenticated:
        new_request = Request.query.filter_by(doctor_id=current_user.id)
        for request in new_request:
            requests.append({'Request ID ': request.id , 'Patient ID': request.patient_id, 'Meeting date': request.meeting_date, 'Meeting time': request.meeting_time})
        return jsonify({'Requests':requests})
    else:
        return redirect(url_for('UserLogIn'))


# Accept a request - add to consultation 

# decline a request DELETE - inform the patient 

# view all accepted consultation details 
    
@app.route('/doctor/dashboard')
@roles_accepted('Doctor')
def doctorDashboard():
    return "Welcome to doctor dashboard"


@app.route('/signup')
def UserSignIn():
   return render_template('signup.html')

@app.route('/signin')
def UserLogIn():
   return render_template('signin.html')

@app.route('/signup', methods=['POST'])
def SignUp():
   
    name = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # check for exiting username and email !!
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists')
        return redirect(url_for('UserSignIn'))

    # encrypting and creating a hash password
    hashed_password = bcrypt.generate_password_hash(password)
    role = Role.query.filter_by(id=request.form['options']).first()
    role_type = request.form['options']
    new_user = User(name=name,email=email, username=username, password=hashed_password, active=1 ,roles=[role], role_id= role_type)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('UserLogIn')) 


@app.route('/signin', methods=['POST'])
def SignIn():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        if bcrypt.check_password_hash(user.password,password):
            role_type = user.role_id
            if (role_type == 1):
                login_user(user)
                return redirect(url_for('doctorDashboard'))
            if (role_type == 2):
                login_user(user)
                return redirect(url_for('patientDashboard'))
        else:
            flash('Please check your login details and try again')
            return redirect(url_for('UserLogIn'))
    else:
        flash('User does not exist')
        return redirect(url_for('UserSignIn'))        


@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))

if __name__=="__main__":
    app.run (debug = True)
