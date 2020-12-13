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
    password = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    remember_me = db.Column(db.Boolean(), default=False)
    server = db.relationship('OrderModel', backref='server', lazy=False)

class ProductModel(UserMixin, db.Model):
    """
    Product Model: items to be sold
    """
    __tablename__ = 'products'
    productCode = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(25), index=True)
    priceEach = db.Column(db.Float)
    textDescription = db.Column(db.String(200), default=None)
    image = db.Column(db.LargeBinary)
    productSold = db.relationship('OrderDetailsModel', backref='product', lazy=False)

class OrderModel(UserMixin, db.Model):
    """
    Order Model
    """
    __tablename__ = 'orders'
    orderNumber = db.Column(db.Integer, primary_key=True)
    orderDate = db.Column(db.DateTime, index=True)
    comments = db.Column(db.Text)
    details = db.relationship('OrderDetailsModel', backref='order', lazy=False)
    serverID = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=False)

class OrderDetailsModel(UserMixin, db.Model):
    """
    OrderDetails Model: contents of each order
    """
    __tablename__ = 'orderdetails'
    orderNumber = db.Column(db.Integer, db.ForeignKey('order.orderNumber'), nullable=False, primary_key=True)
    productCode = db.Column(db.String(25), db.ForeignKey('product.productCode'), nullable=False)
    quantityOrdered = db.Column(db.Integer)