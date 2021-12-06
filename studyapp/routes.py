from studyapp import studyapp_obj, ALLOWED_EXTENSIONS
from flask import render_template, flash, redirect,request
from studyapp.forms import LoginForm, SignupForm, UploadForm, SearchTextForm,ToDoForm,FlashCardForm, ChangeNameForm, TimeScheduleForm
from studyapp.models import User,Post,ToDo,CreateFlashcard, timeSchedule
from flask_login import current_user,login_user,logout_user,login_required
from studyapp import db
from werkzeug.utils import secure_filename
import pdfkit
from markdown import markdown
import os
import glob

#requires user to be logged in
@studyapp_obj.route("/loggedin")
@login_required
def log():
    '''
        User will be redirected to this webpage only if the user is logged into their account.
    '''
    return render_template('home.html')

#allows users to logout and redirects to splash page
@studyapp_obj.route("/logout")
def logout():
    '''
        User is redirected to splash page after logging out of account.
    '''
    logout_user()
    return render_template('splash.html')

#allows users to logout and redirects to homepage
@studyapp_obj.route("/")
def splash():
    '''
        Splash page for web app
    '''
    logout_user()
    return render_template('splash.html')

#LoginForm allows user to login into account after account is created
@studyapp_obj.route('/login',methods=['GET','POST'])
def login():
    '''
        User is able to to log into their account after signing up.

        Parameters:
            username and password
        Returns:
            user creates an account and is able to log into account
    '''
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/home')
    return render_template('login.html',form=form)

