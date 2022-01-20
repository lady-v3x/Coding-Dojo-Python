from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not User.is_valid(request.form):
        return redirect('/')
    data = {
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "email": request.form['email'],
        "pw" : bcrypt.generate_password_hash(request.form['pw']),
        "pwConfirm" : bcrypt.generate_password_hash(request.form['pwConfirm'])
    }
    id=User.newUser(data)
    session['user_id'] = id
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template("dashboard.html", user = User.get_by_id(data), recipes = Recipe.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['post'])
def login():
    data = {
                "email": request.form['email'],
                "pw" : bcrypt.generate_password_hash(request.form['pw'])
            }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.pw, request.form['pw']):
        flash("Invalid Password.")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')