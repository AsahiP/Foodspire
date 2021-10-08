"""foodspire db tables"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Table for a user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), Nullable=False)
    lname = db.Column(db.String(20), Nullable=False)
    username = db.Column(db.String(15), unique = True, Nullable=False)
    email = db.Column(db.String(30), unique = True, Nullable = False)
    password = db.Column(db.String(12), Nullable=False)


    def __reper__(self):
        return f'<User user_id={self.user_id} user_name={self.user_name} email={self.email}>' 



class FavRecipes(db.Model):
    """Table for orders"""

    __tablename__ = "fav_recipes"

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    
    user = db.relationship('Users', back_populates="fav_recipes")
    recipe = db.relationship('Recipes', back_ref='fav_recipes')
    
    def __reper__(self):
        return f'<FavRecipes fav_id={self.fav_id} user_id={self.user_id} recipe_id={self.recipe_id}>' 


class Recipes(db.Model):
    """Recipe details"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    directions = db.Column(db.String, Nullable = False)
    fat = db.Column(db.Integer)
    categories = db.Column(db.String)
    calories = db.Column(db.Integer)
    description = db.Column(db.String)
    protein = db.Column(db.Integer)
    rating = db.Column(db.float)
    recipe_title = db.Column(db.String, Nullable = False)
    ingredients_list = db.Column(db.String, Nullable = False)
    sodium = db.Column(db.Integer)


    def __reper__(self):
        return f'<Recipes recipe_id={self.recipe_id} recipe_title={self.recipe_title} ingredients_list={self.ingredients_list}>' 


class RecipeCategories(db.Model):

    __tablename__ = "recipe_categories"

    recipe_category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))

    recipe = db.relationship('Recipes', back_ref='recipe_categories')
    category = db.relationship('Categories', back_ref='recipe_categories')


    def __reper__(self):
        return f'<RecipeCategories recipe_category_id={self.recipe_category_id} recipe_id={self.recipe_id} category_id={self.category_id}>'


class Categories(db.Model):

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String(15), Nullable=False)

    def __reper__(self):
        return f'<Categories category_id={self.category_id} category_name={self.category_name}>'


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///foodspire"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)

