# Here is a list of all the functions available to be used in our app:

Documentation for: 

    studyapp/
        routes.py

* `log():`
	User will be redirected to this webpage only if the user is logged into their account.

* `login():`
	User is redirected to homepage after logging out of account.

* `login():`
	User is able to log into their account after signing up using a username and password.
	
	Parameters:
		Username and Password
	Returns:
		Account for user

* `signup():`
	User enters a username and password and is able to create and accountthat will be used to log in.
	Parameters:
	Username and password used to create account
	Return:
	An account username and password to use when logging in.


* `markdown_to_flashcard():` 

    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): The HTML version of the markdown file.

* `flashcard_to_pdf():`

    Converts markdown files to flash cards.

            Parameters:
                    file (html): A flashcard (html file)

            Returns:
                    file (pdf): The PDF version of the flashcard (html file).

* `md_to_pdf():`

    
    Converts markdown files to PDF's.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (PDF): The PDF version of the markdown file.
    
* `render_md():`

    Converts markdown files to flash cards.

            Parameters:
                    file (md): A markdown file

            Returns:
                    file (html): Outputs the markdown file as HTML.
