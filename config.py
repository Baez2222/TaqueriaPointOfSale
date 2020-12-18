import os
import secrets
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

secretkey = secrets.token_urlsafe(32)

try:
    load_dotenv(os.path.join(basedir, '.env'))
except FileNotFoundError:
    print('.env file not found use .env_sample for reference')


class BaseConfig(object):
    """
    Base Configuration Settings
    """
    SECRET_KEY = os.getenv('SECRET_KEY') or secretkey
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    """
    Development Configuration Settings
    """
    DB_USER=os.getenv("DB_USER")
    DB_PASS=os.getenv("DB_PASS")
    DB_NAME=os.getenv("DB_NAME")
    DB_HOST=os.getenv("DB_HOST")
    DB_PORT=os.getenv("DB_PORT") or 3306
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
