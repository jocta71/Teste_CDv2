import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def helloWorld():
    return "Testando PRIMEIRA rota :D ! Insira /teste na URL"

@app.route("/teste", methods=["GET"])
def teste():
    return "Testando segunda rota :D !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
