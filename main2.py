#Теперь мы можем написать любое дополнение в адресную строку,
# и это дополнение будет выводиться на сайте после “Привет”.

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<name>/")
def hello_world(name="незнакомец"):
    return f"Привет, {name}"

if __name__ == "__main__":
    app.run()