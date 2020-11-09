"""CRUD operations."""

from model import db, User, Recipe, Ingredient, Image, connect_to_db


# Functions start here!


if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, fname=fname, lname=lname)

    db.session.add(user)
    db.session.commit()

    return user

def create_recipe(recipe_name, date_created, recipe_type):
    """Create and return a new recipe."""

    recipe = Recipe(recipe_name=recipe_name,
                  date_created=date_created,
                  recipe_type=recipe_type)

    db.session.add(recipe)
    db.session.commit()

    return recipe

def create_ingredient(user, recipe, ing_type, ingredient):
    """Create and return a new ingredient."""

    ingredient= Ingredient(user=user, recipe=recipe, ing_type=ing_type, ingredient=ingredient)

    db.session.add(ingredient)
    db.session.commit()

    return ingredient

def create_image(user, recipe, image_path):
    """Create and return a new image."""

    ingredient= Ingredient(user=user, recipe=recipe, image_path=image_path)

    db.session.add(image)
    db.session.commit()

    return image