from flask import Flask, render_template, url_for, redirect , request, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, login_user, LoginManager, login_required,logout_user,current_user
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from models import db
from models import Patient,Doctor

# To create the db:
# python
# from models import db, Doctor, Patient 
# from app import app
# db.create_all()
# quit()/exit()

# To get PATH of sqlite3:
# $env:PATH += ';C:\SQLite3'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/GitHub/EmoCare/Flask_React/flask-server/api/emocare.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)
bcrypt = Bcrypt(app)
app.app_context().push()
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "patientLogIn"
# login_manager.login_view = "doctorLogIn"

@login_manager.user_loader
def load_user(user_id):
    return Patient.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')
 

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/patient/signup')
def patientSignIn():
   return render_template('patientSignup.html')

@app.route('/patient/login')
def patientLogIn():
   return render_template('patientLogin.html')

@app.route('/patient/signup', methods=['POST'])
def patientSignUp():
   
    name = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password' , 'none')

    # check for exiting username and email !!
    patient = Patient.query.filter_by(username=username).first()
    if patient:
        flash('Username already exists')
        return redirect(url_for('patientSignIn'))

    # encrypting and creating a hash password
    hashed_password = bcrypt.generate_password_hash(password)
    new_patient = Patient(name=name,email=email, username=username, password=hashed_password)
    db.session.add(new_patient)
    db.session.commit()
    return redirect(url_for('patientLogIn')) 


@app.route('/patient/login', methods=['POST'])
def patientLogin():
    username = request.form.get('username')
    password = request.form.get('password')

    patient = Patient.query.filter_by(username=username).first()
    if patient:
        if bcrypt.check_password_hash(patient.password,password):
            login_user(patient)
            return redirect(url_for('dashboard'))
        else:
            flash('Please check your login details and try again')
            return redirect(url_for('patientLogIn'))
    else:
        flash('User does not exist')
        return redirect(url_for('patientSignIn'))        

@app.route('/doctor/signup')
def doctorSignIn():
   return render_template('doctorSignup.html')

@app.route('/doctor/login')
def doctorLogIn():
   return render_template('doctorLogin.html')

@app.route('/doctor/signup', methods=['POST'])
def doctorSignUp():
   
    doctorName = request.form.get('doctorName')
    doctorEmail = request.form.get('doctorEmail')
    doctorUsername = request.form.get('doctorUsername')
    doctorPassword = request.form.get('doctorPassword' , 'none')

    # check for exiting username and email !!
    doctor = Doctor.query.filter_by(doctorUsername=doctorUsername).first()
    if doctor:
        flash('Username already exists in the doctor database')
        return redirect(url_for('doctorSignIn'))

    # encrypting and creating a hash password
    hashed_password = bcrypt.generate_password_hash(doctorPassword)
    new_doctor = Doctor(doctorName=doctorName,doctorEmail=doctorEmail, doctorUsername=doctorUsername, doctorPassword=hashed_password)
    db.session.add(new_doctor)
    db.session.commit()
    return redirect(url_for('doctorLogIn')) 


@app.route('/doctor/login', methods=['POST'])
def doctorLogin():
    doctorUsername = request.form.get('doctorUsername')
    doctorPassword = request.form.get('doctorPassword')

    doctor = Doctor.query.filter_by(doctorUsername=doctorUsername).first()
    if doctor:
        if bcrypt.check_password_hash(doctor.doctorPassword,doctorPassword):
            # login_user(doctor)
            return redirect(url_for('dashboard'))
        else:
            flash('Please check your login details and try again')
            return redirect(url_for('doctorLogIn'))
    else:
        flash('User does not exist')
        return redirect(url_for('doctorSignIn'))      

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))

if __name__=="__main__":
    app.run (debug = True)
