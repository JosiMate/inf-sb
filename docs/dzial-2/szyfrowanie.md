# Szyfrowanie, czyli poznajemy szyfr Cezara i szyfr przedstawieniowy

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 10**

Wyobraź sobie, że chcesz wysłać do kolegi wiadomość, której nie może odczytać nikt inny, kto przypadkiem przejmie Twoją kartkę z notatką. Aby to osiągnąć, musisz zamienić zrozumiały tekst na „bełkot”, który tylko osoba posiadająca specjalny klucz będzie w stanie odczytać. To właśnie jest **szyfrowanie**.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. zdefiniować pojęcia: tekst jawny, szyfrogram i klucz
    2. wyjaśnić zasadę działania szyfru przedstawieniowego
    3. samodzielnie zaszyfrować i odszyfrować wiadomość szyfrem Cezara
    4. powiązać proces szyfrowania z operacjami na listach i przesunięciami w programowaniu
    5. odróżnić słabe szyfry od silnego szyfrowania stosowanego w sieci (np. HTTPS)

## 1. Podstawy tajnej komunikacji

Zanim przejdziemy do konkretnych metod, musimy poznać trzy kluczowe pojęcia:

- **Tekst jawny** — wiadomość, którą każdy może przeczytać (np. „Cześć!”).
- **Szyfrogram** — wiadomość po zaszyfrowaniu, która wygląda jak przypadkowy ciąg znaków (np. „Fćǵść!”).
- **Klucz** — tajna informacja, która mówi nam, w jaki sposób zamieniono litery. Bez klucza odszyfrowanie wiadomości jest bardzo trudne.

**Szyfrowanie** to zamiana tekstu jawnego na szyfrogram.
**Deszyfrowanie** to proces odwrotny — odzyskiwanie tekstu jawnego z szyfrogramu.

---

## 2. Szyfr przedstawieniowy (Podstawieniowy)

To jedna z najstarszych i najprostszych metod szyfrowania. Polega na stworzeniu „mapy” (tabeli), w której każdej literze alfabetu przypisujemy inną, zastępczą literę lub symbol.

**Przykład mapy:**
- A $\rightarrow$ @
- B $\rightarrow$ #
- C $\rightarrow$ %
- D $\rightarrow$ &
- ...i tak dalej.

Jeśli chcemy zaszyfrować słowo „BABA”, sprawdzamy w tabeli: B to `#`, A to `@`.
**Wynik**: `#@#@`

Aby odszyfrować wiadomość, odbiorca musi mieć dokładnie taką samą tabelę i szukać znaków w drugą stronę (od symbolu do litery).

---

## 3. Szyfr Cezara (Szyfr przesuwany)

Szyfr Cezara to szczególny rodzaj szyfru przedstawieniowego. Zamiast tworzyć losową tabelę, używamy prostej zasady: **przesuwamy cały alfabet o określoną liczbę miejsc**.

Tą liczbą miejsc jest właśnie nasz **klucz**.

**Przykład: Klucz = 3**
Przesuwamy alfabet o 3 pozycje w prawo:
- A $\rightarrow$ D
- B $\rightarrow$ E
- C $\rightarrow$ F
- ...
- X $\rightarrow$ A (po Z wracamy na początek alfabetu!)
- Y $\rightarrow$ B
- Z $\rightarrow$ C

**Zaszyfrujmy słowo „KOD” (Klucz 3):**
- K $\rightarrow$ N
- O $\rightarrow$ R
- D $\rightarrow$ G
- **Szyfrogram**: `NRG`

**Odszyfrowanie**: Aby odzyskać tekst, przesuwamy litery o klucz w drugą stronę (w lewo).
- N $\rightarrow$ K
- R $\rightarrow$ O
- G $\rightarrow$ D

---

## 4. Szyfrowanie w świecie komputerów

Jak komputer realizuje szyfr Cezara? Nie „przesuwa” on literek w głowie, tylko operuje na ich numerach (indeksach).

**Logika programu:**
1. Stwórz listę zawierającą wszystkie litery alfabetu.
2. Dla każdej litery tekstu jawnego:
   - Znajdź jej numer na liście (np. A to 1, B to 2).
   - Dodaj do tego numer wartość klucza (np. $1 + 3 = 4$).
   - Wybierz literę o nowym numerze (4 to D).
