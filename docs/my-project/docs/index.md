
## Running the app

- Step 1: git clone git@github.com:tnguyenswe/Milestone-2-CMPE-131.git
- Step 2: cd Milestone-2-CMPE-131
- Step 3: install the dependencies using the commands below
- Step 4: python3 run.py

## To view the app

Navigate to [localhost:5000](http://localhost:5000/)

## Dependencies

* `pip3 install flask-login`
* `pip3 install flask_sqlalchemy`
* `pip3 install flask_wtf`
* `pip3 install pdfkit`
* `pip3 install wkhtmltopdf`
* `pip3 install markdown`
* `pip3 install mkdocs`


## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout
    docs/ # This holds all our documentation for this project
        my-project/
            docs/
                index.md # General documentation for running the app and the project layout
                functions.md # Documentation of all functions/classes available to the user

    studyapp/ # Contains the heart of the Flask app
        __pycache__/ # Cache of __init__.py, forms.py, models.py, and routes.py
        flashcards/  # Flashcards are saved here from the functions listed in routes.py
        render_md/  # To render md files, we save those files somewhere then render them- this is where we save them
        static/ # Holds JS files for the timer
        templates/ # Holds the different HTML templates for the different use cases
        __init__.py # Turns our app into a module
        app.db # Holds the SQLAlchemy DB information for our app
        forms.py # Create different wtforms for our app
        models.py # The different models for our DB
        routes.py # The different routes available on the Flask app

    testing uploads/ # As the name suggests, this is for testing uploads to the app

    README.md # Secondary README
    run.py # Python script to run the Flask app

# [Click here to view documentation of functions/classes](http://localhost:8000/functions)