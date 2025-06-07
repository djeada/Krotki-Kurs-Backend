# Krotki-Kurs-Backend

**Krotki-Kurs-Backend** to lekki, edukacyjny projekt pokazujący, jak krok po kroku tworzyć API w Pythonie, wzbogacone o fragmenty w JavaScript (Node.js) oraz opcjonalne rozszerzenia w Go. Idealny punkt wyjścia do nauki budowy serwerów RESTful, uwierzytelniania, pracy z bazami danych i prostego zarządzania klientami frontendowymi (czysty JS, React itp.).

## 🔍 O projekcie

“Krotki-Kurs-Backend” to zestaw przykładów aplikacji i notatek teoretycznych, których celem jest:

- **Zrozumienie podstaw** tworzenia API w Pythonie (FastAPI lub Flask – w zależności od folderu/gałęzi).  
- **Integracja fragmentów** w JavaScript (Node.js) — np. WebSocket, asynchroniczne zadania, skrypty narzędziowe.  
- **Dodanie modułów w Go** — szybkie przetwarzanie danych, serwer gRPC lub prosta mikrousługa HTTP.  
- **Stopniowe kroki** edukacyjne:
  1. Minimalny Flask z obsługą GET  
  2. Dodanie endpointów POST  
  3. Pisanie testów  
  4. Uwierzytelnianie JWT  
  5. Konteneryzacja (Docker)  
  6. Obserwowalność (Prometheus + Grafana)  
  7. Konfiguracja reverse proxy (Apache / Nginx)  

Każdy przykład ma formę “krótkiego kursu” — zawiera tylko niezbędne pliki i kod, aby uniknąć nadmiaru i skupić się na kluczowych koncepcjach.

## 🛠 Technologie

### Python
- **Framework**: FastAPI (główna gałąź) / Flask (starsze branch’e)  
- **ORM / DB**: SQLModel / SQLAlchemy z SQLite (domyślnie) lub PostgreSQL/MySQL  
- **Uwierzytelnianie**: Python-Jose (JWT), Passlib (hashowanie haseł)  
- **Inne**: Uvicorn, Pydantic, Alembic (migracje)  

### JavaScript (Node.js)
- **Serwer narzędziowy**: Express  
- **WebSocket**: Socket.IO  
- **Klient HTTP**: axios / node-fetch  
- **Narzędzia**: npm scripts (`start`, `test`, `lint`)  

### Go (opcjonalnie)
- **Mikroserwis**: folder `go_service/` z `go.mod` i `main.go`  
- **Protokół**: HTTP lub gRPC  

### Baza danych
- **Domyślnie**: SQLite (`db.sqlite3` w root)  
- **Alternatywa**: PostgreSQL (konfiguracja przez ENV VAR)  

### Docker (opcjonalnie)
- **Dockerfile** do konteneryzacji serwisu Python  
- **docker-compose.yml** do uruchomienia całego stacku (backend + DB)  

## ⭐ Główne funkcje

- **CRUD** dla przykładowego zasobu (użytkownicy / artykuły)  
  - GET lista, GET pojedynczy, POST, PUT/PATCH, DELETE  
  - Walidacja za pomocą Pydantic  

- **Uwierzytelnianie JWT**  
  - Rejestracja użytkownika (hashowanie przez Passlib)  
  - Logowanie → zwrot tokena JWT (Python-Jose)  
  - Ochrona wybranych endpointów przez dependency/dekorator  

- **Asynchroniczna obsługa** (FastAPI + async/await)  
  - Przykład “długotrwałej” operacji  

- **WebSocket** (Node.js + Socket.IO)  
  - Prostą implementację czatu lub powiadomień w `socket_server.js`  
  - Przykładowy klient w `public/index.html`  

- **Mikroserwis w Go**  
  - Zwrot aktualnego timestampu lub komunikatu JSON  
  - Możliwość wywołania z Pythona (subprocess / HTTP)  

- **Migracje bazodanowe** (Alembic)  
  - Katalog `alembic/` z plikiem `env.py` i przykładami w `versions/`  

- **Dokumentacja API**  
  - Swagger UI dostępne pod `/docs`  
  - ReDoc pod `/redoc`  

## 🚀 Instalacja i uruchomienie

> **Uwaga:** instrukcja dla UNIX (Linux/macOS). Na Windows użyj PowerShell, Git Bash lub WSL — komendy są analogiczne.

