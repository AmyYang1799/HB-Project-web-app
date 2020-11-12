"""Server for JavaScript: Project-Web-App.""" 

from flask import Flask, render_template, request, redirect, flash, session, url_for

from model import connect_to_db
import crud

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
        if request.form["email"] != "admin" or \
            request.form["password"] != "secretpw":
            flash("Invalid credentials")
        else:
            flash("You were successfully logged in!")
            return redirect(url_for('view_recipes'))

    return render_template('login.html')

@app.route("/signup")
def create_account():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_user_by_email(email)
        if user:
            flash('Cannot create an account with that email. Try again.')
        else:
            crud.create_user(email, password)
            flash('Account created! Please log in.')

    return render_template("signup.html")

@app.route("/recipes")
def view_recipes():
    """View recipes"""

    # recipes = crud.get_recipes()

    return render_template("recipes.html")


@app.route("/add_recipe")
def add_recipe():
    return render_template("recipe_form.html")

@app.route('/users')
def register_user():
    """Create a new user."""



    return redirect('/')

@app.route("/logout")
def logout():
    flash("You have successfully logged out!", "info")
    session.pop("user", None)
    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
