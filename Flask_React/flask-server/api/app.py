from flask import Flask, render_template, url_for, redirect , request, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import login_manager, UserMixin, login_user, LoginManager, login_required,logout_user,current_user
from flask_security import Security, SQLAlchemySessionUserDatastore
  
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from models import db
from models import Patient,Doctor,User,Role,user_roles

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
def patientDashboard():
    return "Welcome to patient dashboard"

@app.route('/doctor/dashboard')
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
