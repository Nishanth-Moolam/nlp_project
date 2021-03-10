from models.note import Note, db
from datetime import datetime


def CreateNote(notes_filename, section_id):

    date_added = datetime.now()

    new_note = Note(
            notes_filename=notes_filename, 
            section_id=section_id, 
            date_added=date_added
        )
    db.session.add(new_note)
    db.session.commit()

    return new_note.id

def DeleteNote():
    pass

def UpdateNote():
    pass

def read_note(picture_url):
    from services.reader import read

    words_string = read(picture_url)
    return words_string

def interpret_note(text):
    from services.interpreter import expertai_full

    output_dict = expertai_full(text)
    return output_dict

def read_and_interpret_note(picture_url):
    '''
    returns a dictionary with entities, lemmas, phrases, topics
    ''' 
    return interpret_note(read_note(picture_url))