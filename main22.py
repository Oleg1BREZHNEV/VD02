#Также мы можем прописывать HTML (но не очень удобно).
# Писать мы его будем в тройных кавычках, чтобы можно
# было писать много строк:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <h1>Тестовый запуск локального сервера</h1>
    <p>А это просто текст</p>
    """
    return html

if __name__ == "__main__":
    app.run()