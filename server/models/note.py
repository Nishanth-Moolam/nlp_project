from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes_filename = db.Column(db.String(100), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    date_added = db.Column(db.DateTime, nullable=False)
