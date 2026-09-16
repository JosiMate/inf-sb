# Komputer znajduje NWD i NWW, czyli jak ułożyć program na podstawie algorytmu

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 7**

W poprzedniej lekcji nauczyliśmy się, jak wyznaczać NWD i NWW „na kartce”, korzystając z rozkładu na czynniki pierwsze. Jednak dla komputera rozkładanie liczb na czynniki (szczególnie bardzo dużych) jest czasochłonne i trudne. Programiści używają dlatego specjalnych „przepisów” zwanych **algorytmami**, które pozwalają znaleźć wynik znacznie szybciej.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić, czym jest algorytm i dlaczego jest potrzebny w programowaniu
    2. odróżnić nieoptymalną metodę odejmowania od optymalnego algorytmu Euklidesa
    3. przełożyć kroki algorytmu na konstrukcje programistyczne (pętle i warunki)
    4. zaprojektować logikę programu obliczającego NWD i NWW w środowisku Scratch

## 1. Czym jest algorytm?

**Algorytm** to skończony ciąg jasno określonych czynności, które prowadzą do rozwiązania problemu. To tak naprawdę „przepis na wynik”.

W programowaniu nie piszemy kodu „z głowy”. Proces zawsze wygląda tak:
**Problem $\rightarrow$ Algorytm (Plan) $\rightarrow$ Kod (Implementacja) $\rightarrow$ Program**

Jeśli algorytm jest błędny, nawet najpiękniejszy kod w Scratchu czy Pythonie nie zadziała.

---

## 2. Metoda „na odejmowanie” (Algorytm nieoptymalny)

Najprostszy sposób na znalezienie NWD to wielokrotne odejmowanie mniejszej liczby od większej, aż obie liczby staną się sobie równe.

**Algorytm:**
1. Pobierz dwie liczby: $A$ i $B$.
2. Dopóki $A$ nie jest równe $B$:
   - Jeśli $A > B$, to odejmij $B$ od $A$ ($A = A - B$).
   - W przeciwnym razie odejmij $A$ od $B$ ($B = B - A$).
3. Gdy liczby będą równe, ich wartość to **NWD**.

**Przykład dla 48 i 18:**
- $48 > 18 \rightarrow 48 - 18 = 30$ (teraz mamy 30 i 18)
- $30 > 18 \rightarrow 30 - 18 = 12$ (teraz mamy 12 i 18)
- $18 > 12 \rightarrow 18 - 12 = 6$ (teraz mamy 12 i 6)
- $12 > 6 \rightarrow 12 - 6 = 6$ (teraz mamy 6 i 6)
- **Koniec!** Liczby są równe. **NWD = 6**.

!!! warning "Dlaczego to jest nieoptymalne?"
    Wyobraź sobie, że chcesz znaleźć NWD dla liczb 1 000 000 i 2. Komputer musiałby wykonać 499 999 odejmowań! To strata czasu i mocy obliczeniowej.

---

## 3. Algorytm Euklidesa (Metoda optymalna)

Euklides, grecki matematyk, wymyślił sprytny sposób. Zamiast odejmować wiele razy, użył **dzielenia z resztą (modulo)**. Modulo pozwala nam „przeskoczyć” wszystkie niepotrzebne odejmowania za jednym razem.

**Algorytm:**
1. Pobierz dwie liczby: $A$ i $B$.
2. Dopóki $B$ nie jest równe 0:
   - Zapamiętaj wartość $B$ jako tymczasową.
   - Zastąp $A$ wartością $B$.
   - Zastąp $B$ resztą z dzielenia $A$ przez $B$ (modulo).
3. Gdy $B$ stanie się zerem, wynik znajduje się w zmiennej $A$.

**Przykład dla 48 i 18:**
- Krok 1: $48 \div 18 = 2$ reszta **12** $\rightarrow$ (teraz mamy 18 i 12)
- Krok 2: $18 \div 12 = 1$ reszta **6** $\rightarrow$ (teraz mamy 12 i 6)
- Krok 3: $12 \div 6 = 2$ reszta **0** $\rightarrow$ (teraz mamy 6 i 0)
- **Koniec!** Druga liczba to 0. **NWD = 6**.

