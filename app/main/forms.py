from flask_wtf import FlaskForm
import datetime
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from sqlalchemy import DateTime


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')


class CreatePostForm(FlaskForm):

    content = StringField('Content', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    date = DateField()
    tags = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Post')
    posterId = IntegerField()
    likes = IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date.data = datetime.date.today()

class CreateComment(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired])
    date = DateField()
    commenterId = IntegerField()
    commentedPostId = IntegerField()
    submit = SubmitField('Comment')