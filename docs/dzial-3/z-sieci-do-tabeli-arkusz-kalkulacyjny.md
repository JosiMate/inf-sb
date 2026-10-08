# Z sieci do tabeli, czyli jak interpretować dane w arkuszu kalkulacyjnym

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 18**

!!! abstract "O tym temacie"

    Pozyskiwanie, importowanie i interpretowanie danych gospodarczych oraz branżowych ze źródeł internetowych (np. GUS, urzędy pracy, portale branżowe) to kluczowa umiejętność w analizie rynku. W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się pobierać dane tabelaryczne ze stron WWW, czyścić i formatować dane w arkuszu kalkulacyjnym, używać funkcji statystycznych oraz budować czytelne kosztorysy i wykresy analityczne.

!!! success "Kryteria sukcesu"

    Po tej lekcji:
    1. Zidentyfikuję oficjalne źródła danych statystycznych i gospodarczych (GUS - stat.gov.pl, Eurostat, CEIDG)
    2. Zaimportuję tabele z witryn internetowych do arkusza kalkulacyjnego (Excel / Calc)
    3. Oczyszczę zaimportowane dane (usuwanie zbędnych spacji, zmiana separatora dziesiętnego)
    4. Skonwertuję dane tekstowe na wartości liczbowe oraz formatować waluty i procenty
    5. Zastosuję serie danych i mechanizm automatycznego wypełniania komórek (AutoFill)
    6. Wykonywać obliczenia przy użyciu podstawowych funkcji (`SUMA`, `ŚREDNIA`, `MIN`, `MAKS`)
    7. Utworzę prosty kosztorys materiałowy i robocizny w arkuszu kalkulacyjnym
    8. Dobiorę i utworzę wykresy do wizualizacji importowanych danych statystycznych
    9. Zinterpretuję wyniki oraz wyciągnę wnioski na podstawie analizy tabelarycznej
    10. Wyeksportuję i udostępnię arkusz w formacie XLSX lub PDF

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Do czego służą sekcje i podziały stron w długich dokumentach technicznych?
    2. **Sprzed kilku tygodni.** Jak dodać automatyczną numerację stron od drugiej strony dokumentu?
    3. **Z dawniejszych tematów.** Czym jest szablon dokumentu (.dotx / .ott)?

    ??? success "Odpowiedzi"

        1. Pozwalają zmieniać nagłówki, stopki, orientację stron (pionowa/pozioma) i numerację w różnych częściach dokumentu.
        2. Wstawiając podział sekcji i wyłączając opcję „Połącz z poprzednim” w nagłówku/stopce nowej sekcji.
        3. Gotowy wzorzec dokumentu ze zdefiniowanymi stylami, układem i elementami stałymi.

## 1. Źródła danych w sieci i sposoby ich importu

W codziennej pracy przedsiębiorca lub pracownik musi śledzić wskaźniki gospodarcze: ceny surowców, stopy inflacji, minimalne wynagrodzenie czy przeciętne koszty materiałów.

```
+-----------------------------------------------------------------------+
|  ŹRÓDŁO DANYCH (Strona WWW / GUS) --> IMPORT / KOPIOWANIE           |
|                                       v                               |
|  ARKUSZ KALKULACYJNY (Czyszczenie i konwersja separatorów)           |
|                                       v                               |
|  FORMUŁY I FUNKCJE (SUMA, ŚREDNIA) --> KOSZTORYS / WYKRES ANALITYCZNY |
+-----------------------------------------------------------------------+
```

### Najważniejsze państwowe i branżowe portale danych:

- **Główny Urząd Statystyczny (`stat.gov.pl` / Bank Danych Lokalnych):** Dane o cenach, zatrudnieniu, produkcji.
- **Portal Dane.gov.pl:** Otwarte dane publiczne z różnych sektorów gospodarki.
- **NBP (`nbp.pl`):** Aktualne i archiwalne kursy walut.

---

## 2. Czyszczenie i konwersja danych po imporcie

