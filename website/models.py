from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    gender = db.Column(db.String(25))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregnancies = db.Column(db.Integer)
    glucose = db.Column(db.Integer)
    blood_pressure = db.Column(db.Integer)
    skin_thickness = db.Column(db.Float)
    insulin = db.Column(db.Integer)
    BMI = db.Column(db.Float)
    diabetes_pedigree_function = db.Column(db.Float)
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    diabetes_app = db.relationship('User')


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    rate = db.Column(db.Float)
    address = db.Column(db.String(2083))
    phoneNumber=db.Column(db.String(100))
    
    
