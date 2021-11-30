import flask
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = 'studyapp/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'md'}

studyapp_obj = flask.Flask(__name__)

studyapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
studyapp_obj.config.from_mapping (
        SECRET_KEY = 'Milo',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        )

db=SQLAlchemy(studyapp_obj)

login=LoginManager(studyapp_obj)
login.login_view='login'

from studyapp import routes,models
