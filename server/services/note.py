from models.note import Note, db
from datetime import datetime


def CreateNote(notes_filename, section_id):

    date_added = datetime.now()

    new_note = Note(
        notes_filename=notes_filename, section_id=section_id, date_added=date_added)
    db.session.add(new_note)
    db.session.commit()
