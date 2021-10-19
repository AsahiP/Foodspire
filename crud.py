"""CRUD operations
Create Read Update Delete"""

from flask.templating import render_template
from model import db, User, FavRecipe, Recipe, RecipeCategory, Category, connect_to_db

def create_user(fname, lname, email, username, passwordd):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, username=username, passwordd=passwordd)

    db.session.add(user)
    db.session.commit()

    return user





def create_fav_recipes(user_id, recipe_id):
    """Create and return a favorite recipe"""

    fav_recipe = FavRecipe(user_id=user_id, recipe_id=recipe_id)

    db.session.add(fav_recipe)
    db.session.commit()

    return fav_recipe


def create_recipes(directions, ingredients_list, recipe_title, fat=7, calories=100, description='no description',  protein=10, rating=3, sodium=80): # defaults if NO value
    """creating information for all the recipes"""

    recipe=Recipe(directions=directions, fat=fat, calories=calories, description=description, protein=protein, rating=rating, recipe_title=recipe_title, ingredients_list=ingredients_list, sodium=sodium)

    db.session.add(recipe)
    db.session.commit()

    return recipe

def create_recipe_categories(recipe_id, category_id):
    """create categories of user preferences"""

    recipe_category=RecipeCategory(recipe_id=recipe_id, category_id=category_id)

    db.session.add(recipe_category)
    db.session.commit()

    return recipe_category


def create_categories(category_name):
    """create categories of user preferences"""

    category=Category(category_name=category_name)

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

# category_obj = Category.query.filter_by(category_name=dietary_preference).first()


def get_recipes_by_diet_pref(dietary_preference):
    """return recipes from dietary preferences chosen in questions.html"""

    category_obj = Category.query.filter_by(category_name=dietary_preference).first()
    return category_obj.recipes

def get_recipes_by_meal_time(meal_time):
    """return recipes from meal time preference in questions.html"""

    category_obj = Category.query.filter_by(category_name=meal_time).first()
    return category_obj.recipes

    # return category object

# def get_instructions_by_recipe(category_obj):

#     category_obj.recipes

#     recipe_category_obj = RecipeCategory.query.filter_by(recipe_id=category_obj).first()

#     return recipe_category_obj.directions
    # instructions= category_obj.recipes

# def get_instructions_for_recipe(dietary_preference):
# get instructions to iterate through and display as a list in dispay_recipes
    
#     category_obj = Category.query.filter_by(category_name=dietary_preference).first()
#     return category_obj.directions
    # return category object



if __name__ == '__main__':
    from server import app
    connect_to_db(app)