Zauważ, że zamiast wielu kroków, wystarczyły nam tylko **3 operacje**.

---

## 4. Z algorytmu do kodu (Scratch)

Aby komputer wykonał te instrukcje, musimy użyć konkretnych bloków z kategorii **Sterowanie** i **Operatorzy**.

| Krok algorytmu | Blok w Scratch |
| --- | --- |
| „Dopóki $B \neq 0$” | `powtarzaj aż < (zmienna B) = 0 >` |
| „Reszta z dzielenia” | operator `(zmienna A) mod (zmienna B)` |
| „Zapamiętaj wartość” | `ustaw [temp] na (zmienna B)` |
| „Zmień wartość” | `ustaw [zmienna A] na (zmienna B)` |

### A co z NWW?
Komputer nie musi uczyć się nowego algorytmu dla NWW. Wykorzystujemy „złotą zasadę” z poprzedniej lekcji. W programie dodajemy po prostu jedną linię obliczeń na samym końcu:
`ustaw [NWW] na ( (A * B) / NWD )`

!!! tip "Logika programisty"
    Zawsze najpierw stwórz schemat blokowy lub listę kroków (algorytm), a dopiero potem szukaj odpowiednich klocków w Scratchu. Próba pisania programu „na żywo” bez planu to najczęstsza przyczyna błędów (bugów).

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Co to jest algorytm w kontekście programowania?",
    "opcje": [
      "Specjalny rodzaj języka programowania",
      "Kolejność zapisu plików na dysku",
      "Jasno określony zestaw kroków prowadzących do rozwiązania problemu",
      "Błąd w kodzie, który trzeba naprawić"
    ],
    "poprawna": 2,
    "wyjasnienie": "Algorytm to swego rodzaju 'przepis' — lista instrukcji, które komputer musi wykonać po kolei, aby osiągnąć cel."
  },
  {
    "pytanie": "Dlaczego metoda odejmowania jest uznawana za nieoptymalną?",
    "opcje": [
      "Bo daje błędne wyniki dla liczb parzystych",
      "Bo wymaga zbyt wielu powtórzeń przy dużych różnicach między liczbami",
      "Bo nie można jej zapisać w Scratchu",
      "Bo jest zbyt skomplikowana dla programisty"
    ],
    "poprawna": 1,
    "wyjasnienie": "Przy dużych liczbach (np. 1 000 000 i 1) komputer musiałby wykonać ogromną liczbę odejmowań, co drastycznie spowalnia program."
  },
  {
    "pytanie": "Który operator w Scratchu jest kluczowy dla optymalnego algorytmu Euklidesa?",
    "opcje": [
      "Dodawanie (+)",
      "Mnożenie (*)",
      "Modulo (mod)",
      "Większy niż (>)"
    ],
    "poprawna": 2,
    "wyjasnienie": "Operator 'mod' oblicza resztę z dzielenia, co pozwala algorytmowi Euklidesa błyskawicznie redukować liczby."
  },
  {
    "pytanie": "W jaki sposób program najszybciej obliczy NWW, mając już obliczone NWD?",
    "opcje": [
      "Robiąc rozkład na czynniki pierwsze",
      "Wykorzystując wzór: (A * B) / NWD",
      "Odejmując NWD od mniejszej z liczb",
      "Sumując A i B, a potem dzieląc przez NWD"
    ],
    "poprawna": 1,
    "wyjasnienie": "Zależność NWD * NWW = A * B pozwala na błyskawiczne obliczenie NWW za pomocą jednego dzielenia."
  },
  {
    "pytanie": "Jeśli w algorytmie Euklidesa druga liczba (B) stała się zerem, gdzie szukamy wyniku NWD?",
    "opcje": [
      "W sumie obu liczb",
      "W ostatniej reszcie z dzielenia",
      "W pierwszej liczbie (A)",
      "Wynik jest zawsze równy 1"
    ],
    "poprawna": 2,
    "wyjasnienie": "Zgodnie z algorytmem, gdy B osiąga 0, wartość zgromadzona w zmiennej A jest największym wspólnym dzielnikiem."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady oparte na logice środowiska Scratch 3.0.*
