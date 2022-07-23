from flask_app import app, render_template, redirect, request, bcrypt, session,flash
from flask_app.models.recipe import Recipe


@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html', recipes=Recipe.get_all())

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_recipe.html')


@app.route('/create/recipe', methods=['post'])
def create_recipe():
    print(request.form)
    # this is the validation step 
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data = {'id': id}
    return render_template('edit_recipe.html', recipe = Recipe.get_one(data))

@app.route('/recipes/show/<int:id>')
def show_recipe(id):
    data = {'id': id}
    return render_template('show_recipe.html', recipe = Recipe.get_one_with_join(data))


@app.route('/recipes/delete/<int:id>')
def delete(id):
    data = {'id': id}
    Recipe.destroy(data)
    return redirect("/recipes")

