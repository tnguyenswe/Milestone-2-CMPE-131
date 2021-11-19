from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class SignupForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    signup=SubmitField("Sign Up")

class UploadForm(FlaskForm):
    file = FileField()