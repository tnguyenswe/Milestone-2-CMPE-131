from studyapp import studyapp_obj
from flask import render_template, flash, redirect,request
from studyapp.forms import LoginForm, SignupForm, UploadForm
from studyapp.models import User,Post
from flask_login import current_user,login_user,logout_user,login_required
from studyapp import db
import markdown.extensions.fenced_code
from werkzeug.utils import secure_filename

@studyapp_obj.route("/loggedin")
@login_required
def log():
    return render_template('loggedin.html')

@studyapp_obj.route("/loggedout")
def logout():
    logout_user()
    return redirect('/')


@studyapp_obj.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/loggedin')
    return render_template('login.html',form=form)


@studyapp_obj.route('/signup',methods=['GET','POST'])
def signup():
    form=SignupForm()
    all_users=User.query.all()
    if form.validate_on_submit():
        u=User(username=form.username.data,password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect ('/login')
    return render_template('signup.html',form=form)


@studyapp_obj.route('/')
def home():
    title = "Homepage"
    return render_template('home.html',title=title)

@studyapp_obj.route("/md_to_flashcard", methods=['GET', 'POST'])
def markdown_to_flashcard():
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(filename)
        open_file = open(filename, "r")
        md_template_string = markdown.markdown(
        open_file.read(), extensions=["fenced_code", "codehilite"]
        )
        return md_template_string
    return render_template('md_to_flashcard.html', form=form)


# @studyapp_obj.route('/flashcard_to_pdf')
# def flashcard_to_pdf():
    
# @studyapp_obj.route('/md_to_pdf')
# def md_to_pdf():

# @studyapp_obj.route('/render_md')
# def render_md():