from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

import config
import os

test = Blueprint('test', __name__)


class UseMsOcr(MethodView):

    def get(self):
        return 'test endpoint'


    def post(self):
        return 'test endpoint'


test.add_url_rule('/test', view_func=UseMsOcr.as_view('test'))

