# Zera, jedynki i wagi, czyli różne reprezentacje liczb

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 9**

!!! abstract "O tym temacie"

    **1 godzina lekcyjna** · Dział II. Programowanie i algorytmy · rozdział 9

    Czy zastanawiałeś się kiedyś, jak komputer „widzi” liczbę 5, kolor czerwony albo literę „A”? Dla nas liczby są zapisane w systemie dziesiętnym, bo mamy dziesięć palców u rąk. Komputer nie ma palców — ma miliardy mikroskopijnych przełączników, które mogą być tylko w dwóch stanach: **włączone (1)** lub **wyłączone (0)**. To dlatego świat informatyki opiera się na zerach i jedynkach.



!!! success "Kryteria sukcesu"

    Po tej lekcji:
    1. Wyjaśnię, dlaczego komputery używają systemu dwójkowego
    2. Określę wagę poszczególnych bitów w bajcie
    3. Zamienię prostą liczbę binarną na dziesiętną i odwrotnie
    4. Skorzystam z kalkulatora systemowego do konwersji liczb
    5. Odróżnię bit od bajtu i rozumieć ich znaczenie w przechowywaniu danych

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Jak znaleźć wspólny mianownik dwóch ułamków zwykłych a/b i c/d?
    2. **Sprzed kilku tygodni.** Co oznacza pojęcie ułamka nieskracalnego?
    3. **Z dawniejszych tematów.** Do czego służy dzielenie całkowite `//` w Pythonie?

    ??? success "Odpowiedzi"

        1. Najmniejszym wspólnym mianownikiem jest Najmniejsza Wspólna Wielokrotność (NWW) mianowników b i d.
        2. Ułamek, w którym licznik i mianownik są względnie pierwsze (ich NWD wynosi 1).
        3. Oblicza iloraz całkowity z dzielenia bez reszty (np. `7 // 2` daje `3`).

## 1. System dziesiętny vs dwójkowy

Większość z nas używa **systemu dziesiętnego** (podstawa 10). Używamy cyfr od 0 do 9. Kiedy zabraknie nam cyfr, dodajemy nową kolumnę (dziesiątki, setki, tysiące).

Komputer używa **systemu dwójkowego** (podstawa 2). Ma do dyspozycji tylko dwie cyfry: **0** i **1**. 
- **1** = prąd płynie / stan wysoki / prawda
- **0** = prąd nie płynie / stan niski / fałsz

Pojedyncza taka cyfra (0 lub 1) to **bit** (od angielskiego *binary digit*). Jest to najmniejsza możliwa jednostka informacji w komputerze.

---

## 2. Wagi bitów — jak czytać zera i jedynki?

Aby zrozumieć, jaką wartość ma liczba binarna, musimy poznać **wagi bitów**. W systemie dziesiętnym wagi to 1, 10, 100, 1000... W systemie dwójkowym wagi są potęgami liczby 2.

W jednym **bajcie** (który składa się z 8 bitów) wagi liczymy od prawej strony (od najmłodszego bitu):

| Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |

### Jak zamienić liczbę binarną na dziesiętną?
To proste: sumujemy wagi wszystkich bitów, które mają wartość **1**.

**Przykład: Co to za liczba `00001101`?**
- Bit 0 (waga 1): ma wartość **1** $\rightarrow$ bierzemy 1
- Bit 1 (waga 2): ma wartość **0** $\rightarrow$ pomijamy
- Bit 2 (waga 4): ma wartość **1** $\rightarrow$ bierzemy 4
- Bit 3 (waga 8): ma wartość **1** $\rightarrow$ bierzemy 8
- Pozostałe bity to 0.
- **Suma**: $8 + 4 + 1 = 13$.
- **Wynik**: `00001101` w systemie dwójkowym to **13** w systemie dziesiętnym.

---

## 3. Zamiana z dziesiętnego na dwójkowy

Aby zamienić liczbę dziesiętną na binarną, sprawdzamy, które wagi „mieszczą się” w naszej liczbie.

