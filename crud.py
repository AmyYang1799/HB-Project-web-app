"""CRUD operations."""

from model import db, User, Recipe, Image, connect_to_db


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

def create_recipe(recipe_name, date_created, prep_time, cook_time, num_servings, ingredients, directions, user_id):
    """Create and return a new recipe."""

    print(recipe_name)
    print(date_created)
    print(prep_time)
    print(cook_time)
    print(num_servings)
    print(ingredients)
    print(directions)
    print(user_id)

    recipe = Recipe(recipe_name=recipe_name,
                  date_created=date_created,
                  prep_time=prep_time,
                  cook_time=cook_time,
                  num_servings=num_servings,
                  ingredients=ingredients,
                  directions=directions,
                  user_id=user_id
                  )

    db.session.add(recipe)
    db.session.commit()

    return recipe

def get_recipes():
    """Return all recipies."""

    return Recipe.query.all()

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

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_recipe_by_id(recipe_id):
    """Return a recipe by primary key."""

    return Recipe.query.get(recipe_id)

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def add_saved_recipe(user_id, recipe_id):
    """Add and return a saved recipe."""

    user = User.query.get(user_id)

    if user.saved_recipes is None:
        user.saved_recipes = recipe_id
    else:
        user.saved_recipes = user.saved_recipes + "," + recipe_id

    db.session.commit()

    return Recipe.query.get(recipe_id)