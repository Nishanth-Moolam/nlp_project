from app import db

class Lemma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
