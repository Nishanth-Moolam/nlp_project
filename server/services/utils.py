import os
import config
from app import db
from models.section import Section


def make_folder(folder_name):
    os.mkdir(config.server_path+'/static/uploads/'+folder_name)


def save_file(file, folder_name, file_name):
    file.save(os.path.join(
        config.server_path + '/static/uploads/'+folder_name, file_name))


def find_section(section_name):
    section = Section.query.filter_by(section_name=section_name).first()
    return section.id
