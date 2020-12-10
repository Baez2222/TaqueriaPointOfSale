import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
try:
    load_dotenv(os.path.join(basedir, '.env'))
except FileNotFoundError:
    load_dotenv(os.path.join(basedir, '.env_sample'))


class BaseConfig(object):
    """
    Base Configuration Settings
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    """
    Development Configuration Settings
    """
    # TODO: add SQLACLHEMY_DATABASE_URI
    pass
