from flask import Blueprint, render_template
from .models import UserModel
from .forms import LoginForm, RegisterForm

user = Blueprint('user', __name__,
                 template_folder='templates', url_prefix='/user')


@user.route('/login')
def login():
    """
    User Login View
    """
    form = LoginForm()
    return render_template('user/login.html', title='Login', form=form)


@user.route('/register')
def register():
    """
    User Register View
    """
    form = RegisterForm()
    return render_template('user/register.html', title='Register', form=form)


@user.route('/dashboard')
def dashboard():
    """
    User Dashboard View
    """
    return render_template('user/dashboard.html', title='Dashboard')
