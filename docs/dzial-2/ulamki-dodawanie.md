# Wspólny mianownik, czyli jak program dodaje i skraca ułamki

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 8**

Do tej pory uczyliśmy się NWD i NWW jako abstrakcyjnych pojęć matematycznych i algorytmów. Czas sprawdzić, gdzie one „pracują” w rzeczywistości. Jednym z najważniejszych zastosowań tych algorytmów w informatyce jest obsługa ułamków. Komputery nie lubią ułamków zwykłych (takich jak $1/3$), wolą ułamki dziesiętne ($0,333...$), ale w wielu zawodach precyzja ułamka zwykłego jest niezbędna.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić rolę NWD w procesie skracania ułamków
    2. wyjaśnić rolę NWW w procesie sprowadzania ułamków do wspólnego mianownika
    3. rozpisać algorytm dodawania dwóch ułamków zwykłych
    4. zaprojektować logikę programu, który sumuje ułamki i automatycznie upraszcza wynik

## 1. Skracanie ułamków (Zastosowanie NWD)

Skracanie ułamka polega na zapisaniu go w najprostszej możliwej postaci. Aby to zrobić, musimy znaleźć największą liczbę, przez którą możemy podzielić jednocześnie licznik i mianownik. Ta liczba to właśnie **NWD**.

**Algorytm skracania:**
1. Pobierz licznik ($L$) i mianownik ($M$).
2. Oblicz $NWD(L, M)$.
3. Podziel licznik przez NWD $\rightarrow$ nowy licznik.
4. Podziel mianownik przez NWD $\rightarrow$ nowy mianownik.

**Przykład dla ułamka $12/18$:**
- $L = 12, M = 18$.
- $NWD(12, 18) = 6$.
- Nowy licznik: $12 \div 6 = 2$.
- Nowy mianownik: $18 \div 6 = 3$.
- **Wynik: $2/3$**.

---

## 2. Dodawanie ułamków (Zastosowanie NWW)

Dodawanie ułamków o różnych mianownikach to proces, który dla człowieka bywa żmudny, ale dla komputera jest banalny, jeśli mamy gotowy algorytm NWW.

**Algorytm dodawania ($L1/M1 + L2/M2$):**
1. **Znajdź wspólny mianownik**: Oblicz $NWW(M1, M2)$. To będzie nasz nowy mianownik ($M_{wynik}$).
2. **Dostosuj liczniki**:
   - Oblicz, ile razy mianownik $M1$ mieści się w $M_{wynik}$. Pomnóż licznik $L1$ przez tę wartość.
   - Oblicz, ile razy mianownik $M2$ mieści się w $M_{wynik}$. Pomnóż licznik $L2$ przez tę wartość.
3. **Zsumuj**: Dodaj nowe liczniki do siebie $\rightarrow$ otrzymasz licznik wyniku ($L_{wynik}$).
4. **Uprość**: Zastosuj algorytm skracania (z punktu 1), aby wynik był w najprostszej postaci.

**Przykład dla $1/4 + 1/6$:**
1. $NWW(4, 6) = 12$. Nasz wspólny mianownik to **12**.
2. Dostosowanie:
   - $12 \div 4 = 3 \rightarrow 1 \cdot 3 = 3$.
   - $12 \div 6 = 2 \rightarrow 1 \cdot 2 = 2$.
3. Sumowanie: $3 + 2 = 5$.
4. Wynik: **$5/12$** (nie da się już skrócić, bo $NWD(5, 12) = 1$).

---

## 3. Jak to zapisać w programie?

W programowaniu nie piszemy wszystkiego od nowa. Wykorzystujemy tzw. **funkcje** lub gotowe bloki z poprzednich lekcji. Program do dodawania ułamków to w rzeczywistości „orkiestra”, która steruje innymi algorytmami.

