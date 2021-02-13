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
        from services.note import CreateNote
        from services.insights import process_insights

        from services.reader import ms_ocr_read

        if request.files:

            notes_file = request.files['notes_file']
            notes_section = request.form['notes_section']
            notes_filename = secure_filename(notes_file.filename)

            # add notes info into notes db model
            section_id = find_section(notes_section)
            CreateNote(notes_filename=notes_filename, section_id=section_id)

            # uses upload service to upload notes file
            try:
                # saves note to local
                save_file(notes_file, notes_section, notes_filename)
            except:
                return 'error occured while uploading'

            try:
                # processes insights
                # ms_ocr_read does not work since files are not hosted online. Must investigate how to host images and files online
                process_insights(notes_filename)
            except:
                return 'error occured while processing insights'
            return 'file worked with notes folder: '+notes_section
        return 'file not present'


upload.add_url_rule('/upload', view_func=UploadNotesFile.as_view('upload'))


class CreateSectionFolder(MethodView):

    def get(self):

        return 'this is the create section folder page'

    def post(self):
        from services.utils import make_folder
        from services.section import CreateSection

        section_name = request.form['section_name']

        # add into db model
        CreateSection(section_name=section_name)

        # creates the folder
        make_folder(section_name)

        return 'section created!'


upload.add_url_rule(
    '/newsection', view_func=CreateSectionFolder.as_view('newsection'))
