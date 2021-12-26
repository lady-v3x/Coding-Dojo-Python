from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checker():
    return render_template("checker.html", td = 8, tr = 8, col1 = "red", col2 = "black")
if __name__ == "__main__":
    @app.route('/<int:num>')
    def checker2(num):
        return render_template("checker.html", tr= 8, td = int(num), col1 = "red", col2 = "black")
    
    @app.route('/<int:num>/<int:num1>')
    def checker3(num,num1):
        return render_template("checker.html", td= int(num), tr = int(num1), col1 = "red", col2 = "black")
    
    @app.route('/<int:num>/<int:num1>/<string:col1>')
    def checker4(num,num1,col1):
        return render_template("checker.html", td= int(num), tr = int(num1), col1 = col1, col2 = "black")
    
    @app.route('/<int:num>/<int:num1>/<string:col1>/<string:col2>')
    def checker5(num,num1,col1,col2):
        return render_template("checker.html", td= int(num), tr = int(num1), col1 = col1, col2 = col2)
    app.run(debug=True)