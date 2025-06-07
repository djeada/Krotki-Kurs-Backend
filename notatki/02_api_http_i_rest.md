## API, HTTP i REST

### Co będziesz wiedzieć?

* Dowiesz się, czym jest protokół HTTP, jak wygląda wymiana żądania i odpowiedzi oraz poznasz metody GET, POST, DELETE i PUT wraz z kodami statusu.
* Zrozumiesz, czym jest API, poznasz architekturę REST oraz inne modele komunikacji.
* Nauczysz się korzystać z API, używając narzędzia curl, biblioteki requests w Pythonie i funkcji fetch w JavaScript w przeglądarce.
* Poznasz narzędzia DevTools, dowiesz się, jak śledzić żądania sieciowe i analizować ich nagłówki.
* Zrozumiesz, czym jest JSON, dlaczego jest tak popularny i jakie wiążą się z nim ograniczenia.

### Powtórka (z rozszerzeniem)

* Serwer to komputer lub program, ktory udostepnia zasoby lub uslugi, a klient wysyla zadania do serwera. Serwerow moze byc wiele, wspolpracujacych ze soba.
* Frontend to czesc aplikacji dzialajaca po stronie uzytkownika, na przyklad przegladarka renderujaca strone, a backend to serwer odpowiedzialny za przetwarzanie zadan i wysylanie odpowiedzi.
* Wspolczesne systemy sa wielowarstwowe – backend jednej uslugi moze byc frontendem dla innej uslugi (mikroserwisy).
* Przyklad: przegladarka laczy sie z serwerem, ktory udostepnia pliki HTML, JS, CSS i obrazy; podobnie jądro systemu operacyjnego wspolpracuje ze sterownikami, ktore komunikuja sie z kontrolerami dyskow.

```
+---------------------+
|   Jądro (Kernel)    |
|     [Backend]       |
+----------+----------+
           |
           | komunikacja
           |
+----------v---------------+
|    Sterownik (Driver)    |
| [Frontend dla kontrolera |
|   oraz backend dla k.’a] |
+----------+---------------+
           |
           | komunikacja
           |
+----------v----------+
| Kontroler dysku     |
|  (Disk Controller)  |
|     [Hardware]      |
+---------------------+
```

#### Model Klient Serwer

Więcej przykładów systemów działających w modelu **klient-serwer**

| Kategoria                        | Serwer                                        | Typowy klient / protokół                                           |
| -------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ |
| **Pliki i udziały**              | **SMB/CIFS** (Samba, Windows File Server)     | Eksplorator Windows, `smbclient`, macOS Finder                     |
|                                  | **FTP/SFTP**                                  | FileZilla, WinSCP, `ftp` / `sftp` w terminalu                      |
| **Bazy danych**                  | **PostgreSQL**                                | psql, pgAdmin, aplikacje korzystające z drivera PG                 |
|                                  | **MongoDB**                                   | mongo shell, aplikacje z driverem Mongo                            |
| **Web / API**                    | **HTTP serwer (Apache, Nginx, Node.js)**      | Przeglądarka, `curl`, aplikacje mobilne/SPA                        |
| **Poczta elektroniczna**         | **SMTP** (wysyłka)                            | Mail Transfer Agent (Postfix) -> serwery dalej / klient wysyłający |
|                                  | **IMAP / POP3** (odbiór)                      | Thunderbird, Outlook, aplikacje mobilne                            |
| **Nazwa hostów**                 | **DNS**                                       | System resolver, `dig`, przeglądarka                               |
| **Czas**                         | **NTP**                                       | Usługa czasu w systemie operacyjnym                                |
| **Zdalny dostęp**                | **SSH**                                       | `ssh` w terminalu, PuTTY, scp/rsync                                |
|                                  | **RDP**                                       | Microsoft Remote Desktop, rdesktop                                 |
| **Kolejki wiadomości / IoT**     | **RabbitMQ (AMQP)**                           | Producent/Konsument AMQP, micro-services                           |
|                                  | **MQTT broker (Mosquitto, HiveMQ)**           | Czujniki IoT, Home-Assistant                                       |
| **Cache / pamięć klucz-wartość** | **Redis**                                     | Aplikacje web, CLI `redis-cli`                                     |
| **Druk**                         | **CUPS Print Server**                         | Dialog drukowania w systemie, IPP                                  |
| **Strumieniowanie multimediów**  | **Icecast / RTSP**                            | VLC, odtwarzacze sieciowe                                          |
| **Gry online**                   | **Minecraft Server, CS\:GO Dedicated Server** | Klient gry                                                         |

