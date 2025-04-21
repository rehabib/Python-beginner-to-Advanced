# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))# Get the directory of the current file/config.py

class Config:
    SECRET_KEY ="6fd6e607933cd668aff427d9d77fade0"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'library.db') # SQLite databasee
    SQLALCHEMY_TRACK_MODIFICATIONS = False
