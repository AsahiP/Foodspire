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


# def create_fav_recipes(user_id, recipe_id): #original
#     """Create and return a favorite recipe"""

#     fav_recipe = FavRecipe(user_id=user_id, recipe_id=recipe_id)

#     db.session.add(fav_recipe)
#     db.session.commit()

#     return fav_recipe

def create_fav_recipes(chosen_recipe): #test
    """Create and return a favorite recipe"""
    print("*"*30)
    print("running crud function create_fav_recipes")
    # qrd_recipe = Recipe.query.filter_by(recipe_title=chosen_recipe).first()
    # qrd_recipe_id = qrd_recipe.recipe_id

    qrd_recipe = Recipe.query.filter_by(recipe_title=chosen_recipe).first()
    # print("*"*30)
    # print("queried recipe")
    # print(type(qrd_recipe))
    # qrd_recipe_id = qrd_recipe.recipe_id
    # print("*"*30)
    # print("queried recipe id")
    # print(type(qrd_recipe_id))
    # qrd_users = qrd_recipe.users
    # print("*"*30)
    # print("queried user")
    # print(type(qrd_users))
    # qrd_user_id = qrd_users.user_id
    # qrd_recipe_user_id = qrd_recipe.user_id

    # fav_recipe = FavRecipe(user_id=qrd_recipe_user_id, recipe_id=qrd_recipe_id)

    # fav_recipe = FavRecipe(recipe_id=qrd_recipe_id)

    # db.session.add(fav_recipe)
    # db.session.commit()
    # return fav_recipe
    return qrd_recipe




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


def get_recipes_by_preference(answers): ## in testing
    """return recipes from meal time preference in questions_test.html"""
    ### testing if can iterate through list of inputs to include all of the inputs###
    ## ended up refractoring the original code
    print("*"*50)
    print(f"\nanswers = {answers}")

    for pref in answers:
        category_obj = Category.query.filter_by(category_name=pref).first()
        if pref==None:
            return Recipe.query.all() #would like to return a different default, so that the queries are only relevant to the chosen preferences
        return category_obj.recipes


def get_recipe_by_title(chosen_recipe_title):
    """retrieve recipe from db by title"""
    
    return Recipe.query.filter_by(recipe_title=chosen_recipe_title).first()


def get_recipes_based_on_prefs(lst_of_prefs):
    #category is the same as user's pref
    category_obj_lst=[] #veg, salad, lunch --> 1,3,7


    for pref in lst_of_prefs:
        category_obj = Category.query.filter(Category.category_name == pref).first()
        category_obj_lst.append(category_obj)

    
    
    lst_of_recipe_category_sets = []
    
    for category in category_obj_lst:
        
        recipe_category_set = set()
        recipe_category_lst = RecipeCategory.query.filter(RecipeCategory.category_id == category.category_id).limit(25).all() #limit for testing
        
        for recipe_category in recipe_category_lst:
            recipe_category_set.add(recipe_category.recipe_id)

        lst_of_recipe_category_sets.append(recipe_category_set)


    final_result = lst_of_recipe_category_sets[0]

    for recipe_category_set in lst_of_recipe_category_sets[1:]:
        print(f"Prev final_result: {final_result}")
        final_result = final_result.intersection(recipe_category_set)
        print(f"New final_result after calling intersection method: {final_result}")


    return final_result # returns set of recipe ids (can query these recipe ids when needing to display on frontend)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)


