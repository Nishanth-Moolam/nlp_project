from app import db

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
