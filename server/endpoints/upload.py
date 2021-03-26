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
        from services.utils import find_section_name, save_file, does_section_exist
        from services.note import CreateNote
        from services.insights import process_insights

        if request.files:

            # initializes values
            notes_file = request.files['notes_file']
            notes_section_id = request.form['section_id']
            
            # uploads note to db is section exists
            if does_section_exist(notes_section_id):
                # this is the version saved in db
                notes_filename = secure_filename(notes_file.filename)
                # add notes info into notes db model
                note_id = CreateNote(notes_filename=notes_filename, section_id=notes_section_id)
                # finds section name
                notes_section = find_section_name(notes_section_id)
            else:
                return 'section does not exist'

            # uses upload service to upload notes file
            try:
                # saves note to local
                save_file(notes_file, notes_section, notes_filename, note_id)
            except:
                return 'error occured while uploading'

            try:
                # reads note, extracts insights from note, and saves insights in db
                process_insights(notes_filename, note_id)
            except:
                return 'error occured while reading and processing insights'

            return 'file uploaded to section: '+notes_section

        return 'file not present'

upload.add_url_rule('/upload', view_func=UploadNotesFile.as_view('upload'))

class DeleteNotesFile(MethodView):

    def post(self):
        from services.note import DeleteNote

        note_id = request.form['note_id']

upload.add_url_rule('/delete', view_func=DeleteNotesFile.as_view('delete'))  

class CreateSectionFolder(MethodView):

    def post(self):
        from services.utils import make_folder
        from services.section import CreateSection

        section_name = request.form['section_name']

        # add into db model
        section_id = CreateSection(section_name=section_name)

        # creates the folder
        make_folder(str(section_id)+'-'+section_name)

        return 'section created!'


upload.add_url_rule(
    '/newsection', view_func=CreateSectionFolder.as_view('newsection'))
