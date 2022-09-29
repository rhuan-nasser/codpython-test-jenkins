from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Homepage criada para testes!"

app.run()
