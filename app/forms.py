from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
 