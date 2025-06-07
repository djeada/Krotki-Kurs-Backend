from flask import Flask, jsonify, request

app = Flask("Biblioteka")

ksiazki = [
    {" id ": 1, " tytul ": " Przygody Tomka Sawyera ", " autor ": " Mark Twain "},
    {" id ": 2, " tytul ": " Władca Pierścieni ", " autor ": " J.R.R. Tolkien "},
    {" id ": 3, " tytul ": " Ojciec Chrzestny ", " autor ": " Mario Puzo "},
]


@app.route("/")
def lista_ksiazek():
    return jsonify(ksiazki)


@app.route("/<int:id>")
def ksiazka(id):
    if id >= 0 and id < len(ksiazki):
        return jsonify(ksiazki[id])
    return "Not Found", 404


@app.route("/", methods=["POST"])
def dodaj_ksiazke():
    nowa = request.json
    ksiazki.append(nowa)
    return "Success", 201


app.run(debug=True)
