from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin 
from flask_security import UserMixin,RoleMixin
from datetime import datetime,date


db = SQLAlchemy()
#user data model 
#Role data model 


class Role(db.Model,RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default = '')
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='user_roles' , backref='user')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

# Define the user_roles association table
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')),
)
    
class Patient(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100))
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(100))
   

class Doctor(db.Model, UserMixin):
    doctorId = db.Column(db.Integer , primary_key=True)
    doctorUsername = db.Column(db.String(20), unique=True)
    doctorName =  db.Column(db.String(1000))
    doctorEmail = db.Column(db.String(100))
    doctorPassword = db.Column(db.String(80))

class Request(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    meeting_date = db.Column(db.String,nullable=False)
    meeting_time = db.Column(db.String,nullable=False)

    doctor_ref = db.relationship("User", uselist=False, foreign_keys=[doctor_id])
    patient_ref = db.relationship("User", uselist=False, foreign_keys=[patient_id])
    