
Object-Relational Mapping ORM – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych (lub inny element systemu) o relacyjnym charakterze. Implementacja takiego odwzorowania stosowana jest m.in. w przypadku, gdy tworzony system oparty jest na podejściu obiektowym, a system bazy danych operuje na relacjach. Ułatwia to programistom pracę z bazą danych, często odbywa się to jednak kosztem wydajności zapytań do bazy danych. Największą zaletą ORM jest prostota użytkowania.

Przykładowo, aby zmienić hasło użytkownika w bazie danych użytkowników musimy wykonać poniższą operację:

public void changePassword(User u, String newPassword) {
        con.prepareStatement(„UPDATE tab_users SET password = ? WHERE login = ?”).
        setString(1, u.getPassword()).
        setString(2, u.getLogin()).execute();
}

Chcielibyśmy, aby taka operacja wyglądała następująco:

public void changePassword(User u, String newPassword) {
      u.setPassword(newPassword);
}

a więc bez konieczności „grzebania” w relacyjnej bazie danych.

Najbardziej popularną implementacją idei ORM dla javy jest Hibernate.

Elementy technologii ORM :
    API (Application Programming Interface), czyli Interfejs programowania aplikacji) do zarządzania trwałością obiektów

    Mechanizm specyfikowania metadanych opisujących odwzorowanie klas na relacje w bazach danych

    Język lub API do wykonywania zapytań.

Praca z ORM:

    Tworzymy model danych w obiektowym języku programowania.

    Tworzymy schemat bazy danych odpowiadający temu modelowi (może się oczywiście okazać, że już mamy jakąś bazę danych, z którą musimy współpracować).

    Definiujemy odwzorowanie bazy danych na model relacyjny. Tworzymy aplikację obiektową operującą na modelu obiektowym (tworząc kod aplikacji w zasadzie nie musimy się zastanawiać jak nasze obiekty zostaną zapisane).

    W razie konieczności pobrania obiektów z bazy danych, bądź utrwalenia jakiegoś nowo utworzonego obiektu, czy też usunięcia utrwalonego obiektu posługujemy się odpowiednim API danego narzędzia ORM.
