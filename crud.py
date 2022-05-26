"""CRUD operations
Create Read Update Delete"""

# from flask.templating import render_template
from model import db, User, FavRecipe, Recipe, RecipeCategory, Category, connect_to_db
from server import RegisterForm
import bcrypt

from flask import flash

""""
Categories in order:

Create
Get
Update
"""


#################################################
##CREATE
##
#################################################

def create_user(fname, lname, email, username, password):
    """Create, add, & return new user."""
    print("\n","%"*50)
    print("executing %%create_user")
    
    password_code = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    password = password_code.decode('utf-8')
    
    user = User(fname=fname, lname=lname, email=email, username=username, password=password)

    
    db.session.add(user)
    db.session.commit()

    return user



def create_fav_recipes(user_id, recipe_id): 
    """Create and return a favorite recipe (to store in db fav_recipes table)"""
    """create categories of user preferences"""
    print("\n","%"*50)
    print("executing %%create_fav_recipes")

    fav_recipe = FavRecipe(user_id=user_id, recipe_id=recipe_id)

    db.session.add(fav_recipe)
    db.session.commit()

    return fav_recipe



def create_recipes(directions, ingredients_list, recipe_title, fat=7, calories=100, description='no description',  protein=10, rating=3, sodium=80): # defaults if NO value
    """creating information for all the recipes"""
    print("\n","%"*50)
    print("executing %%create_recipes")

    recipe=Recipe(directions=directions, fat=fat, calories=calories, description=description, protein=protein, rating=rating, recipe_title=recipe_title, ingredients_list=ingredients_list, sodium=sodium)

    db.session.add(recipe)
    db.session.commit()

    return recipe



def create_recipe_categories(recipe_id, category_id):
    """create categories of user preferences"""
    print("\n","%"*50)
    print("executing %%create_recipe_categories")

    recipe_category=RecipeCategory(recipe_id=recipe_id, category_id=category_id)

    db.session.add(recipe_category)
    db.session.commit()

    return recipe_category




def create_categories(category_name):
    """create categories of user preferences"""

    print("\n","%"*50)
    print("executing %%create_categories")

    category=Category(category_name=category_name)

    db.session.add(category)
    db.session.commit()

    return category






#################################################
##GET
##
#################################################




def get_prev_fav_recipes(user_id):
    """Get previous recipes user has selected"""
    print("\n","%"*50)
    print("executing %%get_prev_fav_recipes")

    # return FavRecipe.query.filter(FavRecipe.user_id==user_id).all()
    
    return User.query.filter(User.user_id==user_id).one().recipes



def get_user_by_user_id(user_id):
    """return user_id if it exists"""
    print("\n","%"*50)
    print("executing %%get_user_by_user_id")
    
    return User.query.filter_by(user_id=user_id).first() #this is an object



def get_user_by_username(username):
    """return username if it exists"""
    print("\n","%"*50)
    print("executing %%get_user_by_username")
    
    return User.query.filter_by(username=username).first() #this is an object
    # return User.query.filter(User.username==username).first()



def get_user_by_email(email):
    """return email if it exists"""
    print("\n","%"*50)
    print("executing %%get_user_by_email")

    return User.query.filter_by(email=email).first()



def get_password(password):
    """return password in database to check if it is correct upon login"""

    return User.query.filter(password=password).first()
    # return User.query.filter_by(User.password==password).first()



def get_recipe_by_title(chosen_recipe_title):
    """retrieve recipe from db by title"""
    print("\n","%"*50)
    print("executing get_recipe_by_title")
    return Recipe.query.filter_by(recipe_title=chosen_recipe_title).first()


