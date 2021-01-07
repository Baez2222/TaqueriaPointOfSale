from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from .models import UserModel
from .forms import LoginForm, RegisterForm, CartForm
import os

user = Blueprint('user', __name__,
                 template_folder='templates', url_prefix='/user')

cartList = []


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
    return render_template('user/pointofsale.html', title='PointOfSale', form=form, cartList=cartList)

@user.route('/addCartItem')
def addCartItem():
    try:
        itemName = ["taco", 2.00]
        return jsonify(result=cartList.append(itemName))
    except Exception as e:
	    return str(e)
    
