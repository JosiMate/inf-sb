# Największy i najmniejszy, czyli jak znaleźć NWD i NWW

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 6**

Wyobraź sobie, że masz do wyłożenia podłogę w łazience o wymiarach 240 cm na 360 cm. Chcesz użyć do tego największych możliwych kwadratowych płytek, żeby nie trzeba było ich ciąć, a spoiny były jak najrzadsze. Albo masz dwa budziki: jeden dzwoni co 15 minut, a drugi co 20 minut. Kiedy oba zadzwonią w tym samym czasie po raz pierwszy? To nie są zagadki z podręcznika do matematyki — to konkretne problemy, które rozwiązujemy za pomocą NWD i NWW.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. odróżnić dzielnik liczby od jej wielokrotności
    2. znaleźć największy wspólny dzielnik (NWD) dwóch liczb za pomocą rozkładu na czynniki pierwsze
    3. znaleźć najmniejszą wspólną wielokrotność (NWW) dwóch liczb za pomocą rozkładu na czynniki pierwsze
    4. skorzystać z zależności między NWD a NWW do szybkiego obliczenia jednej z tych wartości

## 1. Podstawa: Dzielniki i wielokrotności

Zanim przejdziemy do „największych” i „najmniejszych”, musimy uporządkować dwa podstawowe pojęcia.

### Dzielniki (Kto dzieli?)
Liczba **A** jest dzielnikiem liczby **B**, jeśli B dzieli się przez A bez reszty.
- **Przykład**: Dzielniki liczby 12 to: 1, 2, 3, 4, 6, 12.
- *Wskazówka*: Dzielniki są zawsze mniejsze lub równe danej liczbie.

### Wielokrotności (Kto pomnaża?)
Liczba **C** jest wielokrotnością liczby **D**, jeśli powstała z pomnożenia D przez jakąś liczbę całkowitą.
- **Przykład**: Wielokrotności liczby 12 to: 12, 24, 36, 48, 60...
- *Wskazówka*: Wielokrotności są zawsze większe lub równe danej liczbie i jest ich nieskończenie wiele.

---

## 2. NWD — Największy Wspólny Dzielnik

**NWD** to największa liczba, która jednocześnie dzieli obie sprawdzane liczby. W praktyce szukamy największego „wspólnego mianownika”, który pozwoli nam np. podzielić dwie różne długości na równe, najdłuższe możliwe kawałki.

### Metoda rozkładu na czynniki pierwsze
To najpewniejszy sposób. Polega na „rozbiciu” liczb na najmniejsze możliwe klocki (liczby pierwsze: 2, 3, 5, 7, 11...).

**Krok po kroku dla liczb 24 i 36:**
1. **Rozkładamy obie liczby**:
   - $24 = 2 \cdot 2 \cdot 2 \cdot 3 = 2^3 \cdot 3$
   - $36 = 2 \cdot 2 \cdot 3 \cdot 3 = 2^2 \cdot 3^2$
2. **Wypisujemy wspólne czynniki z najniższymi potęgami**:
   - Wspólna jest dwójka (najniższa potęga to $2^2$)
   - Wspólna jest trójka (najniższa potęga to $3^1$)
3. **Mnożymy je**:
   - $NWD(24, 36) = 2^2 \cdot 3 = 4 \cdot 3 = 12$

**Wynik**: Największym wspólnym dzielnikiem 24 i 36 jest **12**.

---

## 3. NWW — Najmniejsza Wspólna Wielokrotność

**NWW** to najmniejsza liczba, która jest jednocześnie wielokrotnością obu liczb. Szukamy najwcześniejszego momentu, w którym dwa różne cykle spotykają się w jednym punkcie.

### Metoda rozkładu na czynniki pierwsze
Tutaj zasada jest odwrotna niż przy NWD.

**Krok po kroku dla liczb 24 i 36:**
1. **Rozkładamy obie liczby** (mamy już to z poprzedniego punktu):
   - $24 = 2^3 \cdot 3$
   - $36 = 2^2 \cdot 3^2$
2. **Wypisujemy WSZYSTKIE czynniki, które pojawiły się w rozkładach, ale z NAJWYŻSZYMI potęgami**:
   - Mamy dwójki (najwyższa potęga to $2^3$)
   - Mamy trójki (najwyższa potęga to $3^2$)
