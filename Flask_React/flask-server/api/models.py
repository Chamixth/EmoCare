from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Patient(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20), unique=True , nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Doctor(db.Model, UserMixin)
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20), unique=True , nullable=False)
    password = db.Column(db.String(80), nullable=False)
