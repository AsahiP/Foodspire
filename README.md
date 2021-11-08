<p align="center">
<img src="/static/images/foodspire_index.png" alt="index of Foodspire Webapp"
	title="Homepage for Foodspire" width="690" height="450" />
</p>



# :-: Foodspire


## Table Of Contents

1. Overview
2. Installation Instructions
3. Key learning points


</br>
### OVERVIEW

Foodspire is a full-stack web application intended to help the user find recipes based on a handful of culinary prefences. Using check-box questionnaire, the database containing recipe information returns recipes that align with all of those preferences. The user has the ability to save any recipes for later references. 

#### Technologies used:
    - Javascript
    - jQuery
    - AJAX
    - Python
    - Flask
    - Jinja2
    - HTML5
    - CSS  
    - Kaggle API dataset



<div align="center">

<img src="/static/images/foodspire_questionnaire.png" alt="Questionnaire from Foodspire Webapp"
	title="Preferences Questionnaire for Foodspire" width="275" height="360"/> <img src="/static/images/foodspire_fav_example.png" alt="Snippet of Favorite Recipes from Foodspire Webapp"
	title="Favorite Recipe" width="500" height="360"/>

</div>

<p align="center">
The Preferences Questionnaire and the Favorite Recipes page
</p>



<br/>

### INSTALLATION INSTRUCTIONS

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
   <br/> 2a. Open the terminal and desired directory to run the apps server in. In the terminal type:
   <br/> 2b. virtualenv env
    <br/>2c. source env/bin/activate
    <br/>2d. pip3 install -r requirements.txt
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
    <br/> 6a. The URL localhost:5000

    <br/> 6b. The port number displayed in the terminal when you run the server 
    in the previous step. It would look similar to this:
        Running on http://127/0/0/1:5000/ 

At any point if you would like to stop running the server, press Ctrl+C to quit



#### VIEW THE DATABASE

If you would like to run SQL queries to inspect the database run this command in the terminal:
    psql foodspire

You can either open a new terminal so this does not effect the server, or you 
can quit the server and run the command in the same terminal. 

To quit the database, press Ctrl-C


</br>

### KEY LEARNING POINTS

1. Be aware how information is formatted when using a dataset
        I had spent more time than I would have liked to experimenting with object type conversion 
        because of how the information was stored in my dataset. As well looking thoroughly over the 
        data to ensure that the data I need is organized in a usable way. This sounds like common sense,
        but the app's creation was initialized with food allergies in mind. Though I saw recipes were categorized with some allergy categories, there were other allergy categories that were more complex to sort and use. 
        For example, some allergies listed "Peanut allergies" but I would have to go through
        the entire recipe list to ensure there wasn't any other nut exposure in the ingredients or 
        instructions in order to fulfill the "nut allergy" preference.


2. Learning how to plan for a coding project such as this
        I had started with a Kanban-style planner in the beginning of my project. I stopped using it
        after the first week as I realized that I underestimated the break-down of the tasks I needed
        to complete. This skill improved over the course of the project.


3. How Javascript and AJAX interact with Python/Flask and HTML5
        Javascript and AJAX at times behaved in ways that I did not expect, and I wish I had taken more
        time to examine these behaviors before implementing JS and AJAX. Though I did get some 
        AJAX to work, there were many features I had forgone in order to complete as much of my
        project as I could in the given time. 

4. Detail my methods of approaching problems in the future
        I did note bugs and what code fixed it, though I didn't do much to summarize the
        my process. I feel this would be helpful information for any creative blocks
        in the future.