**Przykład: Zamień liczbę 45 na binarną.**
1. Czy 128 mieści się w 45? Nie $\rightarrow$ **0**
2. Czy 64 mieści się w 45? Nie $\rightarrow$ **0**
3. Czy 32 mieści się w 45? **Tak** $\rightarrow$ **1**. Zostaje: $45 - 32 = 13$.
4. Czy 16 mieści się w 13? Nie $\rightarrow$ **0**.
5. Czy 8 mieści się w 13? **Tak** $\rightarrow$ **1**. Zostaje: $13 - 8 = 5$.
6. Czy 4 mieści się w 5? **Tak** $\rightarrow$ **1**. Zostaje: $5 - 4 = 1$.
7. Czy 2 mieści się w 1? Nie $\rightarrow$ **0**.
8. Czy 1 mieści się w 1? **Tak** $\rightarrow$ **1**. Zostaje: 0.
- **Wynik**: `00101101`.

---

## 4. Bajty i jednostki informacji

Ponieważ pojedynczy bit to za mało, by zapisać cokolwiek sensownego, komputer grupuje je w **bajty**.

- **1 bajt = 8 bitów**.
- Za pomocą jednego bajtu możemy zapisać $2^8 = 256$ różnych wartości (od 0 do 255). To wystarczy np. do zapisania jednej litery alfabetu lub jednej prostej instrukcji procesora.

!!! tip "Trik z Kalkulatorem Windows"
    Nie musisz zawsze liczyć wag w pamięci! W systemie Windows:
    1. Otwórz **Kalkulator**.
    2. Zmień tryb na **Programista**.
    3. Wpisz liczbę w polu `DEC` (dziesiętna) — w polach `BIN` (binarna) i `HEX` (szesnastkowa) zobaczysz automatycznie przeliczone wartości.

---

## 5. Inne systemy (Szesnastkowy)

W informatyce często spotkasz system **szesnastkowy (HEX)**. Dlaczego? Bo zapis binarny jest bardzo długi (np. `101101101010...`), a system szesnastkowy pozwala go zapisać znacznie krócej.

W systemie HEX używamy cyfr 0-9 oraz liter A, B, C, D, E, F (gdzie A=10, B=11 itd.).
- Jeden znak HEX zastępuje dokładnie **4 bity** (tzw. nibble).
- Przykład: Kolory w WWW zapisuje się w HEX, np. `#FF0000` to czysta czerwień.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Dlaczego komputery używają systemu dwójkowego, a nie dziesiętnego?",
    "opcje": [
      "Ponieważ jest on szybszy do dodawania",
      "Ponieważ sprzęt komputerowy opiera się na dwóch stanach: włączony (1) i wyłączony (0)",
      "Ponieważ systemy dziesiętne zajmują więcej miejsca na dysku",
      "Ponieważ tak zdecydowali twórcy pierwszych klawiatur"
    ],
    "poprawna": 1,
    "wyjasnienie": "Podstawą działania procesora i pamięci są tranzystory, które działają jak przełączniki (on/off), co idealnie odpowiada systemowi dwójkowemu."
  },
  {
    "pytanie": "Jaka jest waga drugiego bitu od prawej (Bit 1)?",
    "opcje": [
      "1",
      "2",
      "4",
      "8"
    ],
    "poprawna": 1,
    "wyjasnienie": "Wagi bitów to potęgi dwójki, licząc od prawej: $2^0=1$, $2^1=2$, $2^2=4$ itd. Drugi bit od prawej ma wagę 2."
  },
  {
    "pytanie": "Jaka jest wartość liczby binarnej 00000111 w systemie dziesiętnym?",
    "opcje": [
      "3",
      "7",
      "11",
      "15"
    ],
    "poprawna": 1,
    "wyjasnienie": "Sumujemy wagi bitów, które mają wartość 1: $4 + 2 + 1 = 7$."
  },
  {
    "pytanie": "Ile bitów składa się na jeden bajt?",
    "opcje": [
      "2",
      "4",
      "8",
      "16"
    ],
    "poprawna": 2,
    "wyjasnienie": "Standardowo 1 bajt składa się z 8 bitów."
  },
  {
    "pytanie": "Jaką wartość ma liczba binarna 00001000?",
    "opcje": [
      "4",
      "8",
      "16",
      "10"
    ],
    "poprawna": 1,
    "wyjasnienie": "Tylko czwarty bit od prawej (Bit 3) ma wartość 1. Jego waga to 8."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady oparte na standardach architektury x86 i systemie Windows 11.*