3. **Mnożymy je**:
   - $NWW(24, 36) = 2^3 \cdot 3^2 = 8 \cdot 9 = 72$

**Wynik**: Najmniejszą wspólną wielokrotnością 24 i 36 jest **72**.

!!! tip "Szybki test: NWD vs NWW"
    - **NWD** $\rightarrow$ Szukamy czegoś **mniejszego** (dzielnika), co pasuje do obu.
    - **NWW** $\rightarrow$ Szukamy czegoś **większego** (wielokrotności), w czym obie liczby się mieszczą.

---

## 4. Złota zasada: Relacja NWD i NWW

Istnieje matematyczny „skrót”, który pozwala obliczyć jedną z tych wartości, jeśli znamy drugą. Dla dowolnych dwóch liczb $a$ i $b$ zachodzi zależność:

$$NWD(a, b) \cdot NWW(a, b) = a \cdot b$$

**Co to oznacza w praktyce?**
Jeśli wiesz, że $NWD(24, 36) = 12$, to nie musisz robić rozkładu na czynniki, żeby znaleźć NWW. Możesz użyć wzoru:
$12 \cdot NWW = 24 \cdot 36$
$12 \cdot NWW = 864$
$NWW = 864 / 12 = 72$

!!! warning "Uwaga na pułapkę!"
    Ta zasada działa **tylko dla dwóch liczb**. Przy trzech liczbach (np. NWD z 12, 18 i 24) ta prosta metoda już nie zadziała — musisz wrócić do rozkładu na czynniki pierwsze.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Które z poniższych stwierdzeń jest prawdziwe?",
    "opcje": [
      "Dzielniki liczby są zawsze większe od tej liczby",
      "Wielokrotności liczby są zawsze mniejsze od tej liczby",
      "NWD (Największy Wspólny Dzielnik) musi być mniejszy lub równy mniejszej z dwóch liczb",
      "NWW (Najmniejsza Wspólna Wielokrotność) musi być mniejsza od obu liczb"
    ],
    "poprawna": 2,
    "wyjasnienie": "Dzielniki są mniejsi lub równi liczbie, a wielokrotności więksi lub równi. NWD nie może być większy niż mniejsza z liczb, bo nie mógłby być jej dzielnikiem."
  },
  {
    "pytanie": "Jaki jest NWD liczb 15 i 20?",
    "opcje": [
      "5",
      "10",
      "60",
      "300"
    ],
    "poprawna": 0,
    "wyjasnienie": "Dzielniki 15: {1, 3, 5, 15}. Dzielniki 20: {1, 2, 4, 5, 10, 20}. Wspólne to {1, 5}. Największy z nich to 5."
  },
  {
    "pytanie": "Jaki jest NWW liczb 6 i 8?",
    "opcje": [
      "2",
      "14",
      "24",
      "48"
    ],
    "poprawna": 2,
    "wyjasnienie": "Wielokrotności 6: {6, 12, 18, 24, 30...}. Wielokrotności 8: {8, 16, 24, 32...}. Pierwsza wspólna to 24."
  },
  {
    "pytanie": "Liczby a i b mają NWD = 4 oraz NWW = 24. Iloczyn tych liczb (a * b) wynosi:",
    "opcje": [
      "28",
      "20",
      "96",
      "12"
    ],
    "poprawna": 2,
    "wyjasnienie": "Zgodnie ze złotą zasadą: NWD * NWW = a * b. Zatem 4 * 24 = 96."
  },
  {
    "pytanie": "Do czego w informatyce najczęściej wykorzystujemy algorytmy znajdowania NWD?",
    "opcje": [
      "Do sortowania list nazwisk",
      "Do skracania ułamków do najprostszej postaci",
      "Do zmiany koloru tekstu w dokumencie",
      "Do sprawdzania połączenia z internetem"
    ],
    "poprawna": 1,
    "wyjasnienie": "Aby skrócić ułamek, dzielimy licznik i mianownik przez ich największy wspólny dzielnik (NWD)."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady zgodne z podstawą programową dla szkół branżowych I stopnia.*
