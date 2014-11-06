#!/usr/bin/env python
import logging
from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

stream_handler = logging.StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(stream_handler)

app.config['SQLALCHEMY_DATABASE_URI'] = (environ.get('DATABASE_URL') or
                                         'sqlite:////tmp/test.db')
app.config['APIKEY'] = environ.get('APIKEY')

db = SQLAlchemy(app)
from models import *
from controllers import *