#Signup form allows user to create an account with a username and password
@studyapp_obj.route('/signup',methods=['GET','POST'])
def signup():
    '''
        User enters a username and password and is able to create an account that will be used to log in.

        Parameters:
            Username and password used to create account
        Returns:
            An account username and password to use when logging in
    '''
    form=SignupForm()
    all_users=User.query.all()
    if form.validate_on_submit():
        #username and password is saved to the database for future use
        u=User(username=form.username.data,password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect ('/login')
    return render_template('signup.html',form=form)

#routes to the homepage
@studyapp_obj.route('/home')
def home():
    title = "Homepage"
    return render_template('home.html',title=title)

@studyapp_obj.route("/md_to_flashcard", methods=['GET', 'POST'])
def markdown_to_flashcard():
    '''
    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): The HTML version of the markdown file.
    '''
    import markdown.extensions.fenced_code
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        # save the md file in a flashcards directory
        form.file.data.save("studyapp/flashcards/" + filename)
        open_file = open("studyapp/flashcards/" + filename, "r")
        # convert md to html so render template can render it
        md_template_string = markdown.markdown(
        open_file.read(), extensions=["fenced_code", "codehilite"]
        )
        return render_template('md_to_flashcard.html', form=form, success=True, md_file = md_template_string)
    return render_template('md_to_flashcard.html', form=form)

@studyapp_obj.route('/flashcard_to_pdf', methods=['GET', 'POST'])
def flashcard_to_pdf():
    '''
    Converts markdown files to flash cards.

            Parameters:
                    file (html): A flashcard (html file)

            Returns:
                    file (pdf): The PDF version of the flashcard (html file).
    '''
    
    import pdfkit
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        # save the md file in a flashcards directory
        form.file.data.save("studyapp/flashcards/" + filename)
        input_filename = 'studyapp/flashcards/' + filename
        output_filename = input_filename.split(".html")
        output_filename = output_filename[0] + '.pdf'
        pdfkit.from_file(input_filename, output_filename)
        return render_template('flashcard_to_pdf.html', form=form, pdf=output_filename)        
    return render_template('flashcard_to_pdf.html', form=form)
    
# convert markdown to pdf
@studyapp_obj.route('/md_to_pdf', methods=['GET', 'POST'])
def md_to_pdf():
    '''
    Converts markdown files to PDF's.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (PDF): The PDF version of the markdown file.
    '''
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        form.file.data.save("studyapp/flashcards/" + filename)
        # save the md file name and change to pdf file name
        input_filename = 'studyapp/flashcards/' + filename
        output_filename = input_filename.split(".md")
        output_filename = output_filename[0] + '.pdf'
        
        #convert md file to pdf file
        with open(input_filename, 'r') as f:
            html_text = markdown(f.read(), output_format='html4')
        pdfkit.from_string(html_text, output_filename)
        return render_template('md_to_pdf.html', form=form, pdf=output_filename)
    
    return render_template('md_to_pdf.html', form=form)

#render markdown
@studyapp_obj.route('/render_md', methods=['GET', 'POST'])
def render_md():
    '''
    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): Outputs the markdown file as HTML.
    '''
    
    import markdown.extensions.fenced_code
    form = UploadForm()
    if form.validate_on_submit():
        # get file name from form
        filename = secure_filename(form.file.data.filename)
        form.file.data.save("studyapp/render_md/" + filename)
        open_file = open("studyapp/render_md/" + filename, "r")
        # convert md to html
        md_template_string = markdown.markdown(
        open_file.read(), extensions=["fenced_code", "codehilite"]
        )
        return md_template_string
    return render_template('render_md.html', form=form)


#allows users to create a to do list by typing into the text box and submitting
@studyapp_obj.route("/todo",methods=['GET','POST'])
def todo_list():
    form=ToDoForm()
    todolist=ToDo.query.all()
    if form.validate_on_submit():
        #adds to-do item to list
        item=ToDo(todo=form.todo.data)
        db.session.add(item)
        db.session.commit()
        return redirect ('/todo')
    return render_template('todo.html',form=form,todolist=todolist)

@studyapp_obj.route("/pomorodo")
def pomorodotimer():
    '''
    Creates a pomodoro timer for the user
        Parameters:
            none
        Returns:
            text (html): Reminds the user every 25 minutes to take a break
    '''
    return render_template("pomorodo.html")



@studyapp_obj.route("/trackHours", methods=['GET'])
def timeTracker():
    '''
    creates a timer for the user
    '''
    return render_template('TrackTime.html')

# code from this wesite was referenced to write the following two methods
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/

def allowed_file(filename):
    '''
    Checks if the file uploaded is of supported format..

            Parameters:
                    filename: name of the to check

            Returns:
                    boolean: True if the file is allowed, else false.
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@studyapp_obj.route("/searchText", methods=['GET', 'POST'])
def searchText():
    '''
    Emboldens a specified text on an input file.

            Parameters:
                    file (pdf,txt,md): A text file of allowed extension.

            Returns:
                    file (html): outputs the text of the file in html and emboldens the searched text.
    '''
    form = SearchTextForm()
    if form.validate_on_submit():
        if form.input_file.data.filename == '':
            flash('No selected file')
            return redirect('/searchText')
        if form.input_file.data and allowed_file(form.input_file.data.filename):
            #To get filename from form
            filename = secure_filename(form.input_file.data.filename)
            #To save file with new path
            form.input_file.data.save(os.path.join(studyapp_obj.config['UPLOAD_FOLDER'], filename))
            #opening the file to get text in file
            file = open("studyapp/static/uploads/" + filename, encoding="utf8")
            file =file.read()
            #To get the text to be searched from forms
            search_word = form.text.data
            if search_word in file:
                #sorrounding the searched word with html <strong> tags to bold the text.
                file = file.replace(search_word, '<strong>'+search_word+'</strong>')
            else:
                flash('Searched worrd is not present in file.')

            return render_template('searchText.html', file=file, form=form)
    return render_template('searchText.html', form=form)

@studyapp_obj.route("/flashcard", methods=['GET', 'POST'])
def create_flashcards():
    '''
    Creates a flashcard and adds it to our DB

            Parameters:
                    file (md): MD File to be converted to flash card and added to our DB

            Returns:
                    text (html): Outputs a success message if the flashcard was added successfully.
    '''
    form = FlashCardForm()
    user_flashcards = CreateFlashcard.query.filter_by(user=current_user).all()
    if form.validate_on_submit():
        flashcard = CreateFlashcard(front=form.front.data, back=form.back.data, user=current_user)
        db.session.add(CreateFlashcard)
        db.session.commit()
        flash('Successfully', 'success')
        return redirect(url_for('create_flashcards'))
    return render_template('createflashcard.html', form=form, user_flashcards=user_flashcards)

@studyapp_obj.route("/changefile", methods=['GET','POST'])
def change_file():
    """ User is able to change name of file by entering exisiting name and new name and pressing submit.
    """
    form=ChangeNameForm()
    filename=(os.listdir())
    filename=glob.glob('*.txt')
    if form.validate_on_submit():
        file_name=(form.file_name.data)
        rename_file=(form.rename_file.data)
        os.rename(file_name,rename_file)
        return redirect('/changefile')
    return render_template('changefile.html',form=form,filename=filename)

@studyapp_obj.route("/timeSchedule", methods=['GET', 'POST'])
def TimeSchedule():
    '''
    creates a schedule for user with a task and the scheduled time span

            Parameters:
                    stask name and start and end time for schedule.

            Returns:
                   (html): outputs schedule in a list format
    '''
    form = TimeScheduleForm()

    if form.validate_on_submit():
        task = timeSchedule(taskName=form.TaskName.data, startTime=form.StartTime.data, endTime=form.EndTime.data)
        db.session.add(task)
        db.session.commit()
        return redirect("/timeSchedule")



    Tasks = timeSchedule.query.order_by(timeSchedule.id).all()

    return render_template('timeSchedule.html', Tasks = Tasks, form=form)
