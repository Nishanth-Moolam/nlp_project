import os
import config
from app import db
from models.section import Section
from models.note import Note


def make_folder(folder_name):
    os.mkdir(config.server_path+'/static/uploads/'+folder_name)


def save_file(file, folder_name, file_name):
    file.save(os.path.join(
        config.server_path + '/static/uploads/'+folder_name, file_name))


def find_section(section_name):
    section = Section.query.filter_by(section_name=section_name).first()
    return section.id 


def find_section_name(section_id):
    section = Section.query.filter_by(id = section_id).first()
    return str(section_id)+'-'+section.section_name


def find_note_name(note_id):
    note = Note.query.filter_by(id = note_id).first()
    return note.notes_filename

def find_picture_url(note_id):
    note = Note.query.filter_by(id = note_id).first()
    section = Section.query.filter_by(id = note.section_id).first()

    url = config.server_path + '/static/uploads/'+str(section.id)+'-'+section.section_name+'/'+str(note_id)+'-'+note.notes_filename

    return url

def does_section_exist(section_id):
    sections = Section.query.filter_by(id = section_id).all()
    if len(sections) > 0:
        return True
    return False