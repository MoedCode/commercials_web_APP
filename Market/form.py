from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField

class RegisterForm(FlaskForm):
    email = StringField(label='email')
    password = PasswordField(label='password')
    conf_PWD  = PasswordField(label='confirm password')
    first_name = StringField(label='First Name')
    last_name = StringField(label='Last Name')
    nickname = StringField(label='Nickname')
    photo = FileField(label='photo')
    submit = SubmitField(label='Submit')
