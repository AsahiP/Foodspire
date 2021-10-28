"""Server for an Foodspire: an app that generates recipes based on user preference"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, url_for)
from model import connect_to_db
from jinja2 import StrictUndefined
from werkzeug.utils import secure_filename
import crud, random, os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #to allow image uploads

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)



@app.route("/")
def show_homepage():
    """Display the homepage"""
    print("*******************")
    print("route to homepage- displaying homepage")
    print("*******************")

    return render_template("homepage.html")



@app.route("/loginpage")
def show_login_page():
    """Display the login page"""
    print("#"*30)
    print("route loginpage- displaying login page")
    print("#"*30)

    return render_template("login.html")



@app.route("/login", methods=["GET","POST"])
def validate_login():
    """contains logic to validate username/pass"""
    print("#"*30)
    print("route to login validation")
    print("#"*30)

    
    username = request.form.get("username")
    print("-"*50)
    print(f"username:{username}")

    passwordd = request.form.get("passwordd")
    print("-"*50)
    print(f"password:{passwordd}")
    
    db_user = crud.get_user_by_username(username)
    print("-"*50)
    print("ran crud.get_user_by_username")


    if db_user: #user object exists in database
        print("-"*50)
        print("user in db")
        if passwordd == db_user.passwordd:
            print("-"*50)
            print("checking password")
            session["user_id"]=db_user.user_id
            print (session)
            return redirect("/dashboard")
        else:
            print("-"*50)
            print("incorrect password")
            flash("that is the incorrect password")
            return redirect ("/loginpage")
    else:
        print("-"*50)
        print("user not in db")
        flash("Username does not exist, please create an account")
        # return redirect("/") #change to route that will handle registration
        return redirect("/loginpage")



@app.route("/registeracct")
def show_registration_page():
    """display the registration page"""
    print("#"*30)
    print("running display registration")
    print("#"*30)


    return render_template("registeracct.html")



@app.route("/createacct", methods=["GET", "POST"]) #removed "GET" and changed to method not allowed error
def register_new_acct():
    """store user info in db, redirect to dashboard if input is valid"""
    print("*"*50)
    print("route to createacct- store user info in db, go to dash if input valid")
    print("*"*50)

    
    create_fname=request.form.get("create-fname")
    print("-"*50)
    print(f"fname:{create_fname}")
    create_lname=request.form.get("create-lname")
    print("-"*50)
    print(f"lname:{create_lname}")
    create_email=request.form.get("create-email")
    print("-"*50)
    print(f"email:{create_email}")
    create_username=request.form.get("create-username")
    print("-"*50)
    print(f"username:{create_username}")
    create_passwordd=request.form.get("create-passwordd")
    print("-"*50)
    print(f"password:{create_passwordd}")

    db_user = crud.get_user_by_username(create_username)
    db_email = crud.get_user_by_email(create_email)
    print("-"*50)
    print("ran crud functions get username, get email")

    if db_email:
        flash("An account already exists for this e-mail address")
        return redirect("/registeracct")
    elif db_user:
        flash("That username is taken")
        return redirect("/registeracct")
    else:
        print("-"*50)
        print("running crud create_user")
        new_user=crud.create_user(create_fname, 
                        create_lname, 
                        create_email, 
                        create_username, 
                        create_passwordd)

        session['user_id']=new_user.user_id
        print("-"*50)
        print("account created")
        return redirect("/dashboard")




@app.route("/dashboard")
def show_dashboard():
    """Display user dashboard"""
    print("#"*30)
    print("route dashboard- showing dashboard or redirecting to login")
    print("#"*30)
    

    if "user_id" in session:

        session_user= crud.get_user_by_user_id(session["user_id"])

        return render_template("dashboard.html", session_user=session_user)

    else: 
        return redirect("/login")


@app.route("/generate_rand_recipe.json")
def generate_rand_recipe_button():
    print("#"*30)
    print("route /generate_rand_recipe.json")
    print("#"*30)

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




app.route("/dashboard_rand_button", methods=["POST"])
def use_fav_button():
    print("*"*50)
    print("route dashboard_rand_button- logic to pick recipe when click dashboard button")
    print("*"*50)

    rand_num = random.randint(0,20111)
    rand_lst = []

    if request.method == "POST":
        if rand_num:
            # print("-"*50)
            # print("executing if user_id in session")
            rand_lst.append(rand_num)
            rand_recipe = crud.get_recipe_by_id(rand_lst)
            
            return rand_recipe
        else:
            return redirect("/dashboard")
   


@app.route("/questions")
def show_questions():
    """display the questions page"""
    print("*"*50)
    print("routing to questions- show questions page")
    print("*"*50)

    return render_template("questions.html") 



@app.route("/questions_answers", methods=["POST"])
def intake_questions_answers():
    """organizing questions from questions.html info to select recipes from db"""
    print("*"*50)
    print("running questions function")
    print("*"*50)

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

    # get recipe objects 
    recipe_obj = crud.get_recipe_by_id(recipes_ids_for_chosen_prefs)
    # print(f"\n\nrecipes_obj type = {recipe_obj}")

    # recipe_directions = recipe_obj.directions[2:-2]
    # recipe_ingredients = recipe_obj.ingredients_list[2:-2]

    return render_template("display_recipes.html", recipe_obj=recipe_obj)

#would like to show answers to the questionnaire for user to confirm



@app.route("/favorites", methods=["GET", "POST"])
def get_favrecipes():
    """Display favorite recipes/store recipes in db fav_recipes"""
    print("****************")
    print("route to favorites- logic storing chosen recipes, displaying previously stored")
    print("****************")


    if request.method == "POST":
        print("^"*50)
        print("POST request /favorites")
        chosen_recipe_titles = request.form.getlist("chosen-recipe-title")
        print("-"*50)
        print("values (checked boxes) stored in list from html")
        print(chosen_recipe_titles)

        #loop storing chosen recipes in db fav_recipes
        for recipe_title in chosen_recipe_titles:
            # print("*"*20)
            # print("recipe is type:", type(recipe_title))
            # print("starting for loop")
            recipe_obj = crud.get_recipe_by_title(recipe_title)
            print("-"*50)
            print(f"crud recipe obj: {recipe_obj}")
            fav_recipe_info = crud.create_fav_recipes(session["user_id"], recipe_obj.recipe_id)
            # print("-"*50)
            # print(f"fav_recipe_info={fav_recipe_info}")

    print("^"*50)
    print("GET request /favorites")
    favs = crud.get_prev_fav_recipes(session["user_id"])
    rec_ids = []
    for fav in favs:
        rec_ids.append(fav.recipe_id)

    recipe_objs_lst = crud.get_recipe_by_id(rec_ids)
    
    print("-"*50)
    print(f"recipe_objs_lst:{recipe_objs_lst}")

    return render_template("favorites.html", recipe_objs_lst=recipe_objs_lst)



# @app.route("/show_fav_recipes_deets")
# def show_fav_recipe_deets_buttons():
#     """logic for drop down buttons on favorite page"""
#     print("****************")
#     print("route to show_fav_recipes_deets- drop down button logic")
#     print("****************")

   
#     # print("^"*30)
#     # print("POST REQUEST /show_fav_recipe_deets.json")
#     recipe_title_btn = request.args.get("recipe-title") #GETS FIRST STRING IN RECIPE VAL
#     print("-" *50)
#     print(f"request.args:{request.args}")
#     print(f"recipe button:{recipe_title_btn}")

#     recipe_obj = crud.get_recipe_by_title(recipe_title_btn)
#     print("-"*50)
#     print(f"retrieved recipe: {recipe_obj}")

#     rec_obj_ingredients= recipe_obj.ingredients_list
#     rec_obj_instructions= recipe_obj.directions
#     rec_obj_id = recipe_obj.recipe_id
#     rec_obj_title = recipe_obj.recipe_title
#     rec_obj_description = recipe_obj.description
#     rec_obj_protein = recipe_obj.protein
#     rec_obj_calories = recipe_obj.calories
    
#     #storing ANY possible information for use later
#     recipe_info_dict = {
#         "obj_ingredients": rec_obj_ingredients,
#         "instructions": rec_obj_instructions,
#         "id": rec_obj_id,
#         "title": rec_obj_title,
#         "description": rec_obj_description,
#         "protein": rec_obj_protein,
#         "calories": rec_obj_calories,
#         }

#     # session['ingredients']= rec_obj_ingredients
#     # session['instructions']= rec_obj_instructions
    
    
#     return jsonify(recipe_info_dict)




@app.route("/account_info")
def show_user_account():
    """show the user account information"""
    print("*"*50)
    print("routed to /account- displaying user acct")
    print("*"*50)

    session_user = crud.get_user_by_user_id(session["user_id"])

    return render_template("user_acct.html", session_user=session_user)


@app.route("/edit_account", methods=["GET", "POST"])
def edit_user_acct():
    """logic to allow user to edit their information in the db"""
    print("*"*50)
    print("routed to /edit_account")
    print("*"*50)
    if request.method == "POST":
        user_id= session["user_id"]
        user_obj = crud.get_user_by_user_id(user_id)
        fname = user_obj.fname
        new_fname = request.form.get("#test-input")
        update_name = crud.update_user_fname(fname, new_fname)
        print("-"*50)
        print(update_name)
        
        # return render_template("user_acct.html", update_name=update_name)
        return render_template("user_acct.html")

    #route a button to let user change info
    #should I create a new page- would rather use event handler - display a form when button is pushed?
    #function to delete/overwrite info

# @app.route("/test_route")
# def show_test_route():
#     print("*"*50)
#     print("routed to /test_route- displaying test page")
#     print("*"*50)

#     # json_recipe_info_strg = session['json_recipe_info_strg']
#     ingredients = session['ingredients'][2:-2]
#     instructions = session['instructions'][2:-2]

#     print(f"session ingredients: {ingredients}")
#     print(f"session ingredients type:", type(ingredients))

#     print(f"session instructions: {instructions}")
#     print(f"session instructions type:", type(instructions))

#     recipe_dict={
#         'ingredients':ingredients,
#         'instructions': instructions,
#     }
    
#     return jsonify(recipe_dict)


def allowed_file(filename):

    return'.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/image_upload", methods=["GET", "POST"])
def upload_image():
    print("*"*50)
    print("routed to /image_upload- function to upload image")
    print("*"*50)

    # image_file = request.files['img']


    if request.method == 'POST':
        print("^"*50)
        print("POST REQUEST /image_upload")

        if 'file' not in request.files:
            print("-"*50)
            print("if file not in request.files")
            print(f"request.files: {request.files}")
            print(f"request.files type: {type(request.files)}")

            flash('There is no file part')
            return redirect("/account_info")
            return redirect(request.url)

        file = request.files['file']
        print("-"*50)
        print(f"filename: {file.filename}")
        if file.filename == '':
            print("-"*50)
            print("if file.filename")
            print(f"file.filename: {file.filename}")
            print(f"file.filename type: {type(file.filename)}")
            flash('No selected file')
            return redirect("/account_info")
            # return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)