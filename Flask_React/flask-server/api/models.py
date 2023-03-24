from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


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
