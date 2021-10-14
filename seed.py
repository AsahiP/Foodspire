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
    for category in categories:
        categories_in_db.add(category)


categories_dict = {} #KEY: cateogry_name VALUE: category_id

for category in categories_in_db:
    category_obj = crud.create_categories(category) #this funct returning an object, utilizing object by assigning to var
    categories_dict[category_obj.category_name]=category_obj.category_id
# print("!!!!!!!!!!!!!!!!")
# print(categories_dict)

recipes_in_db =[]
#unpacking
for recipe in recipe_data: # 3 recipes, but each recipe has its own list of categories
    title, directions, ingredients, fat, calories, desc, protein, rating, sodium  = ( #doesn't HAVE to coincide with json data
        recipe['title'], #accessing keys in --jason--, not model
        recipe['directions'],
        recipe['ingredients'],
        recipe['fat'],
        recipe['calories'],
        recipe['desc'],
        recipe['protein'],
        recipe['rating'],
        recipe['sodium']
    )
    # recipe obj
    db_recipe = crud.create_recipes(directions, ingredients, title, fat, calories, desc, protein, rating, sodium) #exact order for crud function params
    recipes_in_db.append(db_recipe)

    category_lst = recipe['categories']    #example: ["Cheese", "Dairy", "Pasta"]
        #key to access dict
    for category in category_lst:
        category_id = categories_dict[category]
        crud.create_recipe_categories(db_recipe.recipe_id, category_id)
        #
    
print("*******************")
print("recipe put into db") #test









   # categories first, in a way recipes relies on categories
    # after seed categories, and recipes
    # seed recipe categories 

    #unpack categories, bc it's a list have to iterate through each element. and add to set
    # after set, iterate to create categories 