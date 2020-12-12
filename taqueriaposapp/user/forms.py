from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    """
    User Login Form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    """
    User Registration Form
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Verify Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class ProfileForm(FlaskForm):
    """
    User Profile Form
    """
    pass
