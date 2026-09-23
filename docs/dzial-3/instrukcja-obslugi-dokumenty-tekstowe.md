# Instrukcja obsługi, czyli tworzymy zaawansowane dokumenty tekstowe

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 15**

!!! abstract "O tym temacie"

    Tworzenie czytelnej instrukcji obsługi, instrukcji stanowiskowej BHP czy procedury serwisowej wymaga opanowania zaawansowanych funkcji edytorów tekstu (Word, LibreOffice Writer). W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się stosować style akapitowe, układy wielokolumnowe, podziały sekcji, automatyczne spisy treści oraz wypunktowania procedur technicznych.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie konspektu i struktury nagłówków w zaawansowanym dokumencie
    2. stosować i modyfikować wbudowane style akapitowe (Nagłówek 1, Nagłówek 2, Tekst podstawowy)
    3. tworzyć i formatować automatyczny spis treści na podstawie użytych stylów
    4. dzielić dokument na sekcje (zastępując prosty podział strony)
    5. stosować wielokolumnowy układ tekstu dla instrukcji i ostrzeżeń
    6. wstawiać i edytować nagłówki oraz stopki odmienne dla różnych sekcji
    7. formatować wielopoziomowe listy numerowane i punktowane dla procedur krok po kroku
    8. wstawiać ramki ostrzegawcze (alerty) oraz symbole techniczne
    9. operować wglądem struktury dokumentu (Panel Nawigacji / Konspekt)
    10. eksportować gotową instrukcję do nieedytowalnego formatu PDF

## 1. Struktura i rola stylów w dokumencie technicznym

Dobrze przygotowana instrukcja obsługi musi być przejrzysta i przewidywalna. Czytelnik lub pracownik na stanowisku musi w kilka sekund odnaleźć poszukiwaną procedurę lub ostrzeżenie BHP.

```
+-----------------------------------------------------------------------+
|  STRUKTURA DOKUMENTU TEKSTOWEGO                                       |
|  - Nagłówek 1  --> Tytuł Rozdziału (np. 1. Bezpieczeństwo)            |
|  - Nagłówek 2  --> Podrozdział (np. 1.1 Środki Ochrony Indywidualnej) |
|  - Tekst Podst.-> Treść właściwa, opisy                               |
|  - Listy / Akapity -> Procedury krok po kroku                         |
+-----------------------------------------------------------------------+
```

### Dlaczego stosujemy STYLE zamiast ręcznego formatowania?

- **Spójność wyglądu:** Wszystkie nagłówki tego samego poziomu wyglądają identycznie w całym dokumencie.
- **Automatyzacja:** Pozwala na wygenerowanie **Automatycznego Spisu Treści** jednym kliknięciem.
- **Nawigacja:** Umożliwia szybkie przemieszczanie się po rozdziałach w *Panelu Nawigacji*.
- **Błyskawiczne zmiany:** Zmiana czcionki w stylu *Nagłówek 1* automatycznie aktualizuje cały, 50-stronicowy dokument.

---

## 2. Sekcje, kolumny i numery stron

Standardowy dokument traktuje wszystkie strony jednakowo. W instrukcji technicznej często potrzebujemy, aby strona tytułowa nie miała numeru, a wykaz procedur był ułożony w dwóch kolumnach.

| Element | Do czego służy | Jak wstawić (Word / Writer) |
| --- | --- | --- |
| **Podział sekcji (Section Break)** | Dzieli dokument na niezależne formatowanie (np. nagłówków/stopek) | *Układ -> Podziały -> Sekcja (od następnej strony)* |
| **Kolumny (Columns)** | Dzieli wyselekcjonowany tekst na 2 lub 3 szpalty | *Układ -> Kolumny -> Dwie* |
| **Automatyczny Spis Treści** | Generuje wykaz rozdziałów wraz z numerami stron | *Odwołania -> Spis treści* |
| **Odłącz od poprzedniego** | Odłącza nagłówek/stopkę sekcji od sekcji wcześniejszej | *Nagłówek i Stopka -> Link to Previous (Odłącz)* |

