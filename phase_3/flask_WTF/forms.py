from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(message= "We need your name!, it cannot be empty")])
    email = StringField("Email", validators=[DataRequired(message="Email message is required"), Email(message="Please enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired(message="Password is required"), Length(min=6, message="change password to at least 6 characters")])
    submit = SubmitField("Register")
