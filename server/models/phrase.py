from app import db

class Phrase(db.Model):
    __tablename__ = 'phrase'
    __searchable__ = ['value']
    
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
