from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField

class UserRegisterForm(FlaskForm):
    username = StringField("Username")
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    password = PasswordField("Password", [validators.DataRequired(), validators.EqualTo('confirm_password')])
    confirm_password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Register')


