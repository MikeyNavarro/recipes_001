from crypt import methods
from flask_app import app, render_template, redirect, request, bcrypt, session, flash
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def users():
    return render_template("users.html", users=User.get_all())


@app.route("/user/create")
def create_user():
    return render_template("new_user.html")


@app.route("/user/db/create", methods=["POST"])
def save():
    users = User.save(request.form)
    return redirect("/users")
