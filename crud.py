"""CRUD operations
Create Read Update Delete"""

from model import db, User, FavRecipes, Recipes, RecipeCategories, Categories, connect_to_db

def create_user(fname, lname, email, username, password):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_fav_recipes(user_id, recipe_id):
    """Create and return a favorite recipe"""

    fav_recipe = FavRecipes(user_id=user_id, recipe_id=recipe_id)

    db.session.add(fav_recipe)
    db.session.commit()

    return fav_recipe


def create_recipes(directions, fat=None, categories, calories=None, protein=None, rating=None, recipe_title, ingredients_list):
    """creating information for all the recipes"""

    recipe=Recipes(directions=directions, fat=fat, categories=categories, protein=protein, rating=rating, recipe_title=recipe_title, ingredients_list=ingredients_list)

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
