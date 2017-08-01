import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
