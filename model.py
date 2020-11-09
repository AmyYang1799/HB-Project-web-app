from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

from sqlfaker.database import Database

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(30), nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    
    

    def __repr__(self):
        return f'<User user_id={ self.user_id } email={ self.email } password={ self.password } fname={self.fname} fname={self.lname}>'
    

class Recipe(db.Model):
    """A recipe."""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    recipe_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return f'<Recipe recipe_id={ self.recipe_id } recipe_name={self.recipe_name} date_created={self.date_created} recipe_type={ self.recipe_type } user_id={self.user_id}>'


class Ingredient(db.Model):
    """Ingredients in a recipe."""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ing_type = db.Column(db.String(30), nullable=False)
    ingredient = db.Column(db.String(50), nullable=False)
    # ing_meas = db.Column(db.float, nullable=False)

    def __repr__(self):
        return f'<Ingredient recipe_id={ self.recipe_id } user_id={self.user_id} ing_type={self.ing_type} ingredient={self.ingredient} ing_meas={ self.ing_meas }>'
    

class Image(db.Model):
    """Images uploaded by user."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))
    image_path = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'<Image image_id={ self.image_id } uploaded_by={self.user_id} recipe_id={self.recipe_id} image_path={self.image_path}>'




def connect_to_db(flask_app, db_uri='postgresql:///recipes', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)



#

# # add database
# my_db = Database(db_name="recipesdb")

# # add tables
# my_db.add_table(table_name="users", n_rows=500)
# my_db.add_table(table_name="recipes", n_rows=500)
# my_db.add_table(table_name="images", n_rows=500)
# my_db.add_table(table_name="ingredients", n_rows=500)

# # add columns to users table
# my_db.tables["users"].add_primary_key(column_name="user_id")
# my_db.tables["users"].add_column(column_name="email", data_type="varchar(50)", data_target="email")
# my_db.tables["users"].add_column(column_name="password", data_type="varchar(30)", data_target="password")
# my_db.tables["users"].add_column(column_name="fname", data_type="varchar(30)", data_target="fname")
# my_db.tables["users"].add_column(column_name="lname", data_type="varchar(30)", data_target="lname")


# # add columns to recipes table
# my_db.tables["recipes"].add_primary_key(column_name="recipe_id")
# my_db.tables["recipes"].add_column(column_name="recipe_name", data_type="varchar(100)", data_target="recipe_name")
# my_db.tables["recipes"].add_column(column_name="date_created", data_type="date", data_target="date_created")
# my_db.tables["recipes"].add_column(column_name="recipe_type", data_type="varchar(50)", data_target="recipe_type")
# my_db.tables["recipes"].add_foreign_key(column_name="user_id", target_table="users", target_column="user_id")


# # add columns to ingredints table
# my_db.tables["ingredients"].add_primary_key(column_name="ingredient_id")
# my_db.tables["ingredients"].add_column(column_name="ingredient", data_type="varchar(50)", data_target="ingredient")
# my_db.tables["ingredients"].add_column(column_name="ing_type", data_type="varchar(30)", data_target="ing_type")
# my_db.tables["ingredients"].add_column(column_name="ing_meas", data_type="float", data_target="ing_meas")
# my_db.tables["ingredients"].add_foreign_key(column_name="user_id", target_table="users", target_column="user_id")
# my_db.tables["ingredients"].add_foreign_key(column_name="recipe_id", target_table="recipes", target_column="recipe_id")

# # add columns to images table
# my_db.tables["images"].add_primary_key(column_name="image_id")
# my_db.tables["images"].add_column(column_name="image_path", data_type="varchar", data_target="image_path")
# my_db.tables["images"].add_foreign_key(column_name="uploaded_by", target_table="users", target_column="user_id")
# my_db.tables["images"].add_foreign_key(column_name="recipe_id", target_table="recipes", target_column="recipe_id")


# my_db.generate_data()
# my_db.export_sql("test.sql")