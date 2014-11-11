__author__ = 'Administrator'

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

def ini_db():
    app = Flask(__name__)
    app.config.from_pyfile('../config/config.py')
    db = SQLAlchemy(app)
    return db