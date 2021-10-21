"""foodspire db tables"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Table for a user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    passwordd = db.Column(db.String(20), nullable=False)

    recipes = db.relationship('Recipe', secondary='fav_recipes', backref='users')


    def __repr__(self):
        return f'<User user_id={self.user_id} user_name={self.username}>' 



class FavRecipe(db.Model):
    """Table for orders"""

    __tablename__ = "fav_recipes"

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    
    # user = db.relationship('Users', back_populates="fav_recipes")
    # recipe = db.relationship('Recipes', back_populates='fav_recipes')
    
    def __repr__(self):
        return f'<FavRecipe fav_id={self.fav_id} user_id={self.user_id} recipe_id={self.recipe_id}>' 



class Recipe(db.Model):
    """Recipe details"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    directions = db.Column(db.String, nullable=False)
    fat = db.Column(db.Integer)
    # categories = db.Column(db.String, nullable=False) #removing to normalize data
    calories = db.Column(db.Integer)
    description = db.Column(db.String)
    protein = db.Column(db.Integer)
    rating = db.Column(db.Float)
    recipe_title = db.Column(db.String, nullable=False)
    ingredients_list = db.Column(db.String, nullable=False)
    sodium = db.Column(db.Integer)
    
    categories = db.relationship("Category", secondary="recipe_categories", backref="recipes")

    # users = list of users who favorited this recipe 

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} recipe_title={self.recipe_title}>' 


class RecipeCategory(db.Model):

    __tablename__ = "recipe_categories"#assoc table

    recipe_category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id')) 
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))


    def __repr__(self):
        return f'<RecipeCategory recipe_category_id={self.recipe_category_id} recipe_id={self.recipe_id} category_id={self.category_id}>'


class Category(db.Model):

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String, nullable=False)
    #recipes is the relationship to access recipes table
    ### I CAN GET RECIPE FROM recipes BECAUSE OF BACKREF
    def __repr__(self):
        return f'<Categories category_id={self.category_id} category_name={self.category_name}>'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///foodspire" #configure app: point to db
    app.config["SQLALCHEMY_ECHO"] = False # lets you know what sequel is running behind scenes
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # omit warning, depricating soon
    db.app = app # start/initialize app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    from flask import Flask
    # from server import app
    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()

