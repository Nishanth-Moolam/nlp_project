from models.note import Note, db
from datetime import datetime


def CreateNote(notes_filename, section_id):

    date_added = datetime.now()

    new_note = Note(
        notes_filename=notes_filename, section_id=section_id, date_added=date_added)
    db.session.add(new_note)
    db.session.commit()

def DeleteNote():
    pass

def UpdateNote():
    pass

def ReadNote(picture_url):
    from interpreter import ms_ocr

    words_string = ms_ocr(picture_url)
    return words_string

def InterpretNote(text):
    from interpreter import expertai_full

    output_dict = expertai_full(text)
    return output_dict

def ReadAndinterpretNote(picture_url):
    '''
    returns a dictionary with entities, lemmas, phrases, topics
    ''' 
    return InterpretNote(ReadNote(picture_url))