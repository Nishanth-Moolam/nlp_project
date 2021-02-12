from app import db

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
