"""Server for an Foodspire: an app that generates recipes based on user preference"""


import crud, random, os
from model import User, connect_to_db
from flask import Flask, render_template, request, flash, session, redirect, jsonify, url_for
from flask_login import LoginManager, login_required, login_user,logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

# from wtforms.fields.html5 import URLField

from jinja2 import StrictUndefined
# from werkzeug.utils import secure_filename


app = Flask(__name__)
# app.secret_key = "dev"
app.config['SECRET_KEY'] = "Xyfjghr?CFI'@}%"
app.jinja_env.undefined = StrictUndefined
bcrypt = Bcrypt(app)


UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#for unfinished photo upload
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #to allow image uploads

# app.add_url_rule(
#     "/uploads/<name>", endpoint="download_file", build_only=True
# )

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_business_user(id):
    return User.query.get(id)



####################################################
## CLASSES FOR FLASK LOGIN
##
####################################################



class RegisterForm(FlaskForm):
    """Register user form."""
    
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    
    fname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "First name"})

    lname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Last name"})

    email = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "E-mail address"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Register")
    

    def validate_username(self, username):

        existing_username_obj = User.query.filter_by(username=username.data).first()
        
        if existing_username_obj:
            raise ValidationError(
                "That username already exists. Please choose a different one.")

        


class LoginForm(FlaskForm):

    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "password"})

    submit = SubmitField("Login")



@app.route("/")
def show_homepage():
    """Display the homepage"""


    return render_template("index.html")


####################################################
## LOGIN AND USER REGISTRATION
##
####################################################



@app.route("/login_page")
def show_login_page():
    """Display the login page"""

    form = LoginForm()
    
    return render_template("login.html", form=form)




@app.route("/login_form", methods=['GET', "POST"])
def validate_login():
    """contains logic to validate username/pass"""

    form = LoginForm()


    if form.validate_on_submit():
        user_obj= crud.get_user_by_username(form.username.data)

        if user_obj:
            check = bcrypt.check_password_hash(user_obj.password, form.password.data) 

            

            if bcrypt.check_password_hash(user_obj.password, form.password.data):
                login_user(user_obj, remember=True) #
                session["username"] = form.username.data
                print_session= session["username"]
            
                return redirect('/dashboard')

        if user_obj == None:
            bad_login_dict = {          
                "code": "Username or password incorrect"
                }


            return jsonify(bad_login_dict)

        return redirect('/login_page')




@app.route("/register_user")
def show_user_registration():
    """display the registration page"""
    
    regform = RegisterForm()

    return render_template("registeracct.html", regform=regform)




@app.route("/register_user_form", methods=["POST", "GET"])
@login_required
def handle_user_registration():
    """process user registration inputs"""
    
    regform = RegisterForm()
    email = regform.email.data

    check_user = crud.get_user_by_email(email) 

    if request.method=="POST":

        if check_user:
            flash("Email address already exists to another user.")
            return redirect("/register_user")

        elif regform.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(regform.password.data).decode('utf-8')
            new_user = crud.create_user(regform.fname.data,
                            regform.lname.data,
                            regform.email.data,
                            regform.username.data,
                            regform.password.data)
            session['username']=new_user.username
            
            return redirect(url_for('show_dashboard'))

    return render_template('registeracct.html', regform=regform)




@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """logout user"""

    logout_user()
    return redirect("/")


##############################################
## DASHBOARD/ DASHBOARD PROCESSES
##
##############################################


@app.route("/dashboard")
@login_required
def show_dashboard():
    """Display user dashboard"""

    if "username" in session:
        # session_user= crud.get_user_by_user_id(session["user_id"])
        session_user = session["username"]
        return render_template("dashboard.html", session_user=session_user)

    else: 
        return redirect("/login")

# _user_id


@app.route("/generate_rand_recipe.json")
def generate_rand_recipe_button():
    """process generating recipe from recipe button"""

    rand_num = random.randint(0,20111)
    rand_lst = []

    rand_lst.append(rand_num) 

    rand_recipe = crud.get_recipe_by_id(rand_lst)[0] 
    
    title= rand_recipe.recipe_title
    ingredients= rand_recipe.ingredients_list[2:-2] 
    directions= rand_recipe.directions[2:-2]


    ingredients = ingredients.split('","') #returns a list
    directions = directions.split('","')

    session['rand_recipe'] = rand_recipe.recipe_title
    
    recipe_dict = {
        "title": title,
        "ingredients": ingredients,
        "directions": directions
    }

    return jsonify(recipe_dict)


@app.route("/add_wildcard_to_fav", methods=["POST"])
def add_wildcard_to_fav():

    wildcard_recipe = session['rand_recipe']

    wildcard_recipe_obj= crud.get_recipe_by_title(wildcard_recipe)
    crud.create_fav_recipes(session['_user_id'], wildcard_recipe_obj.recipe_id)

    return redirect("/dashboard")
   

##############################################
## QUESTIONNAIRE/ QUESTIONNAIRE PROCESSES
##
##############################################

@app.route("/questions")
@login_required
def show_questions():
    """display the questions page"""

    return render_template("questions.html") 


@app.route("/recipe_answers", methods=["POST"])
@login_required
def intake_recipe_answers():
    """organizing questions from questions.html info to select recipes from db"""
    

    lst_of_preferences = request.form.getlist("dietary-pref") #test
   
    #get recipe ids exclusively for recipes containing all chosen preferences
    recipes_ids_for_chosen_prefs = crud.get_recipe_ids_based_on_prefs(lst_of_preferences) 
    recipe_objs = crud.get_recipe_by_id(recipes_ids_for_chosen_prefs)
    
    if len(recipes_ids_for_chosen_prefs) == 0:
        flash("There are no recipes based on the choices you made.") 
        flash("try to refine your search")
    

    return render_template("display_recipes.html", recipe_objs=recipe_objs)


