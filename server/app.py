from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

import config

from endpoints.upload import upload
from endpoints.test import test
from endpoints.notes import notes

# folder where file uploads exist
UPLOAD_FOLDER = config.server_path+'/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.register_blueprint(upload, url_prefix='')
app.register_blueprint(notes, url_prefix = '')
app.register_blueprint(test, url_prefix='')

# enables cors
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = config.sql_alchemy_database_uri
app.config['SECRET_KEY'] = config.secret_key
db = SQLAlchemy(app)

# When deleting and reinitializing db, I need this for the tables to instantiate
'''
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes_filename = db.Column(db.String(100), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    date_added = db.Column(db.DateTime, nullable=False)


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    notes = db.relationship('Note', backref='section')
'''


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
