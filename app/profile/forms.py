from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class WeightEntryForm(FlaskForm):
    weight = IntegerField('Weight', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit Data')


class SleepEntryForm(FlaskForm):
    sleep = IntegerField('Sleep', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit Data')


class GradeEntryForm(FlaskForm):
    grade = IntegerField('Grade', validators=[DataRequired()])
    gradeSubject = StringField('Subject', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit Data')
