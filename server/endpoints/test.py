from flask import Flask, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView

import config
import os

test = Blueprint('test', __name__)


class UseExpert(MethodView):

    def get(self):
        return 'test endpoint'


    def post(self):
        from services.interpreter import expertai_full_analyze

        test_string = 'hello, this is nick, and Im going to talk about my interests. My interests include music and languages'
        output_ = expertai_full_analyze(test_string)

        return {'return': output_}


test.add_url_rule('/test', view_func=UseExpert.as_view('test'))