def get_recipe_ids_based_on_prefs(lst_of_prefs):
    """get recipes exclusively from categories from recipes passed in to parameter"""
    print("\n","%"*50)
    print("executing get_recipe_ids_based_on_prefs")
    #category is the same as user's pref
    category_obj_lst=[] #veg, salad, lunch --> 1,3,7

    for pref in lst_of_prefs:
        category_obj = Category.query.filter(Category.category_name == pref).first()
        category_obj_lst.append(category_obj)
    
    lst_of_recipe_category_sets = []
    final_result = set()

    for category in category_obj_lst:
        if category != None: # conditional in case nothing is returned
            recipe_category_set = set()
            recipe_category_lst = RecipeCategory.query.filter(RecipeCategory.category_id == category.category_id).all() #limit for testing

            for recipe_category in recipe_category_lst:
                recipe_category_set.add(recipe_category.recipe_id) 
                
            lst_of_recipe_category_sets.append(recipe_category_set)
        
        else:
            lst_of_recipe_category_sets.append(set())# avoids None value
    
    if lst_of_recipe_category_sets != []:
        final_result = lst_of_recipe_category_sets[0]

        for recipe_category_set in lst_of_recipe_category_sets[1:]:
            final_result = final_result.intersection(recipe_category_set)

    return final_result # returns set of recipe ids (can query these recipe ids when needing to display on frontend)
    


def get_recipe_by_id(wanted_ids):
    """get recipe from db.recipes via db.recipe_categories"""
    print("\n","%"*50)
    print("executing get_recipe_by_id")


    qrd_recipes_from_id_lst = []
    print("1818181811818181818181181818118181811818")
    for id in list(wanted_ids):
        qrd_recipes_from_id = Recipe.query.filter_by(recipe_id=id).first()
        print("achieved qrd_recipes_from_id")
        print(f"\nqrd_recipes_from_id:   {qrd_recipes_from_id}") 
        qrd_recipes_from_id_lst.append(qrd_recipes_from_id)
    print("\n","%"*50)
    print("get_recipe_by_id return statement")
    print(qrd_recipes_from_id_lst)
    return qrd_recipes_from_id_lst


#################################################
##CHANGE DB
##
#################################################


def update_user_fname(user_id, changed_fname):
    """change user fname in db, check to see if name is <10 chars"""
    print("\n","%"*50)
    print("executing %%update_user_fname")

    print(f"%%this is the changed_name: {changed_fname}")
    user_obj = get_user_by_user_id(user_id)
    print(f"%%this is the user_obj: {user_obj}")

    user_obj.fname = changed_fname
    updated_fname = user_obj.fname
    print(f"%%updated_fname: {updated_fname}")

    db.session.commit()
    return updated_fname


def update_user_lname(user_id, changed_lname):
    """pass in user information to change in db"""
    print("\n","%"*50)
    print("executing %%update_user_lname")

    user_obj = get_user_by_user_id(user_id)
    print(f"%%this is the user_obj: {user_obj}")
    user_obj.lname = changed_lname

    db.session.commit()


def update_user_email(user_id, changed_email):
    """pass in user information to change in db"""
    print("\n","%"*50)
    print("executing %%update_user_email")

    user_obj = get_user_by_user_id(user_id)
    print(f"%%this is the user_obj: {user_obj}")
    user_obj.email = changed_email

    db.session.commit()
    

def update_user_password(user_id, changed_password):
    """pass in user information to change in db"""
    print("\n","%"*50)
    print("executing %%update_user_password")

    password_code = bcrypt.hashpw(changed_password.encode('utf-8'), bcrypt.gensalt())

    new_password = password_code.decode('utf-8')

    user_obj = get_user_by_user_id(user_id)
    # print(f"%%this is the user_obj: {user_obj}")


    user_obj.password = new_password

    db.session.commit()


def delete_fav_recipe(fav_recipe_title):
    """Delete fav recipe"""
    print("\n","%"*50)
    print("executing %%delete_fav_recipe")

    # fav_recipe = FavRecipe.query.get(fav_recipe_id)
    recipe_obj = get_recipe_by_title(fav_recipe_title)
    print(recipe_obj)
    recipe_saved_to_favs = FavRecipe.query.filter(FavRecipe.recipe_id==recipe_obj.recipe_id).all()
    # print(recipe_saved_to_favs)
    # print(recipe_saved_to_favs.recipe_id)
    
    for recipe in recipe_saved_to_favs:
        db.session.delete(recipe)
        db.session.commit()

    pass




if __name__ == '__main__':
    from server import app
    connect_to_db(app)




