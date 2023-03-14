from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, login_user, LoginManager, login_required,logout_user,current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from models import db
from models import Patient

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
login_manager.login_view = "Patient"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    username = StringField(validators={InputRequired(), Length(min=4, max=20)}, render_kw={"placceholder": "Username"})
    password = PasswordField(validators={InputRequired(), Length(min=4, max=20)}, render_kw={"placceholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = Patient.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "The username already exists. Enter a different one"
            )

class LoginForm(FlaskForm):
    username = StringField(validators={InputRequired(), Length(min=4, max=20)}, render_kw={"placceholder": "Username"})
    password = PasswordField(validators={InputRequired(), Length(min=4, max=20)}, render_kw={"placceholder": "Password"})
    submit = SubmitField("Login")

@app.route('/')
def home():
    return 'Hello from flask'

@app.route('/dashboard')
@login_required
def dashboard():
    return "welcome to dashboard"

@app.route('/patient', methods=['GET','POST'])
def patientLogin():
    form = LoginForm()

    if form.validate_on_submit():
        patient = Patient.query.filter_by(username=form.username.data).first()
        if patient:
            if bcrypt.check_password_hash(patient.password,form.password.data):
               login_user(patient)
               return redirect(url_for('dashboard'))

    return render_template('patient.html', form=form)

def patientSignUp():
    form = RegisterForm()

# encrypting and creating a hash password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_patient = Patient(username=form.username.data,password=hashed_password)
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('patient'))

    return render_template('Patient.html', form = form)

@app.route('/doctor', methods=['GET','POST'])
def doctorLogin():
    form = LoginForm()

    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(username=form.username.data).first()
        if doctor:
            if bcrypt.check_password_hash(doctor.password,form.password.data):
               login_user(doctor)
               return redirect(url_for('dashboard'))

    return render_template('doctor.html', form=form)

def doctorSignUp():
    form = RegisterForm()

# encrypting and creating a hash password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_doctor = Doctor(username=form.username.data,password=hashed_password)
        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for('/'))

    return render_template('doctor.html',form =form)

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))

if __name__=="__main__":
    app.run (debug = True)