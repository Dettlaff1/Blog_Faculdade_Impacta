import os

SECRET_KEY = os.urandom(32)

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False