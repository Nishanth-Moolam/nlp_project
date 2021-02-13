from app import db

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
