## Wprowadzenie do Backendu i modelu klient-serwer

- Definicja Backendu
- Kluczowe technologie backendowe
- Zasada działania modelu klient-serwer
- Wprowadzenie do Flask (co to jest i jak go użyć)

## Backend - co to jest?

- Część aplikacji internetowej działająca po stronie serwera
- Przetwarza żądania klienta i dostarcza odpowiedzi
- Zarządza i manipuluje danymi w bazie danych
- Implementuje logikę biznesową aplikacji

## Kluczowe technologie backendowe

- Spring Framework: Platforma dla aplikacji Java
- Hibernate: Framework ORM dla aplikacji Java
- Node.js: Platforma dla aplikacji JavaScript
- Ruby on Rails: Framework dla aplikacji Ruby
- Django: Framework dla aplikacji Python
- Flask: Mikroframework dla aplikacji Python
- Java: Język programowania i platforma
- PHP: Język skryptowy dla aplikacji internetowych

## Model klient-serwer - jak działa?

- Architektura systemów komputerowych oparta na podziale na klienta i serwer
- Klient: część aplikacji dostępna i obsługiwana przez użytkownika
- Serwer: część aplikacji odpowiedzialna za przetwarzanie żądań klienta
- Umożliwia skalowanie, łatwiejsze utrzymanie i rozwój systemu
- Komunikacja odbywa się za pomocą protokołów sieciowych (np. HTTP, HTTPS)

## Klient - cechy

- Urządzenie użytkownika (smartfon, laptop, tablet, smart TV)
- Program wykonywany lokalnie na urządzeniu
- Odpowiedzialny za prezentację frontendu
- Wyświetla treści, zbiera interakcje użytkownika
- Komunikuje się z backendem, wysyłając żądania i odbierając odpowiedzi

## Serwer - cechy

- Urządzenie obsługujące aplikację (np. Raspberry Pi, serwery, laptop)
- Program uruchamiający kod lokalnie na urządzeniu serwera
- Komunikuje się z bazą danych i innymi serwerami
- Odpowiada na żądania klientów, wysyłając dane i informacje

## Wprowadzenie do Flask

- Mikroframework webowy w Pythonie
- Ułatwia tworzenie prostych aplikacji internetowych
- Łatwy do nauki, szybki w implementacji
- Oparty na WSGI, kompatybilny z różnymi serwerami
- Wbudowany serwer developerski
- Obsługa żądań HTTP, szablony, rozszerzenia

## Przykłady zastosowań Flask

- Strony internetowe, blogi, platformy społecznościowe
- Pinterest (potwierdzone info)
- Często używany w kursach uniwersyteckich (obok Django), np. Cornell

## Tworzenie aplikacji w Flask

- Zdefiniować instancję aplikacji za pomocą klasy Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Witaj w aplikacji Flask!"

if __name__ == "__main__":
    app.run()
```

## Routing w Flask

- Określa reakcje na żądania HTTP
- Dekorator @app.route("/ścieżka")
- Funkcja obsługująca trasę zwraca odpowiedź

```python
@app.route("/powitanie/<string:name>")
def powitanie(name):
    return f"Witaj, {name}!"

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    suma = a + b
    return f"Suma {a} + {b} = {suma}"
```

## Szablony w Flask

- Dynamiczne strony internetowe
- Oparte na języku szablonów Jinja2
- Użyć funkcji render_template() w funkcji obsługującej trasę

```python
from flask import render_template

@app.route("/powitanie-szablon/<string:name>")
def powitanie_szablon(name):
    return render_template("powitanie.html", imie=name)
```

Utwórz plik szablonu `powitanie.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Witaj w aplikacji Flask!</title>
</head>
<body>
    <h1>Witaj, {{ imie }}!</h1>
</body>
</html>
```

