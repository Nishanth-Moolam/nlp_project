from app import db
from models.note import Note


class Section(db.Model):
    __tablename__ = 'section'
    __searchable__ = ['section_name']
    
    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    notes = db.relationship('Note', backref='section')
