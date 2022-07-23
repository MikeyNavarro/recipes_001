from flask_app import app, render_template, redirect, request, bcrypt, session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods = ['post'])
def register_user():
    print(request.form)
    # validate user info from form
    if not User.validate_user(request.form):
        return redirect('/')
    # hash password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # create data dict to change password value to the hash created above.
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password":pw_hash
    }
    # save user to database
    user_id = User.save(data)
    # log user in
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    # redirect to app page
    return redirect("/recipes")

@app.route('/users/login', methods = ['post'])
def login_user():
    print(request.form)
    # query database for user email from form
    data = {'email': request.form['log_email']}
    user_in_db = User.get_by_email(data)
    # use query to redirect if not found
    if not user_in_db:
        flash("invalid credentials")
        return redirect('/')
    # check password in form against password hash in database
    if not bcrypt.check_password_hash(user_in_db.password, request.form['log_password']):
        flash("invalid credentials")
        return redirect('/')
    # redirect if not found
    # log user in
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    # redirect to app page
    return redirect("/recipes")

@app.route('/users/show/<int:id>')
def show_user(id):
    # create user show page if necessary
    return render_template("show.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')