Częstym problemem przy wklejaniu danych ze strony WWW jest sytuacja, w której arkusz traktuje liczby jako **tekst** (np. z powodu użycia kropki zamiast przecinka jako separatora dziesiętnego).

| Problem po wklejeniu | Przyczyna | Rozwiązanie |
| --- | --- | --- |
| **Liczby wyrównane do lewej** | Arkusz traktuje je jako tekst | Użyj opcji *Znajdź i zamień* (`.` na `,`) |
| **Nierozpoznane twarde spacje** | Spacja jako separator tysięcy | Zamień spaki na brak znaku |
| **Brak symbolu waluty** | Surowy ciąg cyfr | Zastosuj *Formatowanie komórek -> Walutowe* |

!!! info "Szybki test: liczba czy tekst?"

    W arkuszu kalkulacyjnym domyślnie **tekst wyrównuje się do lewej krawędzi komórki**, a **liczby wyrównują się do prawej krawędzi**. Jeśli Twoje wpisane kwoty stoją po lewej stronie — arkusz nie wykona na nich formuł matematycznych!

---

## 3. Praca na funkcjach i budowa kosztorysu

Po przygotowaniu tabeli przechodzimy do wyliczeń z wykorzystaniem podstawowych funkcji arkusza.

```
SUMA(A1:A10)    --> Oblicza łączną wartość z zakresu
ŚREDNIA(B1:B10) --> Oblicza średnią arytmetyczną
MIN(C1:C10)     --> Wyznacza wartość najmniejszą
MAKS(C1:C10)    --> Wyznacza wartość największą
```

### Struktura prostego kosztorysu branżowego:

1. **Lp. / Nazwa pozycji / Jednostka miary / Ilość / Cena jednostkowa netto.**
2. **Wartość netto:** Formuła `= Ilość * Cena_jednostkowa` (np. `=C2*D2`).
3. **Wartość brutto:** Formuła `= Wartość_netto * 1,23` (dla stawki VAT 23%).
4. **Podsumowanie (SUMA):** Formuła `=SUMA(E2:E10)` w komórce RAZEM.

!!! tip "Automatyczne wypełnianie (AutoFill)"

    Przeciągnięcie małego kwadracika w prawym dolnym rogu zaznaczonej komórki (uchwyt wypełniania) kopiuje formułę do niższych wierszy, automatycznie dostosowując adresy komórek.

---

## 4. Instrukcja krok po kroku: Pobieranie danych GUS i przygotowanie kosztorysu

1. **Krok 1:** Wejdź na stronę `stat.gov.pl` lub portal z kursami walut `nbp.pl`.
2. **Krok 2:** Zaznacz tabelę z danymi na stronie, skopiuj ją (`Ctrl + C`).
3. **Krok 3:** Otwórz arkusz kalkulacyjny i wklej dane (*Wklej specjalnie -> Tekst bez formatowania*).
4. **Krok 4:** Jeśli ceny mają kropki, użyj skrótu `Ctrl + H` (Znajdź i zamień) i zamień wszystkie `.` na `,`.
5. **Krok 5:** Sformatuj kolumnę z cenami jako *Format walutowy (PLN)*.
6. **Krok 6:** Dodaj kolumnę *Ilość* i wpisz zapotrzebowanie materiałowe dla wybranego projektu.
7. **Krok 7:** W kolumnie *Wartość* wpisz formułę `=C2*D2` i przeciągnij ją w dół.
8. **Krok 8:** W dolnym wierszu oblicz sumę całkowitą za pomocą funkcji `=SUMA(E2:E10)`.
9. **Krok 9:** Zaznacz nazwy pozycji i ich wartości, a następnie wstaw *Wykres kolumnowy*.
10. **Krok 10:** Zapisz plik pod nazwą `analiza_kosztow.xlsx`.

!!! warning "Uwaga na błąd #ARG! (#VALUE!)"

    Błąd `#ARG!` pojawia się wtedy, gdy w formule próbujesz pomnożyć komórkę zawierającą tekst przez liczbę. Sprawdź, czy zaimportowane ceny na pewno są liczbami!