3. Jeśli nowy numer przekroczy długość alfabetu, użyj operatora **modulo (mod)**, aby wrócić na początek.

!!! tip "Dlaczego szyfry Cezara są 'słabe'?"
    Szyfr Cezara ma ogromną wadę: istnieje tylko 25 możliwych kluczy (przesunięć). Komputer może w ułamku sekundy sprawdzić wszystkie kombinacje i złamać taką wiadomość w procesie zwanym **atakiem brute-force**.

---

## 5. Szyfrowanie w sieci — HTTPS

W dzisiejszych czasach do ochrony haseł czy danych bankowych używa się znacznie bardziej skomplikowanych algorytmów (np. AES lub RSA). Są one tak silne, że nawet najszybsze superkomputery potrzebowałyby milionów lat na ich złamanie.

Jak rozpoznać, że Twoje dane są szyfrowane w internecie?
- W adresie strony zamiast `http://` widzisz **`https://`** (S oznacza *Secure* — bezpieczny).
- Przy adresie strony pojawia się **ikona kłódki**.

To oznacza, że Twoja przeglądarka i serwer strony wymieniły klucze szyfrujące, a każda wysłana informacja jest zamieniona w potężny szyfrogram, którego nikt „po drodze” nie odczyta.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Czym jest klucz w procesie szyfrowania?",
    "opcje": [
      "Hasłem do logowania do komputera",
      "Tajemną informacją pozwalającą zamienić szyfrogram z powrotem w tekst jawny",
      "Sposobem na przyspieszenie działania procesora",
      "Rodzajem wirusa komputerowego"
    ],
    "poprawna": 1,
    "wyjasnienie": "Klucz to parametr (np. liczba przesunięcia w szyfrze Cezara lub tabela zamian), który jest niezbędny do poprawnego zaszyfrowania i odszyfrowania danych."
  },
  {
    "pytanie": "Zaszyfruj słowo 'ALA' szyfrem Cezara z kluczem 1. Jaki będzie wynik?",
    "opcje": [
      "BMB",
      "ZKZ",
      "ALB",
      "BMA"
    ],
    "poprawna": 0,
    "wyjasnienie": "Przesunięcie o 1: A $\rightarrow$ B, L $\rightarrow$ M, A $\rightarrow$ B. Wynik to BMB."
  },
  {
    "pytanie": "Czym różni się szyfr przedstawieniowy od szyfru Cezara?",
    "opcje": [
      "Szyfr Cezara nie wymaga klucza",
      "Szyfr przedstawieniowy używa tylko liczb, a Cezara tylko liter",
      "Szyfr Cezara jest rodzajem szyfru przedstawieniowego, w którym zamiana odbywa się według stałego przesunięcia",
      "Nie ma między nimi żadnej różnicy"
    ],
    "poprawna": 2,
    "wyjasnienie": "Szyfr przedstawieniowy to ogólna metoda zamiany znaków na inne. Szyfr Cezara to konkretny przypadek tej metody, gdzie zamiana wynika z przesunięcia w alfabecie."
  },
  {
    "pytanie": "Dlaczego w programowaniu do szyfru Cezara używamy operatora modulo?",
    "opcje": [
      "Aby przyspieszyć działanie programu",
      "Aby wiadomość była krótsza",
      "Aby po dotarciu do końca alfabetu (litery Z) wrócić na jego początek (litera A)",
      "Aby usunąć spacje z tekstu"
    ],
    "poprawna": 2,
    "wyjasnienie": "Modulo pozwala 'zapętlić' alfabet. Jeśli przesunięcie wyjdzie poza zakres 1-26, modulo sprowadzi wynik z powrotem do zakresu liter alfabetu."
  },
  {
    "pytanie": "Co oznacza litera 'S' w protokole HTTPS?",
    "opcje": [
      "Standard (Standardowy)",
      "Secure (Bezpieczny)",
      "System (Systemowy)",
      "Speed (Szybki)"
    ],
    "poprawna": 1,
    "wyjasnienie": "S pochodzi od angielskiego 'Secure' i oznacza, że transmisja danych między przeglądarką a serwerem jest szyfrowana."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady zgodne z podstawą programową dla szkół branżowych I stopnia.*
