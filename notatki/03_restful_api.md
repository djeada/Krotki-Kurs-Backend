**Budowanie RESTful API**

## Co dzisiaj i w przyszłości się nauczysz

* **Planowanie i modelowanie API**

  * Jak zidentyfikować użytkowników i ich potrzeby
  * Tworzenie modelu zasobów i relacji między nimi
* **Ograniczenia architektury REST**

  * Poznaj sześć kluczowych zasad REST, które kształtują projekt API
* **Walidacja projektu**

  * Metody sprawdzania poprawności modelu API przed jego implementacją
* **Powtórka koncepcji HTTP**

  * Nagłówki, kody odpowiedzi i inne istotne zagadnienia HTTP
* **Typowe wyzwania projektowe**

  * Uwierzytelnianie i autoryzacja
  * Wersjonowanie API
  * Tworzenie i utrzymanie dokumentacji

## Dlaczego projektowanie API jest ważne?

1. **Złożoność projektowania**
   Projektowanie API wymaga świadomych decyzji i kompromisów – dotyka jednych z najtrudniejszych problemów w informatyce.
2. **Affordances (możliwości operacyjne)**
   Każda operacja, którą udostępniasz użytkownikowi, to affordance – pozwolenie na wykonanie określonej czynności.
3. **Zgodność celów**
   Dobrze zaprojektowane API łączy to, co użytkownik chce osiągnąć, z tym, co łatwo wykonać dzięki udostępnionym funkcjom, czyniąc API zarówno potężnym, jak i użytecznym.

## Klient i serwer mogą być czymkolwiek

* **REST API jako bibliotekarz**
  API pełni rolę pośrednika między klientami (aplikacje webowe, mobilne itp.) a miejscem przechowywania danych (baza danych lub inny serwer).
* **Przepływ zapytania i odpowiedzi**

  1. Klient wysyła żądanie do API.
  2. API pobiera niezbędne dane, formatuje je i odsyła odpowiedź.
  3. Klient przetwarza otrzymane dane na postać zrozumiałą dla użytkownika.
* **Obsługa wielu klientów**
  REST API potrafi równolegle obsługiwać zapytania z różnych źródeł, zapewniając efektywny dostęp do zasobów i ich modyfikację.

## URI (Uniform Resource Identifier)

> „Kompaktowy ciąg znaków identyfikujący zasób abstrakcyjny lub fizyczny, który dostarcza prosty i rozszerzalny sposób identyfikacji tego zasobu.”
> Źródło: MDN Web Docs – Glossary: URI

### Przykłady URI

Przykłady:
* `ftp://myserver.dev/files/docs/script.docx`
* `https://api.przyklad.com/uzytkownicy/42`
* `mailto:kontakt@przyklad.com`
* `urn:isbn:9788324621766`
* `tel:+1-412-111-5234`

```
+----------------------------------+
|               URI                |
|                                  |
|    +------------------------+    |
|    |         URL            |    |
|    +------------------------+    |
+----------------------------------+
```

