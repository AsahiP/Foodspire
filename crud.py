"""CRUD operations
Create Read Update Delete"""

# from flask.templating import render_template
from model import db, User, FavRecipe, Recipe, RecipeCategory, Category, connect_to_db


"""
FUNCTIONS IN FILE, IN ORDER OF APPEARANCE:

create_user(fname, lname, email, username, passwordd):
    Create and return a new user


create_fav_recipes(user_id, recipe_id): 
    Create and return a favorite recipe (to store in db fav_recipes table)


create_fav_recipes(user_id, recipe_id): 
    Create and return a favorite recipe (to store in db fav_recipes table)


create_recipes(directions, ingredients_list, recipe_title, fat=7, calories=100, description='no description',  protein=10, rating=3, sodium=80): # defaults if NO value
    creating information for all the recipes


create_recipe_categories(recipe_id, category_id):
    create categories of user preferences

create_categories(category_name):
    create categories of user preferences


get_user_by_user_id(user_id):
    return user_id if it exists


get_user_by_username(username):
    return username if it exists


get_user_by_email(email):
    return email if it exists

get_password(passwordd):
    return passwordd in database to check if it is correct upon login


get_recipe_by_title(chosen_recipe_title):
    retrieve recipe from db by title
    
    return Recipe.query.filter_by(recipe_title=chosen_recipe_title).first()


get_recipe_ids_based_on_prefs(lst_of_prefs):
    get recipes exclusively from categories from recipes passed in to parameter


get_recipe_by_id(wanted_ids):
    get recipe from db.recipes via db.recipe_categories


----------------------------------------------------------------------------------
ADDITIONAL FUNCTIONS IN secret/deleted_code.py:

get_recipe_ids_based_on_prefs(lst_of_prefs)
same as function here, just lousy with print statements to understand logic

get_recipes_by_preference(answers):
original attempt at returning recipes from form answers. keep for testing

"""


def create_user(fname, lname, email, username, passwordd):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, username=username, passwordd=passwordd)

    db.session.add(user)
    db.session.commit()

    return user



def create_fav_recipes(user_id, recipe_id): 
    """Create and return a favorite recipe (to store in db fav_recipes table)"""

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



def get_recipe_by_title(chosen_recipe_title):
    """retrieve recipe from db by title"""
    
    return Recipe.query.filter_by(recipe_title=chosen_recipe_title).first()


def get_recipe_ids_based_on_prefs(lst_of_prefs):
    """get recipes exclusively from categories from recipes passed in to parameter"""
    print("*"*30)
    print("\nexecuting get_recipe_ids_based_on_prefs")
    #category is the same as user's pref
    category_obj_lst=[] #veg, salad, lunch --> 1,3,7

    for pref in lst_of_prefs:
        category_obj = Category.query.filter(Category.category_name == pref).first()
        category_obj_lst.append(category_obj)
    
    lst_of_recipe_category_sets = []
    
    for category in category_obj_lst:
        recipe_category_set = set()
        recipe_category_lst = RecipeCategory.query.filter(RecipeCategory.category_id == category.category_id).all() #limit for testing
        
        for recipe_category in recipe_category_lst:
            recipe_category_set.add(recipe_category.recipe_id)
        
        lst_of_recipe_category_sets.append(recipe_category_set)


    final_result = lst_of_recipe_category_sets[0]


    for recipe_category_set in lst_of_recipe_category_sets[1:]:
        final_result = final_result.intersection(recipe_category_set)


  
    return final_result # returns set of recipe ids (can query these recipe ids when needing to display on frontend)


def get_recipe_by_id(wanted_ids):
    """get recipe from db.recipes via db.recipe_categories"""
    print("*"*30)
    print("executing get_recipe_by_id")

    qrd_recipes_from_id_lst = []
    for id in wanted_ids:
        qrd_recipes_from_id = Recipe.query.filter_by(recipe_id=id).first()
        # print("achieved qrd_recipes_from_id")
        # print(f"\nqrd_recipes_from_id:   {qrd_recipes_from_id}") 
        qrd_recipes_from_id_lst.append(qrd_recipes_from_id)

    return qrd_recipes_from_id_lst




if __name__ == '__main__':
    from server import app
    connect_to_db(app)