W każdym z przypadków jedna strona (serwer) **nasłuchuje** na określonym porcie, czeka na żądania i zarządza współdzielonym zasobem (pliki, dane, czas, druk, audio, itp.). Druga strona (klient) **nawiązuje połączenie**, wysyła zapytania lub komendy i odbiera odpowiedzi. Układ jest więc asymetryczny – serwer utrzymuje usługę, klient z niej korzysta.

#### Jak działa klasyczny serwer?

Serwer odczytuje z dysku plik HTML (oraz powiązane CSS/JS) i przekazuje go *bez zmian* do przeglądarki.

**Dynamiczna strona (szablony)**

- Szablon HTML zawiera pola do uzupełnienia.
- Serwer (lub interpreter / framework) wypełnia je danymi (użytkownik, stan aplikacji, baza).
- Powstaje **nowo wygenerowany** dokument, który trafia do klienta.

**Techniczny szczegół – odpowiedź HTTP**

- Serwer **nie wysyła „pliku” jako pliku**, lecz ramkę **Odpowiedź HTTP**:
    – nagłówki (status, typ MIME, długość, kompresja)
    – ciało z treścią żądanego zasobu.
- Przy statycznej stronie treść = zawartość pliku; przy kompresji (gzip/br) treść jest skompresowana, ale efekt wizualny w przeglądarce pozostaje ten sam.

**Co decyduje o rodzaju odpowiedzi?**

- **Nginx** w trybie „static” → serwuje pliki.
- **Apache + PHP-FPM** → uruchamia kod PHP, wynik trafia do klienta.
- **Serwer Pythona (Django/Flask/FastAPI)** → wykonuje kod Pythona i zwraca rezultat (HTML, JSON, inne).

```
                                [ Przeglądarka (Klient) ]
                                           |
                               1.  HTTP Request (GET/POST)
                                           v
                    +---------------------------------------------+
                    |                 Web Server                  |
                    |  (Apache / Nginx / IIS / Node.js itp.)      |
                    +---------------------------------------------+
                                           |
                               2.  Host-Header + URL routing
                                           v
                    +-----------------------------------------------------------+
                    |                Dispatcher Virtual Hosts                   |
                    +---------------+-------------------+-----------------------+
                    |  one.com      |   two.com         |   domyślny catch-all  |
                    |  /var/www/one |   /var/www/two    |   /var/www/html       |
                    +---------------+-------------------+-----------------------+
                            |                |                    |
               ┌────────────┴───────┐   ┌────┴───────────┐   ┌──-─┴────────────┐
               |                    |   |                |   |                 |
               |               3a. statyczny plik   3a. statyczny plik
               |                (HTML/IMG/CSS/JS)           ...                ...
               |                    |                    |
               |                    |─────►(bezpośrednie wysłanie pliku)◄──────┘
               |
   3b. dynamiczny skrypt (.php / .py / .jsp / .cgi)
               v
        +---------------------------------------------+
        |         Interpreter / Backend (3b)          |
        |  PHP-FPM - uWSGI - Node.js - Ruby - itp.     |
        +---------------------------------------------+
                       | 4. logika aplikacji:
                       |    - zapytania SQL
                       |    - walidacja / autoryzacja
                       |    - generowanie HTML / JSON
                       v
               +-------------------------------+
               |  Wygenerowana odpowiedź (4)   |
               +-------------------------------+
                               |
                       5.  HTTP Response
                               v
                        [ Przeglądarka ]
```