---

## Podsumowanie

Pobieranie danych z sieci i ich interpretacja w arkuszu kalkulacyjnym to podstawowe narzędzie w zarządzaniu finansami i planowaniu produkcji. Umiejętność czyszczenia importowanych tabel, stosowania formatu walutowego oraz funkcji SUMA i ŚREDNIA pozwala na błyskawiczne tworzenie wycen i kosztorysów.

---

## Ćwiczenia

!!! note "Ćwiczenie 1 (Podstawowe):"

    Skopiuj prostą tabelę z cenami paliw lub materiałów ze strony internetowej do arkusza. Zamień ewentualne kropki na przecinki i nadaj kolumnie format walutowy.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 2 (Średnio zaawansowane):"

    Utwórz arkusz z cenami 5 surowców/części. Użyj funkcji `SUMA`, `ŚREDNIA`, `MIN` i `MAKS` do analizy ich wartości.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 3 (Branżowe):"

    Pobierz z sieci aktualny cennik materiałów potrzebnych w Twoim zawodzie i przygotuj kosztorys wykonania konkretnej usługi dla klienta z uwzględnieniem narzutu robocizny.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 4 (Zaawansowane):"

    Zaimportuj tabelę danych statystycznych GUS dotyczących zatrudnienia lub produkcji, przelicz wartości procentowe i sporządź wykres kołowy z etykietami danych.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Dlaczego po wklejeniu tabeli ze strony WWW liczby ułożone po lewej stronie komórki nie chcą się sumować?",
    "opcje": [
      "Arkusz kalkulacyjny traktuje je jako tekst (np. przez kropkę zamiast przecinka)",
      "Komputer ma za mało pamięci RAM",
      "Monitor jest źle podłączony",
      "Trzeba włączyć kalkulator"
    ],
    "poprawna": 0,
    "wyjasnienie": "Liczby wyrównane do lewej są traktowane przez arkusz jako ciągi tekstowe – należy zamienić kropki na przecinki."
  },
  {
    "pytanie": "Która funkcja arkusza kalkulacyjnego służy do obliczania łącznej sumy z podanego zakresu komórek?",
    "opcje": [
      "=ŚREDNIA()",
      "=SUMA()",
      "=ILE.LICZB()",
      "=POŁĄCZ()"
    ],
    "poprawna": 1,
    "wyjasnienie": "Funkcja =SUMA(zakres) dodaje do siebie wszystkie wartości liczbowe znajdujące się w zaznaczonych komórkach."
  },
  {
    "pytanie": "Co to jest uchwyt wypełniania (AutoFill) w arkuszu kalkulacyjnym?",
    "opcje": [
      "Przycisk do włączania drukarki",
      "Mały kwadracik w prawym dolnym rogu zaznaczonej komórki służący do kopiowania formuł i serii danych",
      "Narzędzie do rysowania kółek",
      "Plik instalacyjny programu"
    ],
    "poprawna": 1,
    "wyjasnienie": "Uchwyt wypełniania pozwala szybko skopiować wzór formuły na sąsiednie komórki."
  },
  {
    "pytanie": "Główny Urząd Statystyczny (GUS) publikuje oficjalne dane na stronie:",
    "opcje": [
      "stat.gov.pl",
      "youtube.com",
      "wikipedia.org",
      "facebook.com"
    ],
    "poprawna": 0,
    "wyjasnienie": "Oficjalnym portalem Głównego Urzędu Statystycznego jest serwis stat.gov.pl."
  },
  {
    "pytanie": "Jaka formuła prawidłowo oblicza wartość brutto z komórki A2 (przy stawce VAT 23%)?",
    "opcje": [
      "=A2 * 1,23",
      "=A2 + 23",
      "=A2 / 100",
      "=SUMA(23)"
    ],
    "poprawna": 0,
    "wyjasnienie": "Pomnożenie kwoty netto przez 1,23 dodaje do niej 23% podatku VAT, dając kwotę brutto."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na MS Excel / LibreOffice Calc dla Szkół Branżowych.*
