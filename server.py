"""Server for JavaScript: Project-Web-App.""" 

from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "askdjaskhaljk"


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        flash("You are not logged in!")
        return redirect("/login")

@app.route("/logout")
def logout():
    flash("You have successfully logged out!", "info")
    session.pop("user", None)
    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
