"""Server for an Foodspire: an app that generates recipes based on user preference"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import crud, random
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
    print("route dashboard")
    print("****************")
    

    if "user_id" in session:
        # print("%"*30)
        # print("executing if user_id in session")
        session_user= crud.get_user_by_user_id(session["user_id"])

        # return redirect("/dashboard_fav_button", session_user=session_user)
        return render_template("dashboard.html", session_user=session_user)

    else: 
        return redirect("/login")

@app.route("/generate_rand_recipe.json")
def generate_rand_recipe_button():
    print("#"*30)
    print("route /generate_rand_recipe.json")

    rand_num = random.randint(0,20111)
    rand_lst = []

    rand_lst.append(rand_num) #would refactoring be creating another crud that doesnt need list?
    rand_recipe = crud.get_recipe_by_id(rand_lst)[0] #needs list passed in, (rand_lst)[0] to get int

    title= rand_recipe.recipe_title
    print("&"*30)
    print("title", title)
    ingredients= rand_recipe.ingredients_list[2:-2] #remove chars at beginning and end of list
    directions= rand_recipe.directions[2:-2]


    ingredients = ingredients.split('","') #returns back a list
    # ingredients = ingredients.replace('","', "\n")
    directions = directions.split('","')
    
    recipe_dict = {
        "title": title,
        "ingredients": ingredients,
        "directions": directions
    }
    
    print("$"*30)
    print(recipe_dict)
    return jsonify(recipe_dict)




app.route("/dashboard_fav_button", methods=["POST"])
def use_fav_button():
    print("\n#"*30)
    print("route dashboard_fav_button")

    rand_num = random.randint(0,20111)
    rand_lst = []

    if request.method == "POST":
        if rand_num:
            print("%"*30)
            print("executing if user_id in session")
            rand_lst.append(rand_num)
            rand_recipe = crud.get_recipe_by_id(rand_lst)
            
            return rand_recipe
        else:
            return redirect("/dashboard")

    # return (rand_lst, redirect("/dashboard"))
    # return redirect("/dashboard")
   

    

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
    

    lst_of_preferences = request.form.getlist("dietary-pref") #test
    print(f"\n\nlst_of_preferences = {lst_of_preferences}")

   
    #get recipe ids exclusively for recipes containing all chosen preferences
    recipes_ids_for_chosen_prefs = crud.get_recipe_ids_based_on_prefs(lst_of_preferences) 
    # print(f"\n\nrecipes_ids_for_chosen_prefs type = {recipes_ids_for_chosen_prefs}")

    # get recipe objects 
    recipe_obj = crud.get_recipe_by_id(recipes_ids_for_chosen_prefs)
    # print(f"\n\nrecipes_obj type = {recipe_obj}")


    return render_template("display_recipes.html", recipe_obj=recipe_obj)

#would like to show answers to the questionnaire for user to confirm


@app.route("/favorites", methods=["GET", "POST"])
def get_favrecipes():
    """Display favorite recipes/store recipes in db fav_recipes"""
    print("****************")
    print("route to favorites")
    print("****************")


    if request.method == "POST":

        chosen_recipe_titles = request.form.getlist("chosen-recipe-title")
        print("*"*20)
        print("values (checked boxes) stored in list from html")
        print(chosen_recipe_titles)

        #loop storing chosen recipes in db fav_recipes
        for recipe_title in chosen_recipe_titles:
            print("*"*20)
            # print("recipe is type:", type(recipe_title))
            print("starting for loop")
            recipe_obj = crud.get_recipe_by_title(recipe_title)
            fav_recipe_info = crud.create_fav_recipes(session["user_id"], recipe_obj.recipe_id)
            print("*"*30)
            # print(f"fav_recipe_info={fav_recipe_info}")


    favs = crud.get_prev_fav_recipes(session["user_id"])
    rec_ids = []
    for fav in favs:
        rec_ids.append(fav.recipe_id)

    recipes = crud.get_recipe_by_id(rec_ids)

    return render_template("favorites.html", favorite_recipe_titles=recipes)



"""
JS/AJAX

button for recipe, calls route that randomly selects recipe from db
eventually have random button -> suggest recipe button, take into acct favorited recipe
"""

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)