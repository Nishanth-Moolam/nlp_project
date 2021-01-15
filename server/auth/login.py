from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from flask_login import login_user

from werkzeug.security import generate_password_hash, check_password_hash

login = Blueprint('login', __name__)

class Login(MethodView):

    def get(self):
        return jsonify({'content': 'this is the login page'})

    def post(self):
        from models.user import User, db

        return 'this works'

        '''
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
        '''


login.add_url_rule('/login', view_func=Login.as_view('login'))