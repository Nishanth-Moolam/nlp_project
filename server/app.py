from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_msearch import Search

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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = config.secret_key

# debug mode set to true
app.config["DEBUG"] = True

db = SQLAlchemy(app)

search = Search()
search.init_app(app)

# When deleting and reinitializing db, I need this for the tables to instantiate
'''
class Note(db.Model):
    __tablename__ = 'note'
    __searchable__ = ['notes_filename']

    id = db.Column(db.Integer, primary_key=True)
    notes_filename = db.Column(db.String(100), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    date_added = db.Column(db.DateTime, nullable=False)
    entities = db.relationship('Entity', backref='note')
    lemmas = db.relationship('Lemma', backref='note')
    phrases = db.relationship('Phrase', backref='note')
    topics = db.relationship('Topic', backref='note')

class Section(db.Model):
    __tablename__ = 'section'
    __searchable__ = ['section_name']

    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    notes = db.relationship('Note', backref='section')

class Entity(db.Model):
    __tablename__ = 'entity'
    __searchable__ = ['value']

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

class Lemma(db.Model):
    __tablename__ = 'lemma'
    __searchable__ = ['value']

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

class Phrase(db.Model):
    __tablename__ = 'phrase'
    __searchable__ = ['value']

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

class Topic(db.Model):
    __tablename__ = 'topic'
    __searchable__ = ['value']

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(50), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

'''

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