| Krok   | Co się dzieje?                                                                               |
| ------ | -------------------------------------------------------------------------------------------- |
| **1**  | Przeglądarka wysyła żądanie HTTP.                                                            |
| **2**  | Serwer analizuje nagłówek **Host** i ścieżkę URL.                                            |
| **3a** | Jeśli plik jest statyczny, serwer odczytuje go z dysku i przechodzi od razu do kroku 5.      |
| **3b** | Jeśli to skrypt, przekazuje żądanie do odpowiedniego interpretera lub procesu aplikacyjnego. |
| **4**  | Kod backendu wykonuje logikę (baza danych, generowanie treści).                              |
| **5**  | Serwer zwraca gotowy **HTTP Response** (HTML, JSON, obraz itp.).                             |

### HTTP 

* Protokół warstwy aplikacji odpowiedzialny za komunikację **klient ↔ serwer**
* Definiuje **formatowanie i transmisję** wiadomości (żądanie / odpowiedź)
* **Powszechnie stosowany** standard Web (HTTP / 1.1, HTTP / 2, HTTP / 3)
* **Nazwa domeny ≠ serwer** – musi zostać przetłumaczona przez **DNS** na adres IP serwera

#### Metody HTTP

Żeby zarządzać zasobami stosuje się metody:

* POST służy do tworzenia nowych zasobów (Create)
* GET służy do pobierania zasobów (Retrieve)
* PUT służy do aktualizowania istniejących zasobów (Update)
* DELETE służy do usuwania zasobów (Delete)

Oprócz CRUD istnieją też inne metody, np. HEAD, OPTIONS czy PATCH.

#### Kody Statusu

