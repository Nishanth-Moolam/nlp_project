from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

# from views import views
# from auth import auth


app = Flask(__name__)
# app.register_blueprint(views, url_prefix='')
# app.register_blueprint(auth, url_prefix='')

CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nlpproject.db"
app.config['SECRET_KEY'] = 'samplesecretkey'
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
