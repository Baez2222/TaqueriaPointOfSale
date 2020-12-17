from usernames import is_safe_username
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from taqueriaposapp.user.models import UserModel


class LoginForm(FlaskForm):
    """
    User Login Form
    """
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=4, max=6)], id="keypadVar")
    submit = SubmitField('Enter')


class RegisterForm(FlaskForm):
    """
    User Registration Form
    """
    username = StringField('Username', validators=[DataRequired()],
                           render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={"placeholder": "Email", "autocomplete": "off"})
    password = PasswordField('Password', validators=[DataRequired()],
                             render_kw={"placeholder": "Password"})
    password2 = PasswordField('Verify Password', validators=[
                              DataRequired(), EqualTo('password')],
                              render_kw={"placeholder": "Verify Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        Checks if username is in use
        returns: Boolean
        """
        user = UserModel.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already in use.")

    def validate_email(self, email):
        """
        Checks if email is in use
        returns: Boolean
        """
        user = UserModel.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already in use.")


class ProfileForm(FlaskForm):
    """
    User Profile Form
    """
    pass
