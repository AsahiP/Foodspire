"""drop db, create db, automatically populate db with data """

import os
import json

from random import choice, randint
from datetime import datetime

import crud
import model
import server

def create_user(email, password):
    """Create and return a new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_client(fname, lname, company_name = None, email=None, address, phone_number, bus_phone_number=None):

    client = Clients(fname=fname, lname=lname, company_name=company_name, email=email, address=address, phone_number=phone_number, bus_phone_number=bus_phone_number)

    db.session.add(client)
    db.session.commit()

    return client

def create_orders(client_id, user_id, date_submitted, due_date, total_cost):

    order = Orders(client_id=client_id, user_id=user_id, date_submitted=date_submitted, due_date=due_date, total_cost=total_cost)

    db.session.add(order)
    db.session.commit()

    return order

def create_donut_orders(order_id, donut_id, donut_amt, cost_per, total_per):

    donut_orders = DonutOrders(order_id=order_id, donut_id=donut_id, unit_amt=donut_amt, cost_per=cost_per, total_per=total_per)

    db.session.add(donut_orders)
    db.session.commit()

    return donut_orders


def create_recipes(bake_time, bake_temp, bake_procedure):

    recipes = Recipes(bake_time=bake_time, bake_temp=bake_temp, bake_procedure=bake_procedure)

    return recipes


def create_recipe_ingredients(recipe_id, ingredient_id):

    recipe_ingredients=RecipesIngredients(recipe_id=recipe_id, ingredient_id=ingredient_id)



def create_ingredients(ingredient_name)

    ingredients = Ingredients(ingredient_name)