"""Server for JavaScript: Project-Web-App.""" 

from flask import Flask, render_template, request, redirect, flash, session, url_for

from model import connect_to_db
import crud

from datetime import datetime

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "askdjaskhaljk"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View hompage."""

    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form["email"]

        if email != None:
            user = crud.get_user_by_email(email)
         
            if request.form["password"] != user.password:

                flash("Invalid credentials")
            else:
                #session["User"] = user.user_id

                flash("You were successfully logged in!")
                return redirect(url_for('view_recipes'))

    return render_template('login.html')

@app.route("/signup", methods=["POST"])
def create_account():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_user_by_email(email)
        if user:
            flash('Cannot create an account with that email. Try again.')
        else:
            crud.create_user(email, password, fname, lname)
            flash('Account created! Please log in.')

    return render_template("signup.html")

@app.route("/recipes", methods=["GET", "POST"])
def view_recipes():
    """View recipes"""

    # recipes = crud.get_recipes()

    return render_template("recipes.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":
        recipe_name = request.form.get("recipe_name")
        date_created = datetime.now()
        prep_time = request.form.get("prep_time")
        cook_time = request.form.get("cook_time")
        num_servings = request.form.get("num_servings")
        ingredients = request.form.get("ingredients")
        directions = request.form.get("directions")
        
        #user = session['User']

        crud.create_recipe(recipe_name, date_created, prep_time, 
            cook_time, num_servings, ingredients, directions)
        flash("Recipe added!")
        
     
    return render_template("recipe_form.html")

@app.route("/logout")
def logout():
    flash("You have successfully logged out!", "info")
    session.pop("user", None)
    return redirect("/login")


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000)
