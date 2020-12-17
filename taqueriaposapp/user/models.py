from enum import unique
from operator import index
from usernames import is_safe_username
from random_username.generate import generate_username
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from taqueriaposapp.utils.sqlalchemy import ResourceMixin
from taqueriaposapp.extensions import db


class UserModel(ResourceMixin, UserMixin, db.Model):
    """
    User Model Object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    firstName = db.Column(db.String(20))
    lastName = db.Column(db.String(20))
    email = db.Column(db.String(60), unique=True, index=True)
    password = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    remember_me = db.Column(db.Boolean(), default=False)
    server = db.relationship('OrderModel', backref='server', lazy=False)

    def is_safe(self, username):
        """
        Checks if username is safe to use
        """
        if is_safe_username(username):
            self.username = username
        else:
            username = generate_username(1)[0]
            self.username = username

    def set_password(self, password):
        """
        Encrypts password
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks password against database
        returns: Boolean
        """
        return check_password_hash(self.password, password)


class ProductModel(ResourceMixin, db.Model):
    """
    Product Model: items to be sold
    """
    __tablename__ = 'products'
    productCode = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(25), index=True)
    priceEach = db.Column(db.Float)
    textDescription = db.Column(db.String(200), default=None)
    image = db.Column(db.LargeBinary)
    productSold = db.relationship(
        'OrderDetailsModel', backref='product', lazy=False)


class OrderModel(ResourceMixin, db.Model):
    """
    Order Model
    """
    __tablename__ = 'orders'
    orderNumber = db.Column(db.Integer, primary_key=True)
    orderDate = db.Column(db.DateTime, index=True)
    comments = db.Column(db.Text)
    details = db.relationship('OrderDetailsModel', backref='order', lazy=False)
    serverID = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)


class OrderDetailsModel(ResourceMixin, db.Model):
    """
    OrderDetails Model: contents of each order
    """
    __tablename__ = 'orderdetails'
    id = db.Column(db.Integer, primary_key=True)
    orderNumber = db.Column(db.Integer, db.ForeignKey(
        'orders.orderNumber'), nullable=False, primary_key=True)
    productCode = db.Column(db.String(25), db.ForeignKey(
        'products.productCode'), nullable=False)
    quantityOrdered = db.Column(db.Integer)
