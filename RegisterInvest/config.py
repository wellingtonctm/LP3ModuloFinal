import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(32)
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Data', "myBase.db")