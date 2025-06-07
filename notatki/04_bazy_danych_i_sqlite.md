
## Bazy danych

    Bazy danych to zorganizowane zbiory danych, które umożliwiają łatwe wyszukiwanie, przechowywanie i aktualizowanie informacji.
    Bazy danych służą do przechowywania różnych rodzajów informacji, takich jak informacje o produktach, klientach, zamówieniach, książkach, muzyce i wiele innych.

Rodzaje baz danych

    Relacyjne bazy danych (RDBMS) - najczęściej stosowane rodzaje baz danych, które korzystają z języka SQL do manipulowania danymi.
    Nierelacyjne bazy danych (NoSQL) - stosowane w przypadku dużej ilości danych, które nie mają ściśle określonej struktury.
    Bazy danych desktopowe - aplikacje, które umożliwiają tworzenie i zarządzanie prostymi bazami danych na poziomie jednego użytkownika.
    Bazy danych w chmurze - bazy danych dostępne przez internet, które są przechowywane na serwerach dostawcy usług chmurowych.

Podstawowe pojęcia

    Tabela - podstawowa struktura danych w relacyjnych bazach danych.
    Klucz główny - unikalny identyfikator rekordu w tabeli.
    Klucz obcy - wartość w tabeli, która odwołuje się do klucza głównego innej tabeli.
    Zapytania SQL - język programowania stosowany do tworzenia, modyfikowania i pobierania danych z bazy danych.

Przykłady zapytań SQL

    SELECT * FROM tabela - pobiera wszystkie rekordy z tabeli.
    SELECT kolumna1, kolumna2 FROM tabela WHERE warunek - pobiera wybrane kolumny z tabeli, które spełniają podany warunek.
    INSERT INTO tabela (kolumna1, kolumna2) VALUES (wartość1, wartość2) - dodaje nowy rekord do tabeli.
    UPDATE tabela SET kolumna = wartość WHERE warunek - aktualizuje istniejące rekordy w tabeli, które spełniają podany warunek.
    DELETE FROM tabela WHERE warunek - usuwa wybrane rekordy z tabeli, które spełniają podany warunek.

Normalizacja

    Normalizacja to proces projektowania baz danych, który ma na celu minimalizację redundancji danych i poprawienie struktury tabel.
    Normalizacja polega na dzieleniu dużych tabel na mniejsze i bardziej spójne pod względem danych.
    Proces normalizacji opiera się na szeregu reguł, zwanych postaciami normalnymi, które określają, jakie wymagania muszą być spełnione przez każdy schemat tabeli.

Postacie normalne

    1. postać normalna (1NF) - tabela jest w 1NF, jeśli każda jej kolumna zawiera tylko pojedynczą wartość, a każdy rekord jest unikalny i identyfikowalny za pomocą klucza głównego.
    2. postać normalna (2NF) - tabela jest w 2NF, jeśli spełnia wymagania 1NF i każda kolumna zależy bezpośrednio tylko od klucza głównego.
    3. postać normalna (3NF) - tabela jest w 3NF, jeśli spełnia wymagania 2NF i nie ma w niej zależności funkcyjnych między kolumnami, które nie są związane z kluczem głównym.
    Postać normalna Boyce'a-Codda (BCNF) - tabela jest w BCNF, jeśli spełnia wymagania 3NF i każda zależność funkcyjna w tabeli jest związana z kluczem głównym.
    
    
    Oto przykłady tabeli przed i po zastosowaniu kolejno 1NF, 2NF i 3NF:
1. Postać normalna (1NF)
Tabela przed normalizacją
ID	Imię i nazwisko	Telefon
1	Jan Kowalski	123-456-789
2	Anna Nowakowska	987-654-321
3	Janusz Kowalski	111-222-333, 444-555-666
Tabela po normalizacji (1NF)

Tabela po normalizacji zawiera dwie osobne kolumny dla numerów telefonów, co eliminuje powtarzające się wartości i poprawia strukturę tabeli.
ID	Imię i nazwisko	Telefon1	Telefon2
1	Jan Kowalski	123-456-789	
2	Anna Nowakowska	987-654-321	
3	Janusz Kowalski	111-222-333	444-555-666
2. Postać normalna (2NF)
Tabela przed normalizacją
Numer zamówienia	ID produktu	Nazwa produktu	Cena jednostkowa	Ilość sztuk
1	101	Książka	20,00 zł	2
1	102	Długopis	5,00 zł	3
2	103	Ołówek	1,50 zł	5
Tabela po normalizacji (2NF)

Tabela po normalizacji zawiera dwie osobne tabele dla zamówień i produktów, co eliminuje powtarzające się wartości i poprawia strukturę tabeli.
Tabela zamówień
Numer zamówienia	ID produktu	Ilość sztuk
1	101	2
1	102	3
2	103	5
Tabela produktów
ID produktu	Nazwa produktu	Cena jednostkowa
101	Książka	20,00 zł
102	Długopis	5,00 zł
103	Ołówek	1,50 zł

