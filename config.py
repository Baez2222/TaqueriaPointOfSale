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
    # TODO: add SQLACLHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'db.sqlite3')
