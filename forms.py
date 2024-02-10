from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20])
  email = StringField('Email', vaildators = [DataRequired(), Email(), Length(min=10, max=30)])
  password = PasswordField('Password', validators = [DataRequired(), Length(min=5, max=20)])
  confirm_password = PasswordField('Confirm_Password', 
                                  validators = [DataRequired(), Length(min=5, max=20), EqualTo('password')])
  submit = SubmitField('Sign Up')
  
class LoginForm(FlaskForm):
  email = StringField('Email', vaildators = [DataRequired(), Email(), Length(min=10, max=30)])
  password = PasswordField('Password', validators = [DataRequired()])
  remember BooleanField('Remember Me')
  submit = SubmitField('Login')