3. Postać normalna (3NF)
Tabela przed normalizacją
Numer zamówienia	Nazwa produktu	Kategoria produktu	Opis produktu	Cena jednostkowa	Ilość sztuk
1	Książka	Książki	Nowa książka	20,00 zł	2
1	Długopis	Ar			

Tabela po normalizacji (3NF)

Tabela po normalizacji zawiera trzy osobne tabele dla zamówień, produktów i kategorii produktów, co eliminuje powtarzające się wartości i poprawia strukturę tabeli.
Tabela zamówień
Numer zamówienia	ID produktu	Ilość sztuk
1	101	2
1	102	3
2	103	5
Tabela produktów
ID produktu	Nazwa produktu	Opis produktu	Cena jednostkowa	ID kategorii
101	Książka	Nowa książka	20,00 zł	1
102	Długopis	Czarny długopis	5,00 zł	2
103	Ołówek	Niebieski ołówek	1,50 zł	2
Tabela kategorii produktów
ID kategorii	Nazwa kategorii
1	Książki
2	Artykuły biurowe

Indeksowanie

    Indeksowanie to proces dodawania indeksów do tabel w celu przyspieszenia wyszukiwania i sortowania danych.
    Indeksy są specjalnymi strukturami danych, które umożliwiają szybsze wyszukiwanie danych poprzez tworzenie listy wskaźników do rekordów w tabeli.
    Indeksy mogą być tworzone dla jednej lub wielu kolumn w tabeli, w zależności od potrzeb.

Transakcje

    Transakcje to operacje wykonywane na bazie danych, które składają się z jednego lub więcej zapytań SQL.
    Transakcje są wykonywane w trybie atomowym, co oznacza, że ​​są wykonywane jako całość lub w ogóle nie są wykonywane.
    Transakcje zapewniają spójność i integralność danych poprzez uniemożliwienie jednoczesnego dostępu wielu użytkowników do tych samych danych.

Bezpieczeństwo i backup

    Bezpieczeństwo danych jest kluczowe dla każdej bazy danych.
    W celu zapewnienia bezpieczeństwa, bazy danych powinny być zabezpieczone za pomocą haseł, a dostęp do danych powinien być kontrolowany przez uprawnienia użytkowników.
    Backupy to kopia zapasowa bazy danych, która jest tworzona w celu odtworzenia danych w przypadku awarii lub utraty danych.
    Backup


# Architektura 3-warstwowa

## 1. Warstwa klienta (Warstwa prezentacji)
- Przeglądarka / Aplikacja desktopowa / Mobilna  
- Odpowiada za prezentację danych użytkownikowi  
- Często poprzedzona serwerem WWW (Apache, Nginx, httpd itp.)

```txt
[Klient] → [Webserver (Apache, Nginx, HTTPD)] → [App Server]
````

---

## 2. Warstwa aplikacji (Warstwa logiki biznesowej)

* **Aplikacja** napisana w:

  * Java, Python, C#, JavaScript/Node.js itp.
* **Serwer aplikacyjny** zawiera kod biznesowy
* Podstawowe elementy:

  * **System operacyjny**
  * **Sprzęt (hardware)**

```txt
+--------------------------------------+
|  Serwer aplikacyjny (Application)    |
|  — Java, Python, .NET, Node.js etc. |
|  — Zawiera logikę biznesową         |
|  — System operacyjny                |
|  — Sprzęt                           |
+--------------------------------------+
```

---

## 3. Warstwa bazy danych (Warstwa danych)

* **Serwer bazodanowy** obsługuje systemy RDBMS:

  * MySQL, Oracle, MS SQL Server itp.
* Przechowuje i udostępnia dane aplikacji
* Podstawowe elementy:

  * **System operacyjny**
  * **Sprzęt (hardware)**

```txt
+--------------------------------------+
|  Serwer bazy danych (Database)       |
|  — MySQL, Oracle, MSSQL itp.         |
|  — System operacyjny                |
|  — Sprzęt                           |
+--------------------------------------+
```

---

## Komunikacja w sieci

* Urządzenia wymieniają się danymi za pomocą:

  * **Adresu IP**
  * **Nazwy hosta**

Przykład:

```txt
[App Server] ⇄ [Database Server]
   ↕ IP / Hostname
```

---

> **Uwaga:**
>
> * Serwer WWW (np. Apache, Nginx) często działa jako „bramka” pomiędzy klientem a serwerem aplikacyjnym.
> * Każda z warstw może być fizycznie odseparowana na różnych maszynach lub instancjach w chmurze.

```





