from flask_wtf import FlaskForm
from sqlalchemy import or_
from sqlalchemy.orm import with_polymorphic
from wtforms import SelectField, StringField, PasswordField, ValidationError, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import User


class SignupForm(FlaskForm):
    username: StringField = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email(message='Valid email address required')])
    name: StringField = StringField ('Name', validators=[DataRequired ()])
    age= IntegerField ('Age', validators=[DataRequired ()])
    university = StringField ('University', validators=[DataRequired ()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

    def validate_email (self, email):
        if "@ucl.ac.uk" not in str(email):
            raise ValidationError('Please try again and register using a certified UCL email address.')
        user = User.query.filter_by (email=email.data).first()
        if user is not None:
            raise ValidationError('An account is already registered for that email address. Please use a different email address or Log In.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in?')
