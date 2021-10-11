"""drop db, create db, automatically populate db with data """

import os
import json


import crud
import model
import server

os.system('dropdb foodspire')
os.system('createdb foodspire')


model.connect_to_db(server.app)
model.db.create_all()


with open('data/five_test_recipes.json') as f:
    recipe_data = json.loads(f.read())

recipes_in_db =[]
for recipe in recipe_data:
    recipe_title, ingredients_list, directions, categories = {
        recipe['recipe_title'],
        recipe['ingredients_list'],
        recipe['recipe_directions'],
        recipe['categories']
    }

    db_recipe = crud.create_recipes(recipe_title, directions, ingredients_list, categories)
    recipes_in_db.append(db_recipe)