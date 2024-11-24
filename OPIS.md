## Projekt - Bazy danych
*Grupa 2*<br>
*Radosław Szepielak, Paweł Saltarius, Paweł Gadomski*

# Opis systemu
**Aktorzy:** klient, administrator, zewnętrzny system płatności

System będzie się składał z dwóch głównych sekcji: Sekcja użytkownika i sekcja administratora.

# Sekcja użytkownika

W sekcji użytkownika będzie znajdowały się wszystkie dostępne dla klientów funkcje oraz informacje. Aby wejść do panelu użytkownika należy się zalogować/zarejestrować na konto użytkownika. Użytkownik będzie miał dostęp do trzech usług:

1. ### Webinary
    - Zapisy na nadchodzące webinary (przy płatnych webinarach płatność zewnętrznym systemem). Informacje o poszczególnych webinarach to: data, czas trwania, tytuł, opis, język, koszt, grafika, platforma spotkania oraz przycisk do zapisów.
    - Nagrania z ostatnich webinarów (webinary na które byliśmy zapisani + dodatkowa zakładka na darmowe webinary na które nie byliśmy zapisani). Wyświetlana jest też data kiedy stracimy do nich dostęp.
    - Nadchodzące webinary na które jesteśmy zapisani (data, informacje, link do spotkania).
2. ### Kursy
    - Zapisy na dostępne kursy w następujących formach: 
        - Stacjonarne, odbywają się w wyznaczonej sali i są zaliczane na podstawie obecności, mają ustalony limit miejsc.
        - on-line synchroniczne, wymagają uczestnictwa w wydarzeniach na żywo na platformie do webinarów, nagrania są przechowywane w zewnętrznym systemie, a linki do nich udostępniane uczestnikowi, brak limitu miejsc
        - on-line asynchroniczne, zaliczenie odbywa się po obejrzeniu materiałów (automatyczna weryfikacja), na podstawie obecności, nagrania są przechowywane w zewnętrznym systemie, a linki do nich udostępniane uczestnikowi, brak limitu miejsc
        - hybrydowe, łączą podejście on-line i stacjonarne, mają ustalony limit miejsc
3. ### Studia