from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from flask_login import login_user

from werkzeug.security import generate_password_hash, check_password_hash

signup = Blueprint('signup', __name__)


class Signup(MethodView):

    def get(self):
        return jsonify({'content': 'this is the signup page'})

    def post(self):
        # import from app to use db model
        from models.user import User, db

        return 'this works'

        '''
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
        '''


signup.add_url_rule('/signup', view_func=Signup.as_view('signup'))
