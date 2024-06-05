#Создадим код для введения пароля:

from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<password>/")
def hello_world(password=None):
    if password == "1234":
        return f"Доступ разрешён"
    else:
        return f"Доступ запрещён"

if __name__ == "__main__":
    app.run()