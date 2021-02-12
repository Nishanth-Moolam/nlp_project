from app import db

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