**Schemat działania programu:**
`Start` $\rightarrow$ `Pobierz dane` $\rightarrow$ `Wywołaj Algorytm NWW` $\rightarrow$ `Oblicz nowe liczniki` $\rightarrow$ `Zsumuj` $\rightarrow$ `Wywołaj Algorytm NWD (do skracania)` $\rightarrow$ `Wyświetl wynik` $\rightarrow$ `Koniec`.

!!! tip "Zaleta programowania"
    Raz napisany algorytm NWD i NWW możesz wykorzystać w dziesiątkach różnych programów. Właśnie dlatego programiści tworzą tzw. **biblioteki**, czyli zbiory gotowych, przetestowanych funkcji, których nie trzeba pisać od nowa.

---

## 4. Pułapki programistyczne

Przy ułamkach komputer może napotkać dwa główne problemy:
1. **Dzielenie przez zero**: Program musi sprawdzić, czy mianownik nie jest zerem, zanim zacznie liczyć. Jeśli jest zerem $\rightarrow$ program powinien wyświetlić błąd.
2. **Ułamki niewłaściwe**: Jeśli licznik jest większy od mianownika (np. $7/3$), program może zostać rozbudowany o funkcję zamiany ułamka na liczbę mieszaną ($2$ i $1/3$).

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Który algorytm jest niezbędny do skracania ułamków do najprostszej postaci?",
    "opcje": [
      "Algorytm dodawania",
      "Algorytm NWW",
      "Algorytm NWD",
      "Algorytm mnożenia"
    ],
    "poprawna": 2,
    "wyjasnienie": "Aby skrócić ułamek, musimy podzielić licznik i mianownik przez ich największy wspólny dzielnik (NWD)."
  },
  {
    "pytanie": "Do czego służy NWW w procesie dodawania ułamków?",
    "opcje": [
      "Do sprawdzania, czy ułamek jest właściwy",
      "Do wyznaczenia wspólnego mianownika",
      "Do pomnożenia licznika przez mianownik",
      "Do skracania wyniku końcowego"
    ],
    "poprawna": 1,
    "wyjasnienie": "NWW mianowników pozwala nam sprowadzić ułamki do wspólnego mianownika, co jest warunkiem koniecznym do ich dodawania."
  },
  {
    "pytanie": "Jaki jest poprawny wynik dodawania 1/2 + 1/3 po zastosowaniu algorytmu?",
    "opcje": [
      "2/5",
      "5/6",
      "1/6",
      "2/6"
    ],
    "poprawna": 1,
    "wyjasnienie": "NWW(2, 3) = 6. Ułamki to 3/6 i 2/6. Suma = 5/6."
  },
  {
    "pytanie": "Co program powinien zrobić, jeśli mianownik ułamka wynosi 0?",
    "opcje": [
      "Zignorować to i liczyć dalej",
      "Zamienić 0 na 1",
      "Wyświetlić błąd (dzielenie przez zero jest niedozwolone)",
      "Zmienić ułamek na liczbę całkowitą"
    ],
    "poprawna": 2,
    "wyjasnienie": "W matematyce i informatyce dzielenie przez zero jest nieoznaczone i powoduje błąd programu (crash), dlatego należy to obsłużyć warunkiem 'jeżeli'."
  },
  {
    "pytanie": "W jakiej kolejności program powinien przetwarzać dodawanie ułamków?",
    "opcje": [
      "Skracanie $\rightarrow$ Dodawanie $\rightarrow$ NWW",
      "NWW $\rightarrow$ Dostosowanie liczników $\rightarrow$ Sumowanie $\rightarrow$ Skracanie (NWD)",
      "Sumowanie $\rightarrow$ NWW $\rightarrow$ Skracanie",
      "Skracanie $\rightarrow$ NWW $\rightarrow$ Sumowanie"
    ],
    "poprawna": 1,
    "wyjasnienie": "Najpierw musimy sprowadzić ułamki do wspólnego mianownika (NWW), potem zsumować liczniki, a na samym końcu uprościć wynik za pomocą NWD."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady zgodne z podstawą programową dla szkół branżowych I stopnia.*
