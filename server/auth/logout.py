from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from flask_login import login_user

from werkzeug.security import generate_password_hash, check_password_hash

logout = Blueprint('logout', __name__)


class Logout(MethodView):

    def get(self):
        return 'this works'


logout.add_url_rule('/logout', view_func=Logout.as_view('logout'))
