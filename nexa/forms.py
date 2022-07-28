from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length,EqualTo


class RegisterationForm(FlaskForm):
username = StringField('Username', validators=[DataRequired(),Length(min=4,max=32)])
email = StringField('Email', validators=[DataRequired(),Email()])
password = PasswordField('Password', validators=[DataRequired()])
password_confirm = PasswordField('Password Confirm', validators=[DataRequired(),EqualTo('password')])
submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
email = StringField('Email', validators=[DataRequired(),Email()])
password = PasswordField('Password', validators=[DataRequired()])
submit = SubmitField("Log in")


class QuestionForm(FlaskForm):
body = TextAreaField("Question Body",validators=[DataRequired()])
option_1 = TextAreaField("Option 1",validators=[DataRequired()])
option_2 = TextAreaField("Option 2",validators=[DataRequired()])
option_3 = TextAreaField("Option 3",validators=[DataRequired()])
option_4 = TextAreaField("Option 4",validators=[DataRequired()])
correct_answer = RadioField("Correct answer",choices=['1','2','3','4'])


class AnswerForm(FlaskForm):
answer = RadioField("Select the correct answer",choices=['1','2','3','4'])


class ExamForm(FlaskForm):
title = StringField('Username', validators=[DataRequired(),Length(max=120)])
duration = IntegerField("Duration")
is_active = BooleanField("Is Active")
change_option_order = BooleanField("Change Option Order")
change_question_order = BooleanField("Change Question Order")
show_all = BooleanField("Show all questions at once")
question_based_timer = BooleanField("Question based timer")