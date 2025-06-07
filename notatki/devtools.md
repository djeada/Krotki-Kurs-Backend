

1. **Wprowadzenie**
   - Wideo koncentruje się na zrozumieniu zakładki sieciowej w DevTools, przydatnej w rozwoju backendu i frontendu.

2. **Dostęp do Zakładki Sieciowej**
   - Dostępna w Chrome i Firefox przez menu (trzy kropki > Więcej narzędzi > Narzędzia deweloperskie > Sieć).

3. **Pola w Zakładce Sieciowej**
   - **Nazwa:** Żądany zasób.
   - **Metoda:** Używana metoda HTTP (np. GET).
   - **Status:** Status odpowiedzi z serwera (np. 200 oznacza sukces).
   - **Protokół:** Protokół komunikacyjny (np. HTTP/1.1, HTTP/2, HTTP/3).
   - **Schemat:** Wskazuje, czy połączenie jest zabezpieczone (HTTP vs. HTTPS).
   - **Adres zdalny:** Adres IP serwera i port.
   - **Typ:** Typ zasobu (np. dokument, obraz).
   - **Inicjator:** Identyfikuje źródło żądania.
   - **Rozmiar:** Rozmiar odpowiedzi.
   - **Czas:** Czas trwania żądania.
   - **ID połączenia:** Identyfikuje połączenie TCP.

Example.org
Apache.org
5. **Kluczowe Spostrzeżenia**
   - HTTP/1.1 wymaga wielu połączeń TCP, ograniczając liczbę równoległych żądań.
   - HTTP/2 pozwala na wiele żądań przez jedno połączenie TCP, poprawiając wydajność.
   - HTTP/3 używa UDP, zapewniając szybsze i bardziej bezpieczne połączenia, ale z innymi szczegółami implementacyjnymi.

6. **Śledzenie i Reklamy**
   - Żądania do usług zewnętrznych (Google Tag Manager, Google Analytics, Facebook) w celu śledzenia.
   - Ważność bezpiecznych połączeń (HTTPS) w celu zapobiegania przechwytywaniu danych.

7. **Wskazówki Dotyczące Wydajności i Bezpieczeństwa**
   - Unikaj mieszania treści (HTTP i HTTPS), aby zapobiec zagrożeniom bezpieczeństwa i poprawić wydajność.
   - Optymalizuj strony internetowe, redukując niepotrzebne przekierowania.
