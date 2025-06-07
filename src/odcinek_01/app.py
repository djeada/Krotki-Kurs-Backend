from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route("/")
def hello():
    return "Witaj w aplikacji Flask!"

@app.route("/powitanie/<string:imie>")
def powitanie(imie):
    return f"Witaj, {imie}!"

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    suma = a + b
    return f"Suma {a} + {b} = {suma}"

@app.route("/powitanie-szablon/<string:imie>")
def powitanie_szablon(imie):
    return render_template("powitanie.html", imie=imie)


app.run()
