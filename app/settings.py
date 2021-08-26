from io import StringIO
from os import environ

from dotenv import load_dotenv

FLASK_ENV = environ.get('FLASK_ENV', 'test')

load_dotenv('.env' if FLASK_ENV != 'test' else '.env.test', override=True)


class Settings:
    SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
