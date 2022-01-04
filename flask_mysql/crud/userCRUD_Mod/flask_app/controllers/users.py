from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route('/user/new')
def create():
    return render_template("new_user.html")

@app.route('/process', methods=['POST'])
def process():
    users = {
        "first_name": request.form["fName"],
        "last_name" : request.form["lName"],
        "email" : request.form["email"]
    }
    User.save(users)
    return redirect ('/')

@app.route('/showuser/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html", user = User.showOneUser(data))

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html", user = User.showOneUser(data))

@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/')