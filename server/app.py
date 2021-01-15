from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

from views.home import home

from auth.login import login
from auth.logout import logout
from auth.signup import signup


app = Flask(__name__)

app.register_blueprint(home, url_prefix='')

app.register_blueprint(login, url_prefix='')
app.register_blueprint(logout, url_prefix='')
app.register_blueprint(signup, url_prefix='')

CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nlpproject.db"
app.config['SECRET_KEY'] = 'samplesecretkey'
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
