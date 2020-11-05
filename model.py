from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime



class User(db.model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String(30), nullable=false)
    lname = db.Column(db.String(30) nullable=false)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<User user_id={ self.user_id } fname={self.fname} fname={self.lname} email={ self.email }>'
    

class Recipe(db.model):
    """A recipe."""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=false)
    date_created = db.Column(db.Datetime, nullable=false)
    recipe_type = db.Column(db.String(50), nullable=false)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<Recipe recipe_id={ self.recipe_id } recipe_name={self.recipe_name} date_created={self.date_created} recipe_type={ self.recipe_type } user_id={self.user_id}>'


class Ingredient(db.model):
    """Ingredients in a recipe."""

    __tablename__ = "ingredients"

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ing_type = db.Column(db.String(30), nullable=false)
    ingredient = db.Column(db.String(50), nullable=false)
    ing_meas = db.Column(db.float, nullable=false)

     def __repr__(self):
        return f'<Ingredient recipe_id={ self.recipe_id } user_id={self.user_id} ing_type={self.ing_type} ingredient={self.ingredient} ing_meas={ self.ing_meas }>'
    

class Image(db.model):
    """Images uploaded by user."""

    image_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    image_path = db.Column(db.String(255), nullable = false)

    def __repr__(self):
        return f'<Image image_id={ self.image_id } uploaded_by={self.user_id} recipe_id={self.recipe_id} image_path={self.image_path}>'




    # def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo = False
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)