from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

import config

from endpoints.home import home
from endpoints.upload import upload

# folder where file uploads exist
UPLOAD_FOLDER = config.server_path+'/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(upload, url_prefix='')

# enables cors
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = config.sql_alchemy_database_uri
app.config['SECRET_KEY'] = config.secret_key
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
    print(config.server_path + 'static/uploads/')
