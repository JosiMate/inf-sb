# Dokumentacja techniczna, czyli jak wykorzystać zaawansowane możliwości edytorów

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 17**

!!! abstract "O tym temacie"

    Tworzenie profesjonalnej dokumentacji technicznej, paszportów maszyn oraz rysunków wykonawczych i złożeniowych wymaga opanowania edytorów tekstu i grafiki wektorowej. W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się tworzyć rysunki złożeniowe, dodawać odnośniki i numerację pozycji, podpisować ilustracje i tabele oraz generować automatyczne spisy ilustracji i tabel.

!!! success "Kryteria sukcesu"

    Po tej lekcji:
    1. Wyjaśnię pojęcie i rolę rysunku złożeniowego (Assembly Drawing) w dokumentacji
    2. Wymienię cechy prawidłowo sporządzonej dokumentacji technicznej
    3. Utworzę proste schematy i rysunki wektorowe przy użyciu narzędzi rysunkowych (LibreOffice Draw, Word)
    4. Dodam i formatować odnośniki liczbowe (balony / pozycje) do elementów rysunku
    5. Wstawiać podpisy pod ilustracjami i rysunkami technycznymi (Captions)
    6. Wstawiać podpisy i numerację tabel (np. Tabela 1: Wykaz części)
    7. Generować automatyczny spis ilustracji oraz spis tabel w edytorze tekstu
    8. Zarządzę pozycjonowaniem i zakotwiczeniem rysunków w tekście (Anchor/Position)
    9. Utworzę tabele specyfikacji materiałowej (BOM - Bill of Materials)
    10. Zastosuję zasady zasad spójności i czytelności dokumentacji techniczno-ruchowej (DTR)

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Co to jest spad (bleed) w przygotowaniu dokumentu do druku?
    2. **Sprzed kilku tygodni.** Jaki model kolorów stosuje się w druku, a jaki na ekranie?
    3. **Z dawniejszych tematów.** Do czego służą linie pomocnicze (siatka) w układzie strony?

    ??? success "Odpowiedzi"

        1. Obszar drukowany poza krawędzią czystego formatu, zapobiegający białym brzegom po przycięciu papieru.
        2. W druku stosuje się model CMYK, a na ekranie RGB.
        3. Pomagają równo wyrównać i rozmieścić elementy tekstowe i graficzne na stronie.

## 1. Wprowadzenie do Dokumentacji Techniczno-Ruchowej (DTR)

Każde urządzenie, maszyna czy konstrukcja dostarczana do klienta lub stosowana w zakładzie musi posiadać **dokumentację techniczną**. Kluczowym elementem tej dokumentacji jest **rysunek złożeniowy**, pokazujący jak poszczególne części składowe łączą się w całość.

```
+-----------------------------------------------------------------------+
|  ELEMENTY DOKUMENTACJI TECHNICZNEJ                                    |
|  - Rysunek Złożeniowy (z odnośnikami 1, 2, 3...)                      |
|  - Tabela Zestawieniowa (BOM: Nr, Nazwa części, Ilość, Materiał)      |
|  - Podpisy Pod Ilustracjami ("Rysunek 1: Rzut izometryczny...")      |
|  - Automatyczny Spis Ilustracji i Tabel                               |
+-----------------------------------------------------------------------+
```

### Cechy dobrej dokumentacji technicznej:

- **Jednoznaczność:** Każda część ma przypisany unikalny numer pozycji.
- **Kompletność:** Zawiera specyfikację wszystkich elementów (śruby, uszczelki, korpus).
- **Czytelność:** Rysunki i tabele są ponumerowane i podpisane zgodnie z normą.

---

## 2. Tworzenie rysunku złożeniowego i tabeli BOM

Rysunek złożeniowy składa się z widoku zespołu oraz **odnośników** (linii zakończonych grotem lub kropką z numerem pozycji).

| Element | Do czego służy | Jak wstawić |
| --- | --- | --- |
| **Odnośnik / Balon** | Wskazuje konkretną część na rysunku złożeniowym | *Kształty -> Objaśnienia / Kształty wektorowe* |
| **Tabela BOM (Bill of Materials)** | Wykaz wszystkich części potrzebnych do zmontowania | *Wstaw -> Tabela (Lp., Nazwa, Ilość, Normy)* |
| **Podpis ilustracji (Caption)** | Automatycznie ponumerowany podpis pod rysunkiem | *Prawy przycisk na rysunku -> Wstaw podpis* |

