"""CRUD operations."""

from model import db, User, Recipe, Image, connect_to_db, Favorite


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

def create_favorite(user_id, recipe_id):
    """Create a fav recipe."""

    print("???????????????????????????????????????")
    print(Favorite.query.all())
    print(recipe_id)

    user = User.query.get(user_id)
    print(user)
    print(user_id)

    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)

    db.session.add(favorite)

    db.session.commit()

    return favorite


def get_user_fav(user_id):

    #fav = Favorite.query.filter_by(user_id=user_id).all().join()

    #fav = db.session.query(Recipe).filter(Favorite.user_id==user_id).all()

    # fav = db.session.query(Favorite, Recipe,).filter(Favorite.user_id==user_id).filter(Recipe.recipe_id==Favorite.recipe_id).all()

    fav = db.session.query(Recipe.recipe_id, Recipe.recipe_name,).filter(Favorite.user_id==user_id).filter(Recipe.recipe_id==Favorite.recipe_id).all()
    return fav 

def get_fav_by_id(user_id, recipe_id):
    """Return a favorite recipe by recipe id."""

    return Favorite.query.filter_by(recipe_id=recipe_id, user_id=user_id).all()