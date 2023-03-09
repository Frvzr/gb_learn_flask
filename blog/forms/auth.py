from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class LoginForm(FlaskForm):
    username = StringField("username", [validators.DataRequired()],)
    password = PasswordField("Password", [validators.DataRequired()],)
    submit = SubmitField("Login")