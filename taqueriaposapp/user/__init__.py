from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from .models import UserModel, OrderModel, OrderDetailsModel
from .forms import LoginForm, RegisterForm, CartForm
import os
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy
import pymysql

user = Blueprint('user', __name__,
                 template_folder='templates', url_prefix='/user')

cartList = []
def emptyCart():
    global cartList
    cartList = []

engine = sqlalchemy.create_engine('mysql+pymysql://' + os.getenv("DB_USER") + ':' + os.getenv("DB_PASS") + '@' + os.getenv("DB_HOST") + ':' + os.getenv("DB_PORT") + '/' + os.getenv("DB_NAME"))
Session = scoped_session(sessionmaker(bind=engine))
s = Session()


@user.route('/login', methods=['POST', 'GET'])
def login():
    """
    User Login View
    """
    form = LoginForm()
    return render_template('user/login.html', title='Login', form=form)


@user.route('/register', methods=['POST', 'GET'])
def register():
    """
    User Register View
    """
    form = RegisterForm()
    if form.validate_on_submit():
        u = UserModel(email=form.email.data)
        u.is_safe(form.username.data)
        u.set_password(form.password.data)
        u.save()
        return redirect(url_for('.login'))
    return render_template('user/register.html', title='Register', form=form)


@user.route('/dashboard')
def dashboard():
    """
    User Dashboard View
    """
    return render_template('user/dashboard.html', title='Dashboard')

@user.route('/pointofsale', methods=['POST', 'GET'])
def pointofsale():
    """
    Point of Sale main page:
        - menu items
        - items in cart
        - keypad
        - menu options bar on top
    """
    form = CartForm()

    if form.validate_on_submit():
        s.add(OrderModel(comments="test", serverID=123))
        emptyCart()
        return redirect(url_for('.pointofsale'))
    return render_template('user/pointofsale.html', title='PointOfSale', form=form, cartList=cartList)

@user.route('/addCartItem')
def addCartItem():
    try:
        item = request.args.get('itemName', 0, type=str)
        uniqueBool = True
        for i in cartList:
            if item == i[0]:
                i[2] += 1
                uniqueBool = False
        if uniqueBool:
            item = [item, 2.00, 1]
            cartList.append(item)
        return jsonify(result=cartList)
    except Exception as e:
	    return str(e)