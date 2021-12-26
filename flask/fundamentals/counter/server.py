
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'BL0DR3INA-x_x-<3'

@app.route("/")
def index():
    if "count" in session.keys():
        session["count"] += 1
    else:
        session["count"] = 1
        print (session["count"])
    return render_template("counter.html", number = session["count"])

@app.route('/add', methods=['POST'])
def add_two():
    session["count"] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