![diagram_kodu_http](https://github.com/user-attachments/assets/160486c3-7278-48f6-bf12-f7ce6e3b61e9)

* Teoria mówi, że kody 1xx–5xx jasno informują o wyniku żądania.
* W praktyce wiele API zwraca 200 nawet przy błędzie, bo nie obsługują wyjątków w endpointach.
* Często domyślny kod 500 pochodzi z frameworka, chociaż lepiej byłoby zwrócić np. 404 lub inny odpowiedni kod.
* Niektórzy używają POST zamiast GET czy DELETE, bo chcą przesłać więcej danych lub uniknąć ograniczeń GET.

#### Żądanie (Request)

* Klient wysyła żądanie przez sieć do serwera.
* URL wskazuje, jaki zasób chcemy pobrać lub zmodyfikować (może zawierać parametry zapytania).
* Metoda HTTP (GET, POST, PUT, DELETE) określa, co ma się stać z zasobem.

Podstawowe elementy żądania:

```
HTTP REQUEST  (klient → serwer)
┌────────────────────────────────────────────┐
│ Request-Line                               │
│   GET /index.html HTTP/1.1                 │
├────────────────────────────────────────────┤
│ Nagłówki (Headers)                         │
│   Host: example.com                        │
│   User-Agent: Mozilla/5.0 …                │
│   Accept: text/html                        │
│   …                                        │
├────────────────────────────────────────────┤
│ Pusta linia  (CRLF)                        │
├────────────────────────────────────────────┤
│ Body  (opcjonalny)                         │
│   ← dla POST/PUT: JSON, formularz, plik →  │
└────────────────────────────────────────────┘
```

W nagłówkach znajdziemy m.in.:

* metodę żądania (np. POST), adres URL (np. `/api/users`), wersję HTTP (np. `HTTP/1.1`)
* `Host`, czyli docelowy serwer (np. `example.com`)
* `Content-Type`, określający format ciała (np. `application/json`)
* `Content-Length`, czyli rozmiar ciała żądania

W ciele żądania przesyłamy dane (najczęściej w JSON):

```
{
    "username": "jan_kowalski",
    "email": "jan_kowalski@example.com",
    "password": "haslo123"
}
```

#### Odpowiedź (Response)

* Serwer wysyła odpowiedź do klienta, używając protokołu HTTP.
* Status-Line informuje o wersji HTTP, kodzie statusu i krótkim opisie (np. `HTTP/1.1 200 OK`).
* Nagłówki (Headers) zawierają meta-informacje o odpowiedzi, takie jak `Content-Type`, `Content-Length`, `Cache-Control` itp.
* Po pustej linii (CRLF) pojawia się ciało odpowiedzi (Body), które może być statycznym plikiem (HTML, obraz, CSS) lub wygenerowaną dynamicznie treścią.

```
HTTP RESPONSE (serwer → klient)
┌────────────────────────────────────────────┐
│ Status-Line                                │
│   HTTP/1.1 200 OK                          │
├────────────────────────────────────────────┤
│ Nagłówki (Headers)                         │
│   Content-Type: text/html; charset=utf-8   │
│   Content-Length: 347                      │
│   Cache-Control: max-age=3600              │
│   …                                        │
├────────────────────────────────────────────┤
│ Pusta linia  (CRLF)                        │
├────────────────────────────────────────────┤
│ Body                                       │
│   <html> …                                 │
└────────────────────────────────────────────┘
```

#### Jak wysłać żądania?

Możesz użyć narzędzia curl w terminalu, które ma wiele opcji konfiguracyjnych. Przykład prostego żądania POST z JSON-em:

```bash
curl -X POST https://twoj-serwer.pl/api/sciezka \
-H "Content-Type: application/json" \
-d '{"klucz1":"wartość1","klucz2":123,"klucz3":true}'
```

DevTools w przeglądarkach (Chrome, Firefox) to zintegrowane narzędzia dla deweloperów, które ułatwiają:

* analizę struktury i stylów strony,
* podgląd i debugowanie kodu JavaScript,
* monitorowanie sieci (Network) — widać wszystkie wysyłane żądania i odpowiedzi,
* zarządzanie pamięcią podręczną, profilowanie wydajności i inne.
  
W JavaScript w przeglądarce możesz użyć funkcji `fetch`:

```javascript
fetch('https://twoj-serwer.pl/api/sciezka', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    klucz1: 'wartość1',
    klucz2: 123,
    klucz3: true
  })
})
.then(response => {
  if (!response.ok) {
    throw new Error(`Błąd sieci: ${response.status}`);
  }
  return response.json();
})
.then(data => {
  console.log('Odpowiedź z serwera:', data);
})
.catch(error => {
  console.error('Coś poszło nie tak:', error);
});
```

W Pythonie, za pomocą biblioteki `requests`, wygląda to tak:

```python
import requests

url = 'https://twoj-serwer.pl/api/sciezka'
payload = {
  "klucz1": "wartość1",
  "klucz2": 123,
  "klucz3": True
}
response = requests.post(url, json=payload)
if response.status_code == 200:
  data = response.json()
  print('Odpowiedź z serwera:', data)
else:
  print('Błąd:', response.status_code)
```

#### Przykład żądania GET 

`http://wttr.in/NAZWA_MIASTA`

- Chcemy pobrać dane pogodowe dla konkretnego miasta, np. Warszawy.
- Nazwa hosta: `wttr.in`
- Ścieżka: `/Warsaw` (gdzie Warsaw to `/NAZWA_MIASTA`)

**Połączenie TCP/DNS**

Przeglądarka/klient tlumaczy `wttr.in` na adres IP i otwiera połączenie na porcie 80.

**Żądanie HTTP**

```
GET /Berlin HTTP/1.1
Host: wttr.in
Accept: application/json
Connection: close
```

**Odpowiedź HTTP**

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length:  1024
Cache-Control: max-age=600
Connection: close

{
 "current_condition":[
   {
     "temp_C":"16",
     "weatherDesc":[{"value":"Sunny"}],
     "windspeedKmph":"10"
     …
   }
 ],
 "weather":[
   {
     "date":"2025-06-03",
     "hourly":[…]
     …
   },
   …
 ]
}
```

* Ścieżka `/Berlin` to `/NAZWA_MIASTA`.
* Nagłówek `Accept: application/json` prosi o JSON.
* Serwer zwraca kod 200, nagłówki z typem treści `application/json` i ciało z danymi pogodowymi.

#### Przykład żądania POST

```
POST /posts HTTP/1.1
Host: jsonplaceholder.typicode.com
Content-Type: application/json; charset=UTF-8
Content-Length:  fifty

{"title":"abc","body":"xyz","userId":5}
```

* Metoda: POST
* Ścieżka: `/posts`
* Ciało żądania (JSON): `{"title":"abc","body":"xyz","userId":5}`

Przykład w `curl`:

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
     -H "Content-Type: application/json; charset=UTF-8" \
     -d '{"title":"abc","body":"xyz","userId":5}'
```

**Odpowiedź (JSON):**

```json
{
  "id": 101,
  "title": "abc",
  "body": "xyz",
  "userId": 5
}
```

### API

* API (Application Programming Interface) to zestaw reguł i protokołów umożliwiający komunikację między aplikacjami, niekoniecznie tylko przez internet.
* Przykładem może być API Windows, które pozwala na dostęp do funkcji systemowych z poziomu innej aplikacji.
* API dostarcza interfejs programistyczny, dzięki któremu programiści mogą korzystać z funkcjonalności innych programów lub usług.
* W ten sposób można tworzyć nowe aplikacje, wykorzystując już istniejące zasoby — na przykład pobierać dane lub wywoływać usługi zdalne.
* API pozwala na współdzielenie danych i funkcji między różnymi systemami, co ułatwia integrację i budowanie bardziej zaawansowanych rozwiązań.

Przykłady API działających przez HTTP:

* [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/)
* [https://api.github.com](https://api.github.com)

### Budujemy własne API (Flask)

* Jeden adres zasobu – różne metody (GET, POST, PUT, DELETE…)
* Kod stanu HTTP opisuje wynik (200, 201, 404…)
* JSON to standardowy format danych (czytelny dla ludzi i maszyn)

```
ksiazki = [
    {"id": 1, "tytul": "Przygody Tomka Sawyera", "autor": "Mark Twain"},
    {"id": 2, "tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien"},
    {"id": 3, "tytul": "Ojciec Chrzestny", "autor": "Mario Puzo"}
]
```

**Endpoint GET – lista książek**

```python
@app.route("/ksiazki")
def lista_ksiazek():
    return jsonify(ksiazki)          # 200 OK
```

* Żądanie: `GET /ksiazki`
* Odpowiedź: `200 OK` + JSON z tablicą książek

**Endpoint POST – dodawanie książki**

```python
@app.route("/ksiazki", methods=["POST"])
def dodaj_ksiazke():
    nowa = request.json              # oczekuje {"id": 4, "tytul": "...", "autor": "..."}
    ksiazki.append(nowa)
    return jsonify(nowa), 201        # 201 Created
```

* Żądanie: `POST /ksiazki` + nagłówek `Content-Type: application/json`
* Odpowiedź: `201 Created` + JSON nowo dodanego rekordu

### Protokoły aplikacyjne / Style interfejsów API

* HTTP to protokół transportowy używany do przesyłania żądań i odpowiedzi; REST to styl architektury, który korzysta z HTTP do operacji na zasobach
* REST API najczęściej zwraca JSON (dawniej bywał XML), wykorzystuje standardowe metody HTTP (GET, POST, PUT, DELETE) i kody statusu
* GraphQL to język zapytań zbudowany nad HTTP (można go kapsułkować w POST), pozwala klientowi precyzyjnie określić, jakich danych potrzebuje
* MQTT to lekki protokół publikuj-subskrybuj, używany głównie w IoT i przesyłaniu strumieniowym danych, nie jest typowym API-em REST-owym
* WebSockets oferują dwukierunkową, utrzymywaną na stałe sesję TCP, często stosowane do czatu, powiadomień lub strumieniowania (np. wraz z MQTT)
* SOAP to starszy protokół XML-owy oparty na wiadomościach SOAP, dziś rzadko spotykany (pozostał głównie w starszych systemach korporacyjnych)

