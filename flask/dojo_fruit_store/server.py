from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print("Below is request.form dictonary")
    print(request.form)
    # fruit request form data
    strawberry_amt = request.form['strawberry']
    raspberry_amt = request.form['raspberry']
    apple_amt = request.form['apple']
    blackberry_amt = request.form['blackberry']

    # information request form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count = int(strawberry_amt) + int(raspberry_amt) + int(apple_amt) + int(blackberry_amt)
    print(f"Charging { first_name } { last_name } for { count } fruit") 
    return render_template("checkout.html", fname_template=first_name, lname_template=last_name, studentid=student_id, straw_amt=strawberry_amt, raspb_amt=raspberry_amt, apple_amt=apple_amt, black_amt=blackberry_amt )


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)