!!! info "Różnica między podziałem strony a podziałem sekcji"

    Prosty *Podział strony* (`Ctrl + Enter`) przesuwa tekst na nową kartę, ale zachowuje te same marginesy, układ i stopkę. *Podział sekcji* tworzy nową „wyspę”, na której możesz zmienić orientację strony na poziomą, zmienić marginesy czy wyłączyć numerację.

---

## 3. Procedury krok po kroku i ostrzeżenia

Procedury obsługi i naprawy muszą być zapisane w postaci uporządkowanych list wielopoziomowych.

```
1. Przygotowanie stanowiska
   1.1. Włącz zasilanie główne.
   1.2. Sprawdź osłony ochronne.
2. Uruchomienie urządzenia
   2.1. Wciśnij przycisk START.
```

### Elementy graficzne w instrukcjach:

- **Listy wielopoziomowe:** Pozwalają zachować hierarchię czynności.
- **Tabelki ostrzegawcze:** Użycie jednokomórkowych tabel ze scalonym obramowaniem i tłem (np. żółtym dla OSTRZEŻENIA, czerwonym dla NIEBEZPIECZEŃSTWA).
- **Symbole techniczne:** Wstawianie znaków specjalnych (`Insert -> Symbol`), np. $\Omega$, $\degree\text{C}$, $\pm$.

!!! tip "Automatyczny spis treści po zmianach"

    Jeśli dopiszesz nową treść lub zmienisz nagłówki, spis treści nie zaktualizuje się sam w tle. Kliknij prawym przyciskiem myszy na spis treści i wybierz *Aktualizuj pole -> Aktualizuj cały spis*.

---

## 4. Instrukcja krok po kroku: Tworzenie instrukcji stanowiskowej BHP

1. **Krok 1:** Otwórz nowy dokument w edytorze tekstu.
2. **Krok 2:** Wpisz tytuł: „INSTRUKCJA STANOWISKOWA BHP - OBSŁUGA SZLIFIERKI” i zastosuj styl *Tytuł*.
3. **Krok 3:** Wstaw podział sekcji na następną stronę (*Układ -> Podziały -> Sekcja (od następnej strony)*).
4. **Krok 4:** Przejdź do sekcji 2, przejdź do stopki, odznacz opcję *Połącz z poprzednim* i wstaw numerację stron.
5. **Krok 5:** Wpisz nagłówek: „1. Zasady ogólne” i nadaj mu styl *Nagłówek 1*.
6. **Krok 6:** Wpisz nagłówek: „2. Czynności przed rozpoczęciem pracy” (*Nagłówek 1*).
7. **Krok 7:** Pod nagłówkiem 2 utwórz listę numerowaną czynności (np. sprawdzenie przewodu, założenie okularów ochronnych).
8. **Krok 8:** Wstaw jednokomórkową tabelę z żółtym tłem i pogrubionym tekstem: „UWAGA: Zabrania się pracy bez osłony tarczy!”.
9. **Krok 9:** Przejdź na początek dokumentu (strona 1) i wybierz *Odwołania -> Spis treści -> Automatyczny spis treści*.
10. **Krok 10:** Wyeksportuj dokument do formatu PDF (*Plik -> Eksportuj -> Utwórz dokument PDF*).

!!! warning "Unikaj pętli ręcznych spacji!"

    Nigdy nie wyrównuj tekstu ani nie przesuwaj go do prawej krawędzi za pomocą wielokrotnego wciskania spacji! Używaj tabulatorów, wyrównania akapitu lub wcięć na linijce.

---

## Podsumowanie