### 1. Sklonuj repozytorium
```bash
git clone https://github.com/<twoj_uzytkownik>/Krotki-Kurs-Backend.git
cd Krotki-Kurs-Backend
````

Projekt podzielony jest na odcinki w katalogu `src/odcinekX`, odpowiadające kolejnym etapom kursu.

### 2. (Opcjonalnie) Wirtualne środowisko Python

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Python — zależności

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Node.js — WebSocket i skrypty narzędziowe

```bash
cd node_service   # jeśli chcesz uruchomić serwer Socket.IO lub inne skrypty JS
npm install
```

### 5. Uruchomienie z Dockerem

1. Upewnij się, że masz zainstalowane:

   * Docker
   * Docker Compose
2. Skopiuj i skonfiguruj plik środowiskowy:

   ```bash
   cp .env.example .env
   # Edytuj .env:
   # DATABASE_URL=sqlite:///./db.sqlite3
   # SECRET_KEY=twoj_tajny_klucz
   ```
3. Zbuduj i uruchom:

   ```bash
   docker-compose up --build
   ```
4. Dostępne usługi:

   * Backend FastAPI:  `http://localhost:8000`

     * Swagger UI:  `http://localhost:8000/docs`
     * ReDoc:       `http://localhost:8000/redoc`
   * (Opcjonalnie) PostgreSQL: `localhost:5432`

### 6. Uruchomienie bez Dockera

1. Upewnij się, że masz zainstalowaną bazę danych:

   * SQLite (plik `db.sqlite3`) lub
   * PostgreSQL (konfiguracja `DATABASE_URL`)
2. Wykonaj migracje:

   ```bash
   alembic upgrade head
   ```
3. Odpal serwer FastAPI:

   ```bash
   uvicorn app.main:app --reload
   ```
4. (Opcjonalnie) W osobnym terminalu uruchom WebSocket:

   ```bash
   cd node_service
   node socket_server.js
   ```
5. (Opcjonalnie) Go-service:

   ```bash
   cd go_service
   go run main.go
   ```

## 🔌 Przykładowe endpointy

### Rejestracja

```http
POST /users/register
Content-Type: application/json

{
  "username": "jan_kowalski",
  "email":    "jan@example.com",
  "password": "bezpieczne_haslo"
}
```

Zwraca dane nowego użytkownika (bez hasła).

### Logowanie

```http
POST /users/login
Content-Type: application/x-www-form-urlencoded

username=jan_kowalski&password=bezpieczne_haslo
```

Zwraca JSON z polem `access_token`.

### Pobranie profilu (chronione)

```http
GET /users/me
Authorization: Bearer <token_JWT>
```

### CRUD “items”

* **GET**  `/items/`         – lista wszystkich
* **POST** `/items/`         – utwórz nowy (JSON: `{ "title": "", "content": "" }`)
* **GET**  `/items/{id}`     – pobierz po ID
* **PUT**  `/items/{id}`     – modyfikuj
* **DELETE** `/items/{id}`   – usuń

---

## 🔌 WebSocket (Node.js + Socket.IO)

#### Serwer (`node_service/socket_server.js`)

```js
const express = require("express");
const http    = require("http");
const socket  = require("socket.io");

const app  = express();
const srv  = http.createServer(app);
const io   = socket(srv);

io.on("connection", sock => {
  console.log("Nowe połączenie:", sock.id);
  sock.on("message", msg => {
    console.log("Otrzymano:", msg);
    io.emit("message", `Odebrane: ${msg}`);
  });
  sock.on("disconnect", () => console.log("Rozłączono:", sock.id));
});

srv.listen(3000, () => console.log("Socket.IO na porcie 3000"));
```

#### Klient (np. `public/index.html` lub Node.js)

```js
const io = require("socket.io-client");
const socket = io("http://localhost:3000");

socket.on("connect", () => {
  console.log("Połączono:", socket.id);
  socket.emit("message", "Cześć od klienta!");
});
socket.on("message", msg => console.log("Serwer:", msg));
```

## 🔒 Uwierzytelnianie JWT

1. Hasło hashowane przez **Passlib + bcrypt**.
2. Logowanie zwraca **JWT** (Python-Jose).
3. Ochrona endpointów w FastAPI przez dependency `get_current_user`, która:

   * Odczytuje token z nagłówka `Authorization`.
   * Weryfikuje i dekoduje JWT.
   * Sprawdza istnienie użytkownika w bazie.
   * Zwraca obiekt `current_user`.

## 🤝 Wkład i kontrybucje

Chcesz pomóc?

* Zgłaszaj **Issues** na GitHubie.
* Twórz **Pull Requesty**:

  * Poprawki, testy (pytest), dokumentacja.
  * Nowe funkcje: OAuth2, weryfikacja email, testy integracyjne, monitoring.
* Rozbuduj frontend:

  * React/Vue/Angular + komunikacja z API.
  * Przykład chat’u real-time z WebSocket.

Prosimy o przestrzeganie konwencji **PEP8** (Python) i **ESLint** (JS).

## 📄 Licencja

Ten projekt dostępny na licencji **MIT**.