!!! info "Co to jest tabela BOM?"

    BOM (*Bill of Materials*) to tabela zestawieniowa materiałów i części. Jest podstawą dla działu zaopatrzenia i produkcji – bez niej nie da się zamówić odpowiednich komponentów do montażu.

---

## 3. Automatyzacja: Podpisy i Spisy Ilustracji

Ręczne wpisywanie numerów rysunków (np. „Rysunek 1”, „Rysunek 2”) to częsty błąd. Usunięcie jednego rysunku wymagałoby przenumerowania całego dokumentu!

```
Rysunek / Tabela -> Prawy Przycisk -> Wstaw Podpis -> Automatyczny Numer -> Spis Ilustracji
```

### Zalety automatycznych podpisów:

- **Auto-numeracja:** Edytor sam dba o kolejność numerów rysunków i tabel.
- **Odsyłacze krzyżowe:** W tekście możesz napisać „patrz Rysunek 3”, a numer zaktualizuje się sam.
- **Spis ilustracji:** Jednym kliknięciem generujesz wykaz wszystkich rysunków z numerami stron na końcu dokumentu.

!!! tip "Zakotwiczenie rysunku w tekście"

    Rysunek w dokumencie technicznym warto zakotwiczyć *Do akapitu* lub *Jako znak*. Zapobiega to przypadkowemu „rozjeżdżaniu się” ilustracji i podpisów podczas dopisywania tekstu.

---

## 4. Instrukcja krok po kroku: Przygotowanie specyfikacji technicznej zespołu

1. **Krok 1:** Otwórz edytor tekstu (Word lub LibreOffice Writer) i wstaw rysunek złożeniowy (*Wstaw -> Obraz*).
2. **Krok 2:** Wybierz z paska kształtów narzędzie *Objaśnienie (Callout)* lub strzałkę z kołkiem i dodaj odnośniki z numerami `1`, `2`, `3` wskazujące części na rysunku.
3. **Krok 3:** Kliknij prawym przyciskiem myszy na rysunek i wybierz *Wstaw podpis (Insert Caption)*.
4. **Krok 4:** Wybierz etykietę *Rysunek*, wpisz tytuł: „Rysunek złożeniowy zespołu napędowego” i kliknij *OK*.
5. **Krok 5:** Poniżej wstaw tabelę zestawieniową (BOM) z kolumnami: *Nr pozycji, Nazwa części, Ilość, Materiał*.
6. **Krok 6:** Kliknij prawym przyciskiem myszy na tabelę, wybierz *Wstaw podpis*, zmień etykietę na *Tabela* i wpisz: „Tabela 1: Wykaz części składowych”.
7. **Krok 7:** Przejdź na koniec dokumentu, stwórz sekcję *Załączniki*.
8. **Krok 8:** Wybierz z menu *Odwołania -> Wstaw spis ilustracji* i zatwierdź.
9. **Krok 9:** Wybierz *Odwołania -> Wstaw spis tabel* i zatwierdź.
10. **Krok 10:** Wyeksportuj kompletną dokumentację do pliku PDF.

!!! warning "Unikaj rysowania odnośników w osobnym programie!"

    Jeśli nakładasz numery pozycji na rysunek, zgrupuj wszystkie strzałki i cyfry z obrazkiem (*Zgrupuj*), aby przy przesunięciu akapitu odnośniki nie przesunęły się w puste miejsce.

---

## Podsumowanie

Zaawansowane możliwości edytorów tekstu umożliwiają sprawne tworzenie profesjonalnej dokumentacji technicznej. Korzystanie z rysunków złożeniowych, odnośników, tabel BOM oraz automatycznych podpisów i spisów ilustracji eliminuje błędy w numeracji i zapewnia zgodność ze standardami przemysłowymi.

---

## Ćwiczenia

