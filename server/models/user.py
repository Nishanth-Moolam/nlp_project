from flask_login import UserMixin

from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    about = db.Column(db.String(200), nullable=True)
