OVERVIEW

This app was created to help the user find a recipe based on their recipe preferences. Users can store their "favorited" recipes for later reference

Languages used:
    - Javascript
    - jQuiery
    - Python
    - Flask
    - Jinja
    - HTML
    - CSS  



INSTALLATION INSTRUCTIONS

1. This app has come with two files of .json data located in the /data directory.
    "five_test_recipes.json" contains 5 recipes and was intended for test purposes.
    "full_recipes.json.zip" contains a much larger set of data, and was 
    meant to be used with the app. 


You have one of two options for the first step:
    By default the app is set to use "full_recipes.json". To use it, unzip full_recipes.json.zip. 
    Make sure that the unzipped file is in the project-foodspire/data directory.

    To use the smaller file, you need to change a piece of code within the seed.py file (located in the project-foodspire directory). 
    Scroll to line 28 in seed.py. It should read:
        with open('data/full_recipes.json') as f:
    Within the parentheses, change all of the code to 
        'five_test_recipes.json'
    This will change the default data to the data in five_test_recipes.json.
    Save the file to submit the change.
    Note: This can be done with any .json file you would like to use, provided the format is the same to the json files provided (a list of dictionaries)



2. Set up a virtual environment
    2a. Open the terminal and desired directory to run the apps server in. 
        In the terminal type:
        2b. virtualenv env
        2c. source env/bin/activate
        2d. pip3 install -r requirements.txt
    You should see an indicator to the left or your command line that displays you are 
    in the virtual environment (ie. (env))
    To exit the virtual environment, use keys Ctrl + C 


3. Run seed.py
    This will populate the database with the data in the json file, along with 
    initial dummy user information for test purposes. 
    In the terminal run the command:
            python3 seed.py


4. Run server.py
    This will run the server to display the app in your web browser
    In the terminal run the command:
            python3 server.py


5. Open up a browser page (preferably in Incognito mode)


6. Enter either of these into the address bar:
    6a. The URL localhost:5000

    6b. The port number displayed in the terminal when you run the server 
    in the previous step. It would look similar to this:
        Running on http://127/0/0/1:5000/ 

At any point if you would like to stop running the server, press Ctrl+C to quit



VIEW THE DATABASE

If you would like to run SQL queries to inspect the database run this command in the terminal:
    psql foodspire

You can either open a new terminal so this does not effect the server, or you 
can quit the server and run the command in the same terminal. 

To quit the database, press Ctrl-C



NAVIGATION

The home page will display an overview of the app and a login or create account button.
Press the button to be directed to the login page.

If you have user information that is stored in the database- at minimum a username and password- 
you can log in to the dashboard.

If you would like to create an account, press the "Create Account" link below the login form. 
    To create an account enter a 
        - username with a maximum of 20 characters and a minimum of 4.
        - a first name with a maximum of 20 characters and a minimum of 4.
        - a last name with a maximum of 20 characters and a minimum of 4.
        - a passowrd with a maximum of 20 characters and a minimum of 4.

There are three links to visit from the Dashboard, as well as one button

1. The recipe preference questionnaire
    From here you provide your recipe preferences by checking boxes on the right 
    of the displayed preferences

    The following page will display the recipes correlated to all of the preferences
    you have chosen

    You can select the recipes you would like to save by selecting the checkboxes 
    to the left of the recipe names, and pressing the "Save Recipe" button. This 
    will save the recipes to the user's Favorites page

    The questionnaire can be visited an unlimited number of times

2. The users favorite recipes
    This page displays recipes the user has chosen from the recipes generated
    after the questionnaire. If the user is new, the page will be empty.

    To see the recipes, click the recipe title to see the recipe details scroll
    down from the title. To hide the details click the recipe title again.
    
    The page allows to delete favorite recipes. This can be done by checking the boxes
    to the left of the recipe titles that the user would like to have deleted, and
    submitting the deletion by pressing the "Delete Recipes" button.
    This action cannot be undone, and there is currently no confirmation to ensure
    that these recipes are indeed the ones you desire to delete.

3. The users account information
    The user can view and edit their account information from here, such
    as their first name, last name, e-mail address, and password. Pressing the 
    "Edit" button next to the information the user would like to change will
    cause an input bar to scroll down. Input the new information and press "Submit"
    to the right of the text bar to submit.
    There is form validation, so heed any errors to ensure you are entering the
    information correctly. 


The button generates a random recipe on the dashboard for the user to see
    







