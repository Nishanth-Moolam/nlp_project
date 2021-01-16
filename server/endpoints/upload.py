from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from werkzeug.utils import secure_filename

import config
import os

upload = Blueprint('upload', __name__)


class UploadNotesFile(MethodView):

    def get(self):

        return 'this is the upload notes file page'

    def post(self):
        from services.utils import find_section, save_file
        from services.create_note import CreateNote

        if request.files:

            notes_file = request.files['notes_file']
            notes_section = request.form['notes_section']
            notes_filename = secure_filename(notes_file.filename)

            # add notes info into notes db model
            section_id = find_section(notes_section)
            CreateNote(
                notes_filename=notes_filename, section_id=section_id)

            # uses upload service to upload notes file
            try:
                save_file(
                    notes_file, notes_section, notes_filename)
            except:
                return 'file-path does not exist'

            return 'file worked with notes folder: '+notes_section

        return 'file not present'


upload.add_url_rule('/upload', view_func=UploadNotesFile.as_view('upload'))


class CreateSectionFolder(MethodView):

    def get(self):

        return 'this is the create section folder page'

    def post(self):
        from services.utils import make_folder
        from services.create_section import CreateSection

        section_name = request.form['section_name']

        # add into db model
        CreateSection(section_name=section_name)

        # creates the folder
        make_folder(section_name)

        return 'section created!'


upload.add_url_rule(
    '/newsection', view_func=CreateSectionFolder.as_view('newsection'))
