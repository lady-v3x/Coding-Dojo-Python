from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipe/<int:id>')
def showRecipe(id):
    data = {
        "recipe.id": id,
        "id": session['user_id']
    }
    return render_template('showRecipe.html', recipe = Recipe.get_by_id(data),  user = User.get_by_id(data))

@app.route('/update/recipe',  methods = ['post'])
def updateRecipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/recipe/{request.form['id']}")
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "madeOn": request.form["madeOn"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/new/recipe')
def newRecipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('addRecipe.html',user=User.get_by_id(data))



@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "madeOn": request.form["madeOn"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def editRecipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "recipe.id":id
    }
    return render_template("editRecipe.html",edit=Recipe.get_by_id(data))

@app.route('/destroy/recipe/<int:id>')
def destroyRecipe(id):
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')