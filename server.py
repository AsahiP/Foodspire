"""Server for an Foodspire: an app that generates recipes based on user preference"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def show_homepage():
    """Display the homepage"""
    print("*******************")
    print("running homepage")
    print("*******************")

    login_button = request.args.get("login-button")

    return render_template("homepage.html")



@app.route("/loginpage")
def show_login_page():
    """Display the login page"""
    print("*******************")
    print("running display login")
    print("*******************")

    return render_template("login.html")



@app.route("/login", methods=["GET","POST"])
def validate_login():
    """contains logic to validate username/pass"""
    print("*******************")
    print("running login validation")
    print("*******************")

    
    username = request.form.get("username")
    print("*******************")
    print(f"username:{username}")

    passwordd = request.form.get("passwordd")
    print("*******************")
    print(f"password:{passwordd}")
    
    db_user = crud.get_user_by_username(username)
    print("*******************")
    print("ran crud.get_user_by_username")


    if db_user: #user object exists in database
        print("****")
        print("user in db")
        if passwordd == db_user.passwordd:
            print("***************")
            print("checking password")
            session["user_id"]=db_user.user_id
            print (session)
            return redirect("/dashboard")
        else:
            print("**********")
            print("incorrect password")
            flash("that is the incorrect password")
            return redirect ("/loginpage")
    else:
        print("*****")
        print("user not in db")
        flash("Username does not exist, please create an account")
        # return redirect("/") #change to route that will handle registration
        return redirect("/loginpage")



@app.route("/registeracct")
def show_registration_page():
    """display the registration page"""
    print("*******************")
    print("running display registration")
    print("*******************")


    return render_template("registeracct.html")



@app.route("/createacct", methods=["GET", "POST"]) #removed "GET" and changed to method not allowed error
def register_new_acct():
    """store user info in db, redirect to dashboard if input is valid"""
    print("*******************")
    print("running create acct function")
    print("*******************")

    #next step: crud function create user
    
    create_fname=request.form.get("create-fname")
    print("************")
    print(f"fname:{create_fname}")
    create_lname=request.form.get("create-lname")
    print("************")
    print(f"lname:{create_lname}")
    create_email=request.form.get("create-email")
    print("************")
    print(f"email:{create_email}")
    create_username=request.form.get("create-username")
    print("************")
    print(f"username:{create_username}")
    create_passwordd=request.form.get("create-passwordd")
    print("************")
    print(f"password:{create_passwordd}")

    db_user = crud.get_user_by_username(create_username)
    db_email = crud.get_user_by_email(create_email)
    print("*******")
    print("ran crud functions")

    if db_email:
        flash("An account already exists for this e-mail address")
        return redirect("/registeracct")
    elif db_user:
        flash("That username is taken")
        return redirect("/registeracct")
    else:
        print("******")
        print("running crud create_user")
        new_user=crud.create_user(create_fname, 
                        create_lname, 
                        create_email, 
                        create_username, 
                        create_passwordd)

        session['user_id']=new_user.user_id
        print("****************")
        print("account created")
        print("****************")
        return redirect("/dashboard")




@app.route("/dashboard")
def show_dashboard():
    """Display user dashboard"""
    print("****************")
    print("directed to dashboard")
    print("****************")
    
    if "user_id" in session:
        session_user= crud.get_user_by_user_id(session["user_id"])
        return render_template("dashboard.html", session_user=session_user)

    else: 
        return redirect("/login")

    

@app.route("/questions")
def show_questions():
    """display the questions page"""
    print("***********")
    print("displaying the questions page")

    # return render_template("questions.html") #original
    print("*"*20) #test
    print("TEST TEMPLATE") #test
    return render_template("questions_test.html") #this form is for testing edits



@app.route("/questions_answers", methods=["POST"])
def intake_questions_answers():
    """organizing questions from questions.html info to select recipes from db"""
    print("***********")
    print("running questions function")

    ##########
    #correspond categories in db to allergy values in html
    #store the allergy choices to a list
    #iterate through the list
    #if any of the allergies listed match corresponding categories
    #do not display those recipes
    ##########

    #if recipe has category that is nut-free/egg-free would easiest way
    #for later, come up with conditionals that retrieve data/categories correctly
    # allergies = request.form.getlist('allergy')
    # print("***************")
    # print(f"allergies: {allergies}")
    
    # dietary_preference = request.form.get("dietary-pref")
    # print("***************")
    # print(f"dietary_pref: {dietary_preference}")
    # dietary_pref_recipes=crud.get_recipes_by_preference(dietary_preference)
    

    # meal_time = request.form.get("meal-time")
    # meal_time_recipes=crud.get_recipes_by_preference(meal_time)
    # print("***************")
    # print(f"meal time: {meal_time}")


    # additional_pref = request.form.get("add-pref")
    # additional_pref_recipes = crud.get_recipes_by_preference(additional_pref)
    # print("***************")
    # print(f"additional pref: {additional_pref_recipes}")


    # return render_template("display_recipes.html", dietary_pref_recipes=dietary_pref_recipes, meal_time_recipes=meal_time_recipes, additional_pref_recipes=additional_pref_recipes) #original

        ## I refractored the original code lol
    lst_of_preferences = request.form.getlist("dietary-pref") #test
    print(f"\n\n\nlst_of_preferences = {lst_of_preferences}")
   

    recipes_from_lst_pref = crud.get_recipes_by_preference(lst_of_preferences) #test
     # recipes_from_lst_pref = crud.get_recipes_based_on_prefs(lst_of_preferences) #test

    return render_template("display_recipes_test.html", recipes_from_lst_pref=recipes_from_lst_pref) #test
 

# @app.route("/recipe_answers")
# def show_answers():
#     """Show the answers for recipe questionnaire"""

     
#     # take form info from prev route (user preferences)
#     # bring here to display 
#     #user confirms to generate recipes
#     #flash message easier

#     return render_template("recipe_answers.html")


# @app.route('/generated_recipes')
# def show_preferred_recipes():
#     """Show the recipes stored in database congruent with user questionnaire"""

#     # query from database and display in html
#     # allow users to save favorites

#     return render_template("display_recipes.html")

@app.route("/favorites", methods=["GET", "POST"])
def show_favrecipes():
    """Display favorite recipes"""
    print("****************")
    print("directed to favorites")
    print("****************")

    ########
    #store checked recipes in db table: FavRecipes
    #display db info on page
    #
    ######

    if request.method == "POST":
        print("************************")
        print("name of input from html")
        print(request.form.getlist("chosen-recipe-title"))

        chosen_recipe_titles = request.form.getlist("chosen-recipe-title")
        print("*"*20)
        print("values (checked boxes) stored in list from html")
        print(chosen_recipe_titles)

        for recipe_title in chosen_recipe_titles:
            print("*"*20)
            print("recipe is type:", type(recipe_title))
            print("starting for loop")
            recipe_obj = crud.get_recipe_by_title(recipe_title)
            fav_recipe_info = crud.create_fav_recipes(session["user_id"], recipe_obj.recipe_id)
            print("*"*30)
            print(f"fav_recipe_info={fav_recipe_info}")



    return render_template("favorites.html", chosen_recipe_titles=chosen_recipe_titles)

    #1. see if relationships set up correctly in sqlalchemy, check to see if checked recipe shows in database
    #2. how to query recipe to display in page User.recipes
    
    # run model.py interactively, practice using relationship, once established 
    # write crd to return recipes, use to populate favorite recipes page

    #after all that, handle input 
    #sep thang: handling favorited recipe from form 

    # chosen_recipe_titles = request.form.getlist("recipe-title")
    # chosen_recipe_instructions = request.form.getlist("instructions")
    # print("*******chosen recipe titles*********")
    # print(chosen_recipe_titles)
    # print("*******chosen recipe instructions*********")
    # print(chosen_recipe_instructions)




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)