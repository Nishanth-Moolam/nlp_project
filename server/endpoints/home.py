from flask import Flask, jsonify, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView


# blueprint to be used in app
home = Blueprint('home', __name__)


class HomePage(MethodView):

    def get(self):

        return 'this works'


home.add_url_rule('/home', view_func=HomePage.as_view('home'))