Tworzenie zaawansowanych dokumentów tekstowych w pracy zawodowej opiera się na koncepcji stylów, sekcji i automatyzacji. Zastosowanie nagłówków, układu dwukolumnowego oraz automatycznego spisu treści gwarantuje profesjonalny wygląd instrukcji obsługi.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Przygotuj jednostronicowy dokument zawierający trzy nagłówki pierwszego stopnia oraz skompletowaną listę wielopoziomową. Zastosuj wbudowane style.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Utwórz dokument złożony z dwóch sekcji. Pierwsza sekcja (strona tytułowa) nie może posiadać numeru strony, natomiast druga sekcja musi zaczynać się od numeru 1.
3. **Ćwiczenie 3 (Branżowe):** Opracuj dwustronicową instrukcję stanowiskową BHP dla wybranego urządzenia z Twojego zawodu (np. obrabiarek, podnośnika, pieca konwekcyjnego). Użyj tabel ostrzegawczych oraz podziału tekstu na dwie kolumny.
4. **Ćwiczenie 4 (Zaawansowane):** Stwórz rozbudowaną instrukcję obsługi wyrobu zawierającą stronę tytułową, automatyczny spis treści, nagłówki dwóch poziomów, zagnieżdżoną listę numerowaną oraz wyeksportowany plik PDF.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Jaka jest główna zaleta stosowania stylów (np. Nagłówek 1, Nagłówek 2) w edytorze tekstu?",
    "opcje": [
      "Automatyczne sprawdzanie pisowni w języku obcym",
      "Gwarancja spójności wyglądu oraz możliwość automatycznego wygenerowania spisu treści",
      "Zmniejszenie zużycia prądu przez monitor",
      "Zabezpieczenie pliku hasłem"
    ],
    "poprawna": 1,
    "wyjasnienie": "Style porządkują strukturę logiczną dokumentu, co pozwala edytorowi stworzyć automatyczny spis treści i zapewnia jednakowy wygląd nagłówków."
  },
  {
    "pytanie": "Czym różni się podział sekcji od zwykłego podziału strony?",
    "opcje": [
      "Nie ma żadnej różnicy",
      "Podział sekcji pozwala na stosowanie odmiennego formatowania (np. nagłówków, stopek, orientacji) na kolejnych stronach",
      "Podział strony automatycznie zapisuje plik w internecie",
      "Podział sekcji usuwa cały tekst"
    ],
    "poprawna": 1,
    "wyjasnienie": "Podział sekcji izoluje fragmenty dokumentu, umożliwiając np. zmianę orientacji z pionowej na poziomą lub wyłączenie numeracji na wybranej stronie."
  },
  {
    "pytanie": "Jak zaktualizować automatyczny spis treści po dopisaniu nowych rozdziałów?",
    "opcje": [
      "Trzeba przepisać cały spis ręcznie od nowa",
      "Kliknąć prawym przyciskiem myszy na spis i wybrać 'Aktualizuj pole'",
      "Zresetować komputer",
      "Skasować wszystkie spacje"
    ],
    "poprawna": 1,
    "wyjasnienie": "Opcja 'Aktualizuj pole' w spisie treści skanuje dokument w poszukiwaniu nowych nagłówków i aktualizuje numery stron."
  },
  {
    "pytanie": "W jakim celu stosuje się format PDF przy publikacji gotowych instrukcji obsługi?",
    "opcje": [
      "Aby każdy mógł łatwo zmienić tekst instrukcji",
      "Gwarantuje identyczny wygląd dokumentu na każdym urządzeniu i zapobiega przypadkowemu przeskakiwaniu tekstu",
      "PDF automatycznie tłumaczy treść na 50 języków",
      "PDF służy tylko do zapisywania dźwięku"
    ],
    "poprawna": 1,
    "wyjasnienie": "Format PDF utrwala układ graficzny i czcionki, dając pewność, że czytelnik zobowiązany do przestrzegania instrukcji zobaczy dokładnie taki sam dokument jak autor."
  },
  {
    "pytanie": "Gdzie w programie Word / Writer znajduje się funkcja wstawiania automatycznego spisu treści?",
    "opcje": [
      "W zakładce Odwołania / Wstaw (References / Insert)",
      "W kalkulatorze systemowym",
      "W opcjach drukarki",
      "W oknie rysowania kszatłtów"
    ],
    "poprawna": 0,
    "wyjasnienie": "Funkcje obsługi odsyłaczy, podpisów i spisu treści znajdują się w sekcji Odwołania (References)."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na MS Word / LibreOffice Writer dla Szkół Branżowych.*
