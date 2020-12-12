from operator import index
from flask_login import UserMixin
from taqueriaposapp.extensions import db


class UserModel(UserMixin, db.Model):
    """
    User Model Object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String())
    remember_me = db.Column(db.Boolean(), default=False)