!!! note "Ćwiczenie 1 (Podstawowe):"

    Wstaw obraz do dokumentu, użyj funkcji *Wstaw podpis* i sprawdź, czy dodanie drugiego obrazka powyżej automatycznie zmieni numerację.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 2 (Średnio zaawansowane):"

    Utwórz proste schematyczne rysunki wektorowe w edytorze i nałóż na nie 3 odnośniki z numerami pozycji. Zgrupuj obiekty.

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 3 (Branżowe):"

    Przygotuj kartę techniczną wyrobu/maszyny ze swojego zawodu. Zamieść rysunek, tabelę parametrów technicznych oraz tabelę zestawieniową części (BOM).

??? tip "Podpowiedź 1"

    Kierunek: zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: zapoznaj się z odpowiednią sekcją w treści lekcji, gdzie opisano niezbędną funkcję/polecenie krok po kroku.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: przetestuj poszczególne opcje w programie i upewnij się, że efekt końcowy zgadza się z wymaganiami w karcie pracy.


!!! note "Ćwiczenie 4 (Zaawansowane):"

    Stwórz 3-stronicową dokumentację techniczną zawierającą co najmniej 3 rysunki z odnośnikami, 2 tabele specyfikacji oraz wygenerowany automatyczny spis ilustracji i spis tabel.

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
    "pytanie": "Czym jest rysunek złożeniowy w dokumentacji technicznej?",
    "opcje": [
      "Plakatem promocyjnym do zawieszenia na ścianie",
      "Rysunkiem przedstawiającym zespół maszynowy wraz ze wszystkimi częściami składowymi wskazanymi odnośnikami",
      "Zdjęciem z imprezy zakładowej",
      "Rysunkiem wykonanym kredkami"
    ],
    "poprawna": 1,
    "wyjasnienie": "Rysunek złożeniowy pokazuje sposób montażu i wzajemne położenie części tworzących dany zespół."
  },
  {
    "pytanie": "Co oznacza skrót BOM w kontekście dokumentacji technicznej?",
    "opcje": [
      "Baza Ochrony Maszyn",
      "Bill of Materials (Specyfikacja / Tabela zestawieniowa materiałów i części)",
      "Brak Odpowiednich Materiałów",
      "Biuro Obsługi Magazynu"
    ],
    "poprawna": 1,
    "wyjasnienie": "BOM (Bill of Materials) to tabela zawierająca kompletny wykaz części, komponentów i surowców potrzebnych do wytworzenia produktu."
  },
  {
    "pytanie": "Jaka jest główna korzyść ze korzystania z funkcji 'Wstaw podpis' (Caption) zamiast wpisywania tekstu ręcznie pod obrazkiem?",
    "opcje": [
      "Ręczny napis się zamazuje",
      "Edytor automatycznie numeruje ilustracje i umożliwia wygenerowanie automatycznego Spisu Ilustracji",
      "Zdjęcie zmienia kolor na czarno-biały",
      "Dokument zajmuje mniej miejsca na dysku"
    ],
    "poprawna": 1,
    "wyjasnienie": "Automatyczne podpisy pilnują poprawnej kolejności numerów rysunków i stanowią źródło dla automatycznych spisów ilustracji."
  },
  {
    "pytanie": "Po co grupuje się elementy wektorowe (np. strzałki odnośników) z obrazkiem w dokumencie?",
    "opcje": [
      "Aby uniemożliwić ich wydrukowanie",
      "Aby przy przesuwaniu tekstu lub obrazka odnośniki nie przemieściły się w niepożądane miejsce",
      "Aby skasować wszystkie podpisy",
      "Nie ma takiej potrzeby"
    ],
    "poprawna": 1,
    "wyjasnienie": "Grupowanie łączy obraz i strzałki odnośników w jeden obiekt, dzięki czemu zachowują swoje wzajemne położenie."
  },
  {
    "pytanie": "Gdzie w menu edytora MS Word / Writer znajduje się funkcja generowania Spisu Ilustracji?",
    "opcje": [
      "W zakładce Odwołania (References)",
      "W zakładce Widok (View)",
      "W menu Plik -> Drukuj",
      "W oknie kalkulatora"
    ],
    "poprawna": 0,
    "wyjasnienie": "Wszystkie funkcje spisu treści, spisów ilustracji i indeksów znajdują się w zakładce Odwołania (References)."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na MS Word / LibreOffice Writer dla Szkół Branżowych.*