##############################################
## FAVORITES/ FAVORITES PROCESSES
##
##############################################


@app.route("/favorites", methods=["GET", "POST"])
@login_required
def get_favrecipes():

    if request.method == "POST":
        chosen_recipe_titles = request.form.getlist("chosen-recipe-title")

        #loop storing chosen recipes in db fav_recipes
        for recipe_title in chosen_recipe_titles:
            recipe_obj = crud.get_recipe_by_title(recipe_title)
            crud.create_fav_recipes(session["_user_id"], recipe_obj.recipe_id)

    favs = crud.get_prev_fav_recipes(session["_user_id"])
    rec_ids = []
    for fav in favs:
        rec_ids.append(fav.recipe_id)

    recipe_objs_lst = crud.get_recipe_by_id(rec_ids)
  
    return render_template("favorites.html", recipe_objs_lst=recipe_objs_lst)



@app.route("/delete_fav_recipe", methods=["POST"])
def delete_fav_recipe():
    """Delete a recipe from the saved favorites"""


    recipes_to_delete = request.form.getlist("delete-fav-recipe")

    for recipe_title in recipes_to_delete:
        crud.delete_fav_recipe(recipe_title) 
    return redirect("/favorites")
    

##############################################
## USER ACCOUNT/ USER ACCOUNT PROCESSES
##
##############################################


@app.route("/account_info")
@login_required
def show_user_account():
    """show the user account information"""

    session_user_obj = crud.get_user_by_user_id(session["_user_id"])

    return render_template("user_acct.html", session_user_obj=session_user_obj)



@app.route("/edit_account", methods=["POST"])
@login_required
def edit_user_acct():
    """logic to allow user to edit their information in the db"""

    session_user_obj = crud.get_user_by_user_id(session["_user_id"])


    if request.method == "POST":
        
        new_fname = request.form.get('fname_input')
        new_lname = request.form.get("lname_input")
        new_email = request.form.get("email_input")
        new_password = request.form.get("password_input")

        if new_fname!=None:
            if len(new_fname) > 20:
                result_code = "ERROR"
                result_text = "Max input is 20 letters. Enter a name with less than 20 letters"
            elif len(new_fname) < 1:
                result_code = "ERROR"
                result_text = "You did not enter a name"
            else:
                crud.update_user_fname(session_user_obj.user_id, new_fname)                
                result_code = "Success!"
                result_text = f"Your first name has been changed to {new_fname}"
    
        if new_lname!=None:
            if len(new_lname) > 20:
                result_code = "ERROR"
                result_text = "Max input is 20 letters. Enter a name with less than 20 letters"
            elif len(new_lname) < 1:
                result_code = "ERROR"
                result_text = "You did not enter a name"
            else:
                crud.update_user_lname(session_user_obj.user_id, new_lname)                
                result_code = "Success!"
                result_text = f"Your last name has been changed to {new_lname}"
                
        
        
        if new_email!=None:
            if len(new_email) > 30:
                result_code = "ERROR"
                result_text = "Max input is 30 characters. Enter an e-mail address with less than 30 characters"
            elif " " in new_email:
                result_code = "ERROR"
                result_text= "There cannot be any spaces in your e-mail"
            elif len(new_email) < 1:
                result_code = "ERROR"
                result_text = "You did not enter an e-mail address"
            else:
                crud.update_user_email(session_user_obj.user_id, new_email)                
                result_code = "Success!"
                result_text = f"Your e-mail address has been changed to {new_email}"
                
                
        

        if new_password!=None:
            if len(new_password) > 20:
                result_code = "ERROR"
                result_text = "Max input is 20 characters. Enter a password with less than 20 letters"
            elif len(new_password) < 1:
                result_code = "ERROR"
                result_text = "You did not enter anything"
            else:
                crud.update_user_password(session_user_obj.user_id, new_password)                
                result_code = "Success!"
                result_text = f"Your password has been sucessfully changed"
    


    return jsonify({'code': result_code, 'msg': result_text})
  

####UPLOAD PHOTO: UNFINISHED

# def allowed_file(filename):

#     return'.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# @app.route("/image_upload", methods=["GET", "POST"])
# def upload_image():
#     ("+"*70)
#     print("routed to /image_upload- function to upload image")
#     ("+"*70)

#     # image_file = request.files['img']


#     if request.method == 'POST':
#         print("^"*50)
#         print("POST REQUEST /image_upload")

#         if 'file' not in request.files:
#             print("-"*50)
#             print("if file not in request.files")
#             print(f"request.files: {request.files}")
#             print(f"request.files type: {type(request.files)}")

#             flash('There is no file part')
#             return redirect("/account_info")
#             return redirect(request.url)

#         file = request.files['file']
#         print("-"*50)
#         print(f"filename: {file.filename}")
#         if file.filename == '':
#             print("-"*50)
#             print("if file.filename")
#             print(f"file.filename: {file.filename}")
#             print(f"file.filename type: {type(file.filename)}")
#             flash('No selected file')
#             return redirect("/account_info")
#             # return redirect(request.url)

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD FOLDER'], filename))
#             return redirect(url_for('download_file', name=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)