> Uwaga: Nie wszystkie URI to URL-e.
![Hierarchia URI i URL](https://developer.mozilla.org/en-US/docs/Glossary/URI#examples)


## Co to jest REST?

**REST (Representational State Transfer)** to zbiór ograniczeń architektonicznych, które pozwalają tworzyć wydajne, niezawodne i skalowalne systemy.
REST definiuje sposób, w jaki klient i serwer komunikują się ze sobą za pomocą standardowych metod HTTP, operując na zasobach i ich reprezentacjach.

## API – definicja

**API (Application Programming Interface)** to zestaw reguł i interfejsów umożliwiających współpracę pomiędzy różnymi komponentami oprogramowania (lub między oprogramowaniem a sprzętem).

## Porównanie: REST vs inne technologie

| Cecha                      | SOAP                                                                                                   | REST                                               | GraphQL                                                     | gRPC                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Rok powstania**          | 1999                                                                                                   | 2000                                               | 2015                                                        | 2016                                                                       |
| **Format danych**          | wyłącznie XML                                                                                          | XML, JSON, HTML, tekst                             | JSON                                                        | Protobuf (głównie), JSON, XML, Thrift, FlatBuffers                         |
| **Transport**              | zazwyczaj HTTP/HTTPS                                                                                   | HTTP/HTTPS                                         | HTTP/HTTPS                                                  | HTTP/2                                                                     |
| **Społeczność**            | niewielka                                                                                              | duża                                               | rosnąca                                                     | duża                                                                       |
| **Przypadki użycia**       | bramki płatności, zarządzanie tożsamością, systemy finansowe, telekomunikacja, rozwiązania dziedziczne | publiczne API, proste aplikacje oparte na zasobach | mobilne API, złożone systemy, agregacja wielu mikroserwisów | komunikacja o niskich opóźnieniach i dużej przepustowości w mikroserwisach |
| **Złożoność**              | wysoka (specyfikacje, narzędzia)                                                                       | średnia                                            | średnia                                                     | wysoka (wymaga definiowania usług w Protobuf)                              |
| **Wsparcie wersjonowania** | trudniejsze (wszystko w XML, wymaga dodatkowej logiki)                                                 | proste (np. w URL lub nagłówkach)                  | wbudowane (nowe pola, deprecjacje w schemacie)              | wbudowane (wersjonowanie w Protobuf)                                       |

## Sześć ograniczeń architektury REST

1. **Client–Server (Klient–Serwer)**

   * Rozdzielenie odpowiedzialności:

     * Klient zarządza interfejsem i logiką użytkownika.
     * Serwer przechowuje dane i logikę biznesową.

   ```
       Klient 1       Klient 2
          \             /
           \           /
            \         /
             v       v
         +----------------+
         |  REST SERVER   |
         +----------------+
                  |
               [Baza Danych]
   ```

2. **Statelessness (Bezstanowość)**

   * Każde żądanie od klienta musi zawierać wszystkie informacje potrzebne do jego obsługi.
   * Serwer nie przechowuje żadnego kontekstu między kolejnymi zapytaniami.

3. **Cacheability (Możliwość buforowania)**

   * Odpowiedzi muszą być jawnie oznaczone jako buforowalne lub niebuforowalne.
   * Buforowanie może odbywać się na poziomie klienta lub pośredników (np. CDN), przyspieszając kolejne odczyty zasobów.

4. **Layered System (System wielowarstwowy)**

   * Klient nie widzi, czy komunikuje się bezpośrednio z serwerem, czy przez warstwę pośredników (CDN, proxy, load balancer).
   * Ułatwia to skalowanie i wprowadzanie dodatkowych warstw bezpieczeństwa lub buforowania.

5. **Code on Demand (Kod na żądanie)** *(opcjonalne)*

   * Serwer może przesyłać klientowi fragmenty kodu wykonywalnego (np. JavaScript), które klient pobiera i wykonuje.
   * Zwiększa elastyczność, ale może też obniżać przewidywalność zachowania systemu.

6. **Uniform Interface (Jednolity interfejs)**

   * **Identyfikacja zasobów** – każdy zasób ma unikalny identyfikator URI.
   * **Manipulacja przez reprezentacje** – klient modyfikuje zasób, przesyłając jego reprezentację (np. JSON).
   * **Samoopisujące komunikaty** – odpowiedzi zawierają wszystkie informacje potrzebne do przetworzenia (nagłówki, linki, typ zawartości).
   * **HATEOAS (Hypermedia as the Engine of Application State)** – reprezentacje zasobów zawierają linki do dostępnych operacji na nich.

**Jak REST odnosi się do HTTP?**

* REST wykorzystuje protokół HTTP jako podstawowy środek komunikacji.
* Operacje na zasobach w REST (pobieranie, tworzenie, aktualizacja, usuwanie) mapują się bezpośrednio na metody HTTP:

  * **GET** – odczyt zasobu
  * **POST** – utworzenie nowego zasobu
  * **PUT** – pełna aktualizacja zasobu
  * **PATCH** – częściowa aktualizacja zasobu
  * **DELETE** – usunięcie zasobu
* Nagłówki HTTP (np. `Content-Type`, `Accept`, `Cache-Control`) służą do negocjacji formatu danych, wersjonowania i zarządzania buforowaniem.

## Kto lub co wchodzi w interakcję z REST API?

1. **Aplikacje klienckie**

   * Przeglądarki WWW
   * Aplikacje mobilne
   * Skrypty serwerowe
2. **Urządzenia IoT / Boty**

   * Sensory, automatyka domowa, robotyka
3. **Inne usługi sieciowe**

   * Pośrednie mikroserwisy
   * Systemy kolejkowania zadań
4. **Narzędzia deweloperskie**

   * Postman, curl, klienty HTTP w różnych językach

## Odkrywanie (Discovery)

* **Punkt wejścia** – każde REST API udostępnia bazowy URI (np. `/api/`), od którego zaczynamy eksplorację.
* **HATEOAS** (Hypermedia as the Engine of Application State) – odpowiedzi zawierają linki (URI) do powiązanych zasobów i dostępnych operacji, umożliwiając dynamiczne „odkrywanie” API.

## Czym są zasoby?

> *“Kluczową abstrakcją w REST jest zasób. Każda informacja, którą można nazwać, może być zasobem: dokument, obraz, usługa… Zasób to konceptualne mapowanie na zbiór encji, nie konkretna encja w danej chwili.”*

* **Zasób** – logiczna jednostka informacji dostępna pod unikalnym URI.
* **Reprezentacja** – konkretna postać danych zasobu (np. JSON, XML, HTML), przenoszona między klientem a serwerem.
* **Kolekcja zasobów** – np. „wszystkie czerwone książki”
* **Pojedynczy zasób** – np. „czerwona książka z półki nr 4”

```
URI: /biblioteka/ksiazki/czerwone/polki/4
```

## Zrozumienie procesów biznesowych

1. **Poznaj proces** – np. zakup książki online: od wyboru tytułu, przez weryfikację magazynu, koszyk, aż po płatność.
2. **Wykorzystaj HTTP** – HTTP jest wystarczająco ekspresyjne, by przekazywać statusy i komunikaty błędów (kody 2xx, 4xx, 5xx).
3. **Narzędzia do analizy ruchu** – Postman, curl, dodatki Live Headers w przeglądarce pomagają podejrzeć nagłówki i ciało zapytań/odpowiedzi.

## Jak projektować API?

### Uczestnicy (Participants)

* Zidentyfikuj podmioty biorące udział w procesie:

  * Ludzie (klient, administrator)
  * Systemy (baza danych, płatności)
* Podziel na:

  * **Wewnętrzne** vs **zewnętrzne**
  * **Aktywne** (inicjują akcje) vs **pasywne** (oczekują na zdarzenia)

### Aktywności (Activities)

* Skoncentruj się na **procesach biznesowych** (cele, nie tylko kroki).
* Opisz, kto wykonuje jaką czynność i w jakiej kolejności.
* Zidentyfikuj zależności między działaniami.

### Grupowanie metod i zasobów

1. Wyszukaj **rzeczy** (rzeczowniki): produkty, zamówienia, koszyki.
2. Zastanów się, czy koszyk to **kolekcja** pozycji, czy każdy wiersz to oddzielny zasób.
3. Mapuj aktywności na **czasowniki** HTTP:

   * GET /produkty
   * POST /koszyki
   * PUT /koszyki/{id}/pozycje
   * DELETE /zamowienia/{id}

## Weryfikacja przed implementacją

* Twórz **dokumentację** (Swagger/OpenAPI) jeszcze przed kodowaniem.
* Korzystaj z mikroframeworków (hapi.js, Slim) do szybkiego prototypowania i testów.
* Zbieraj feedback od użytkowników i zespołu na wczesnym etapie.

## Wersjonowanie API

* **W URL**: `/v1/produkty`, `/v2/produkty`
* **W nagłówkach**: `Accept: application/vnd.przyklad.v1+json`
* Zawsze dbaj o **jednolitość** i **czytelność**.
* Nawet przy wersjonowaniu w URL wciąż używaj `Accept` do negocjacji formatu danych.

## Wybór typów mediów i przetwarzanie treści

* **JSON** – najbardziej popularny, ale różne konwencje:

  * Collection+JSON (operacje na kolekcjach)
  * HAL (oddziela dane od linków)
  * Ion (opisuje zarówno dane, jak i metadane)
* Każdy format ma swoje zalety i ograniczenia – dobieraj do potrzeb projektu.

## Podejścia hypermedialne

* **Hypermedia** to łączenie różnych formatów (tekst, grafika, video) w sposób nieliniowy, jak „książka przygodowa”.
* REST API z HATEOAS umożliwia klientowi samodzielne odkrywanie ścieżek:

  1. Wejście przez stały punkt startowy (np. `/api/`)
  2. Otrzymanie odnośników do kolejnych zasobów i operacji
* Przykład: GitHub API zaczyna się od `/`, a dalej prowadzi linkami do repozytoriów, issue, pull requestów itd.


