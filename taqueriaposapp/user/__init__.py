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
        # commit order to order model
        orderAdded = s.add(OrderModel(comments="test", serverID=123))
        s.commit()
        # commit order details of current order into OrderDetails table
        currOrderNumber = s.execute("SELECT LAST_INSERT_ID()").fetchone()[0]
        for item in cartList:
            s.add(OrderDetailsModel(orderNumber=currOrderNumber, productCode=item[1], quantityOrdered=item[3]))
            s.commit()
        emptyCart()
        return redirect(url_for('.pointofsale'))
    
    return render_template('user/pointofsale.html', title='PointOfSale', form=form, cartList=cartList)

@user.route('/addCartItem')
def addCartItem():
    try:
        itemCode = request.args.get('itemCode', 0, type=int)
        if itemCode != 0:
            itemName = s.execute("SELECT p.productName FROM products p WHERE p.productCode = %s" % (itemCode)).first()
            uniqueBool = True
            for i in cartList:
                if itemCode == i[2]:
                    i[0] = False
                    uniqueBool = False
            if uniqueBool:
                itemCode = [False, str(itemName.productName), itemCode, 2.00, 0]
                cartList.append(itemCode)
        else:
            for i in cartList:
                if i[0] == False:
                    quantity = request.args.get('quantity', 0, type=int)
                    i[4] += quantity
                    i[0] = True
                    break
        return jsonify(result=cartList)
    except Exception as e:
	    return str(e)