from app import db

class Lemma(db.Model):
    __tablename__ = 'lemma'
    __searchable__ = ['value']
    
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
