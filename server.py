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

    login_button = request.args.get("login-button")

    # if login_button == False:
    return render_template("homepage.html")


@app.route("/login", methods=["GET","POST"])
def show_login():
    """Display login/create account page"""
    #validate user and password inputs
    # if login email doesn't exist
    # make a new login

    # user = crud.get_user_by_email(email)
    
    # db_usename = User.query.filter
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db_username = crud.get_username(username)
        db_password = crud.get_password(password)

        # currently testing accessing database before validating password

        if username != db_username:
            flash("This username does not exist")
            # if password == db_password:
            #     return redirect("dashboard.html")
        else:
           redirect("dashboard.html")
    
    return render_template("login.html")


@app.route("/dashboard")
def show_dashboard():
    """Display user dashboard"""

    return render_template("dashboard.html")



@app.route("/favorites")
def show_favrecipes():
    """Display favorite recipes"""

    return render_template("favorites.html")






if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)