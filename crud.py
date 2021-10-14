"""CRUD operations
Create Read Update Delete"""

from flask.templating import render_template
from model import db, User, FavRecipes, Recipes, RecipeCategories, Categories, connect_to_db

def create_user(fname, lname, email, username, passwordd):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, username=username, passwordd=passwordd)

    db.session.add(user)
    db.session.commit()

    return user


def create_fav_recipes(user_id, recipe_id):
    """Create and return a favorite recipe"""

    fav_recipe = FavRecipes(user_id=user_id, recipe_id=recipe_id)

    db.session.add(fav_recipe)
    db.session.commit()

    return fav_recipe


def create_recipes(recipe_title, directions, ingredients_list, fat=None, calories=None, protein=None, rating=None):
    """creating information for all the recipes"""

    recipe=Recipes(directions=directions, fat=fat, protein=protein, rating=rating, recipe_title=recipe_title, ingredients_list=ingredients_list)

    db.session.add(recipe)
    db.session.commit()

    return recipe

def create_recipe_categories(recipe_id, category_id):
    """create categories of user preferences"""

    recipe_category=RecipeCategories(recipe_id=recipe_id, category_id=category_id)

    db.session.add(recipe_category)
    db.session.commit()

    return recipe_category

def create_categories(category_name):
    """create categories of user preferences"""

    category=Categories(category_name=category_name)

    db.session.add(category)
    db.session.commit()

    return category



def get_user_by_user_id(user_id):
    """return user_id if it exists"""
    
    return User.query.filter_by(user_id=user_id).first() #this is an object


def get_user_by_username(username):
    """return username if it exists"""
    
    return User.query.filter_by(username=username).first() #this is an object
    # return User.query.filter(User.username==username).first()

def get_user_by_email(email):
    """return email if it exists"""

    return User.query.filter_by(email=email).first()
def get_password(passwordd):
    """return passwordd in database to check if it is correct upon login"""

    return User.query.filter(passwordd=passwordd).first()
    # return User.query.filter_by(User.passwordd==passwordd).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)