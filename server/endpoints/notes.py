from flask import Flask, jsonify, request, Blueprint, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

import config
import os

notes = Blueprint('notes', __name__)

'''
add a different endpoint for each section and images
'''


class NotesView(MethodView):

    def get(self, section_id, note_id):
        from services.utils import find_section_name, find_note_name
        section_name = find_section_name(section_id)
        note_name = find_note_name(note_id)

        return send_file(config.server_path+'/static/uploads/'+section_name+'/'+str(note_id)+'-'+note_name)


    def post(self, section_id, note_id):
        return 'post method'


notes.add_url_rule('/section/<int:section_id>/note/<int:note_id>', view_func=NotesView.as_view('note'))


class SectionView(MethodView):
    '''
    this should list out the notes in a section
    '''

    def get(self):
        pass

class FullView(MethodView):
    '''
    this should list out all the sections created
    '''

    def get(self):
        pass