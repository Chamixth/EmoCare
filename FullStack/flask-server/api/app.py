from flask import Flask, render_template, url_for, redirect , request , flash, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_manager, UserMixin, login_user, LoginManager, login_required,logout_user,current_user
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemySessionUserDatastore, roles_accepted, login_required
from datetime import datetime
  
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from models import db
from models import User,Role,user_roles, Request, Consultation

# To create the db:
# python
# from models import db
# from app import app
# db.create_all()
# exit()

# To get PATH of sqlite3:
# $env:PATH += ';C:\SQLite3'
# & sqlite3.exe

app = Flask(__name__)
# path to sqlite3 database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/GitHub/EmoCare/Flask_React/flask-server/api/emocare.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password123@localhost/emocaredb'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_PASSWORD_SALT']='thisisasecretsalt'
app.config['SECURITY_REGISTERABLE']= True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['UPLOAD_FOLDER'] = 'path/to/save/videos'

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
 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/patient/dashboard')
@roles_accepted('Patient')
def patientDashboard():
    return render_template('patientDashboard.html')

def insert_role(role_id, role_name):
    role = Role.query.filter_by(id=1).first()
    if not role:
        doctor_role = Role(id=1,name='Doctor')
        db.session.add(doctor_role)
        db.session.commit()
    else:
        doctor_role = role
    role = Role.query.filter_by(id=2).first()
    if not role:
        patient_role = Role(id=2,name='Patient')
        db.session.add(patient_role)
        db.session.commit()
    else:
        patient_role = role

@app.route('/all/doctors', methods=['GET','POST'])
@roles_accepted('Patient')
def all_doctors():
    doctors = []
    role_doctors = db.session.query(user_roles).filter_by(role_id =1)
    for doctor in role_doctors:
        user = User.query.filter_by(id=doctor.user_id).first()
        doctors.append({'Doctor_id' : user.id, 'Doctor name' : user.name , 'Doctor email': user.email})
    # return jsonify ({'doctors': doctors})
    return render_template('allDoctors.html', doctors = doctors)

# for patients to send requests to doctors
@app.route('/request/<selected_doctor_id>', methods =['GET','POST'])
@roles_accepted('Patient')
def createRequest(selected_doctor_id):
    user = User.query.filter_by(id=selected_doctor_id).first()
    if user is None or user.role_id !=1:
        flash('Doctor not found.', 'error')
        return redirect(url_for('all_doctors'))
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
@roles_accepted('Patient')
def myRequests():
    # requests = []
    # if current_user.is_authenticated:
    my_requests = Request.query.filter_by(patient_id=current_user.id).all()
        # for request in my_requests:
            # requests.append({'Request ID ': request.id , 'Patient ID ': request.patient_id, 'Doctor ID ' : request.doctor_id,'Meeting date': request.meeting_date, 'Meeting time': request.meeting_time , 'Status' : request.status})
        # return jsonify({'My Requests': requests})
    return render_template('myRequests.html', requests = my_requests)
    # else:
    #     return redirect(url_for('UserLogIn'))


# A logged in doctor to see the requests recieved
@app.route('/view/requests')
@roles_accepted('Doctor')
def viewRequest():
    # requests = []
    # if current_user.is_authenticated:
    requests = Request.query.filter_by(doctor_id=current_user.id, status="Pending").all()
        # for request in new_request:
        #    requests.append({'Request ID ': request.id , 'Patient ID': request.patient_id, 'Meeting date': request.meeting_date, 'Meeting time': request.meeting_time, 'Status': request.status})
        # # return jsonify({'Requests':requests})
    return render_template('viewRequest.html', requests = requests)
    # else:
    #     return redirect(url_for('UserLogIn'))
  

# Accept a request - add to consultation - decline a request DELETE - inform the patient 
@app.route('/view/requests/<selected_request_id>' , methods = ['GET','POST'])
@roles_accepted('Doctor')
def acceptRequest(selected_request_id):
    if request.method =='POST':
        if request.form['action'] == "Accept":
            selected_request = Request.query.filter_by(id=selected_request_id).first()
            selected_request.status = "Accepted"
            new_consult = Consultation(request_id = selected_request_id,doctor_id=selected_request.doctor_id,patient_id=selected_request.patient_id, meeting_date=selected_request.meeting_date, meeting_time=selected_request.meeting_time)
            db.session.add(new_consult)
            db.session.commit()
            return redirect(url_for('myConsultation'))
        elif request.form['action'] == 'Delete':
            selected_request = Request.query.get_or_404(selected_request_id)
            selected_request.status= "Declined"
            db.session.commit()
            # flash('Request declined.')
            return redirect(url_for('viewRequest'))
    elif request.method == 'GET':
        selected_request = Request.query.filter_by(id=selected_request_id).first()
    return render_template('acdelreq.html', request_id=selected_request_id)
   
# view all accepted consultation details 
@app.route('/my/consultations')
@roles_accepted('Doctor')
def myConsultation():
    # consults = []
    # if current_user.is_authenticated:
    new_consult = Consultation.query.filter_by(doctor_id=current_user.id)
        # for consult in new_consult:
        #     consults.append({'Consultation ID': consult.id, 'Request ID ': consult.request_id ,'Doctor ID':consult.doctor_id, 'Patient ID': consult.patient_id, 'Meeting date': consult.meeting_date, 'Meeting time': consult.meeting_time})
        # return jsonify({'Consultations':consults})
    return render_template('consultations.html',consultations=new_consult)
    # else:
    #     return redirect(url_for('UserLogIn'))

# upload video
@app.route('/upload/video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        video_file = request.files['video_file']
        filename = request.form['filename']
        patient_id = request.form['patient_id']
        if video_file and filename:
           #Set the UPLOAD_FOLDER configuration variable to the path where you want to save the videos on the local machine.
            video_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            video_file.save(video_path)
            new_video = Video(name=filename,path=video_path,doctor_id=current_user.id,patient_id=patient_id)
            db.session.add(new_video)
            db.session.commit()
            flash("Video Saved!")
            return 'Video uploaded successfully.', 200
        else:
            return 'No video uploaded', 400
    return render_template('video.html')
    
@app.route('/doctor/dashboard')
@roles_accepted('Doctor')
def doctorDashboard():
    return render_template('doctorDashboard.html')


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

    insert_role(1, 'Doctor')
    insert_role(2, 'Patient')

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
