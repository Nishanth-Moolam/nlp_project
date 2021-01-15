from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from flask_login import login_user

from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


class Login(MethodView):

    def get(self):
        return jsonify({'content': 'this is the login page'})

    def post(self):
        from models import User, db

        login_form = dict(request.form)
        email = login_form['email'][0]
        password = login_form['password'][0]

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'content': 'credentials invalid'})

        elif user and check_password_hash(user.password, password):
            return jsonify({'content': 'credentials valid'})

        else:
            return jsonify({'content': 'error occurred'})


auth.add_url_rule('/login', view_func=Login.as_view('login'))


class Signup(MethodView):

    def get(self):
        return jsonify({'content': 'this is the signup page'})

    def post(self):
        # import from app to use db model
        from models import User, db

        # detects form data!
        user = dict(request.form)
        username = user['username'][0]
        about = user['about'][0]
        email = user['email'][0]
        password = user['password'][0]

        user_exists = User.query.filter_by(email=email).first()

        if user_exists:
            try:
                return jsonify({'content': 'user with email already exists'})
            except:
                return 'error'

        else:
            try:
                new_user = User(username=username, about=about,
                                email=email, password=generate_password_hash(password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                return jsonify({'content': 'user added!'})
            except:
                db.session.rollback()
                return jsonify({'content': 'there was a problem adding user'})


auth.add_url_rule('/signup', view_func=Signup.as_view('signup'))


class Logout(MethodView):

    def get(self):
        pass


auth.add_url_rule('/logout', view_func=Logout.as_view('logout'))