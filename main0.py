#Работа с HTML при помощи специальной функции:
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def films():
    return render_template("index04.html")

@app.route("/person/")
def person():
    return render_template("main04.html")

if __name__ == "__main__":
    app.run()