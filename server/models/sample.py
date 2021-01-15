from flask_login import UserMixin

from app import db


# db models


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    about = db.Column(db.String(200), nullable=True)
    blogs = db.relationship('Blog', backref='author')
    comments = db.relationship('Comment', backref='author')


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_added = db.Column(db.DateTime, nullable=False)
    comments = db.relationship('Comment', backref='blog')


class Comment(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    date_added = db.Column(db.DateTime, nullable=False)
