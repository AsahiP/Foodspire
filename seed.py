"""seed database. drop db, create db, automatically populate db with data """

import os
import json


import crud 
import model 
import server

os.system('dropdb foodspire')
os.system('createdb foodspire')


model.connect_to_db(server.app)
model.db.create_all()
print("*********")
print("created db from model")


with open('data/five_test_recipes.json') as f:
    recipe_data = json.loads(f.read())
print("*********")
print("opened/read json file")


#categories first
categories_in_db=set()
for recipe in recipe_data:
    categories = recipe["categories"]
    categories_in_db.add(categories)

    db_categories = crud.create_categories(categories)

print("*******************")
print("categories put into db")    


recipes_in_db =[]
for recipe in recipe_data:
    recipe_title, recipe_directions, ingredients_list, fat, calories, protein, rating  = ( #doesn't HAVE to coincide with json data
        recipe['recipe_title'],
        recipe['recipe_directions'],
        recipe['ingredients_list'],
        # recipe['categories'], # delete to normalize data
        recipe['fat'],
        recipe['calories'],
        recipe['protein'],
        recipe['rating'],
    )

    db_recipe = crud.create_recipes(recipe_title, recipe_directions, ingredients_list, fat, calories, protein, rating)

    recipes_in_db.append(db_recipe)
    
    print("*******************")
    print("recipe put into db") #test


recipe_categories = []
# recipe_id_in_db = model.db.query.filter(Recipes.recipe_id)




   # categories first, in a way recipes relies on categories
    # after seed categories, and recipes
    # seed recipe categories 

    #unpack categories, bc it's a list have to iterate through each element. and add to set
    # after set, iterate to create categories 