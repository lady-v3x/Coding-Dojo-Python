from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("dojosurvey.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        return render_template(
            "surveyinfo.html", 
            name = request.form["name"],
            location = request.form["location"],
            favLang = request.form["favLang"],
            comment = request.form["comment"]
        )
    else:
        return render_template(
            "surveyinfo.html",
            name = request.args.get("name"),
            location = request.args.get("location"),
            favLang = request.args.get("favLang"),
            comment = request.form("comment")
        )

app.run(debug = True)