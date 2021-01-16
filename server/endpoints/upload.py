from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

import services.utils
import config

upload = Blueprint('upload', __name__)


class UploadNotesFile(MethodView):

    def get(self):

        return 'this is the upload notes file page'

    def post(self):

        if request.files:
            try:
                notes_file = request.files['notes_file']
                notes_folder = request.form['notes_folder']
                notes_filename = request.form['notes_filename']

                # add notes info into notes db model
                # checks if notes folder exists
                # uses upload service to upload notes file

                '''
                notes_file.save(os.path.join(
                    config.server_path + 'static/uploads/', notes_filename))
                '''

                return 'file worked with notes folder: '+notes_folder
            except:
                return 'error while uploading'
        return 'file not present'

        '''
        # import from app to use db model
        from models import Blog, db

        # detects form data!
        blog = dict(request.form)
        title = blog['title'][0]
        content = blog['content'][0]
        author_id = blog['author_id'][0]
        date_added = datetime.now()
        try:
            new_blog = Blog(title=title, content=content,
                            author_id=author_id, date_added=date_added)
            db.session.add(new_blog)
            db.session.commit()
            return jsonify({'content': 'blog added!'})
        except:
            db.session.rollback()
            return jsonify({'content': 'there was a problem adding blog'})
        '''


upload.add_url_rule('/upload', view_func=UploadNotesFile.as_view('upload'))
