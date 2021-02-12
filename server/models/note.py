from app import db

'''
Note:

when querying, remember that there could be multiple entries of the same value for entity etc. you must query for all of them, to find all associated notes.
'''


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes_filename = db.Column(db.String(100), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    date_added = db.Column(db.DateTime, nullable=False)
