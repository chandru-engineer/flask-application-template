from dotenv import load_dotenv
import os


# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

# Access environment variables
secret_key = os.environ.get('SECRET_KEY')
debug = os.environ.get('DEBUG')
port = os.environ.get('port')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')




class Config:
    DEBUG = debug
    SECRET_KEY = secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

