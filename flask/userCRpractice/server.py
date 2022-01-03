from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)
app.secret_key = 'plsfuckingwork'

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



if __name__=="__main__":
    app.run(debug=True)