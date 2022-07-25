from crypt import methods
from re import A
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


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    print(request.form)
    return redirect('/users')

@app.route("/user/destroy/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.destroy(data)
    return redirect('/users')

@app.route("/user/show/<int:id>")
def show(id):
    data = {
        "id":id
    }
    return render_template("show_user.html", user = User.get_one(data))