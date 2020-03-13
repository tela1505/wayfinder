from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class CreatePost(FlaskForm):
    content = StringField('Content', validators=DataRequired)
    title = StringField('Content', validators=DataRequired)
    tags = StringField('Tag', validators=DataRequired)