#!/usr/bin/env python
from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (environ.get('DATABASE_URL') or
                                         'sqlite:////tmp/test.db')
app.config['APIKEY'] = environ.get('APIKEY')

db = SQLAlchemy(app)
from models import *
from controllers import *
