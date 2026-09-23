# Kalkulujemy, czyli jak wykorzystać arkusz kalkulacyjny w zarządzaniu finansami

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 19**

!!! abstract "O tym temacie"

    Zarządzanie finansami własnej firmy lub budżetem domowym wymaga umiejętności automatycznego wyliczania podatków, cen usług oraz symulacji wariantów biznesowych. W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się wyliczać podatek VAT, tworzyć listy rozwijane (prawidłowy dobór stawki), używać formuł warunkowych (`JEŻELI`), zaokrąglać kwoty (`ZAOKR`) oraz budować kalkulator symulacji usług.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie kwoty netto, kwoty brutto oraz podatku VAT (23%, 8%, 5%)
    2. obliczać kwotę podatku VAT oraz kwotę brutto z kwoty netto w arkuszu kalkulacyjnym
    3. przeliczać kwotę netto na podstawie znanej kwoty brutto („odrachowanie” VAT)
    4. stosować funkcję `ZAOKR` do prawidłowego zaokrąglania wyliczeń finansowych do 2 miejsc po przecinku
    5. tworzyć i konfigurować Poprawność Danych (Validation Lists) — listy rozwijane stawki VAT
    6. stosować formułę warunkową `JEŻELI` do automatycznego przydzielania rabatów lub narzutów
    7. konstruować arkusz symulacji finansowej oferty (wariant tani vs wariant rozszerzony)
    8. stosować adresowanie względne i bezwzględne (blokowanie komórki znakiem `$`)
    9. formatować komórki finansowe (zastosowanie czerwonego koloru dla ujemnych bilansów)
    10. projektować przejrzysty arkusz kalkulacyjny kalkulatora usług dla klienta

## 1. Podstawy wyliczeń podatkowych w firmie

W obrocie gospodarczym operujemy kwotami **netto** (cena bez podatku) oraz **brutto** (cena końcowa z podatkiem VAT).

```
KWOTA NETTO  *  (1 + STAWKA_VAT)  =  KWOTA BRUTTO
Przykładowo:  100 PLN * 1,23  =  123 PLN Brutto (VAT = 23 PLN)
```

### Podstawowe stawki podatku VAT w Polsce:

- **23%:** Stawka podstawowa (większość towarów, narzędzi i usług).
- **8%:** Stawka obniżona (usługi budowlane mieszkaniowe, wybrane towary).
- **5%:** Stawka obniżona (żywność, książki).

---

## 2. Adresowanie bezwzględne ($) i zaokrąglanie kwót

Przy wyliczaniu podatków i cen kluczowe jest prawidłowe blokowanie komórek ze stawkami oraz dbanie o dokładność groszową.

| Funkcja / Mechanizm | Wzór / Zapis | Zastosowanie |
| --- | --- | --- |
| **Adresowanie bezwzględne** | `$B$1` | Blokuje odwołanie do stawki VAT przy przeciąganiu formuły |
| **Zaokrąglanie kwot** | `=ZAOKR(A1*1,23; 2)` | Zaokrągla wynik dokładnie do 2 miejsc po przecinku (do groszy) |
| **Formuła warunkowa** | `=JEŻELI(A1>1000; A1*0,9; A1)` | Udziela 10% rabatu dla zamówień powyżej 1000 zł |

!!! info "Dlaczego używamy znaku dolara ($)?"

    Kiedy kopiujesz formułę `=A2*B1` w dół, arkusz zmienia ją na `=A3*B2`. Jeśli stawka VAT stoi tylko w komórce `B1`, musisz zapisać formułę jako `=A2*$B$1`. Znak `$` zapobiega przesuwaniu adresu komórki `B1`!

---

## 3. Formuła warunkowa JEŻELI i listy rozwijane

Aby arkusz działał jak profesjonalny kalkulator, warto umożliwić użytkownikowi wybór stawki VAT z listy oraz automatycznie naliczać upusty.

```
PRAWIDŁOWA SKŁADNIA FUNKCJI JEŻELI:
=JEŻELI(Warunek_Logiczny; Wartość_Gdy_Prawda; Wartość_Gdy_Fałsz)
Przykład: =JEŻELI(C2="TAK"; B2*0,95; B2)  <- Nalicza 5% rabatu
```

### Tworzenie listy rozwijanej:
1. Zaznacz komórkę -> Wybierz z menu *Dane -> Poprawność danych (Data Validation)*.
2. Wybierz *Kryteria: Lista*.
3. Wpisz stawki: `23%; 8%; 5%`.

!!! tip "Zaokrąglanie finansowe"

    Samo sformatowanie komórki na „2 miejsca po przecinku” zmienia tylko wyświetlany obraz, ale w pamięci komputera zostają ułamki grosza. Aby zapobiec błędom groszowym przy sumowaniu, zawsze używaj funkcji `=ZAOKR(wyrażenie; 2)`.

---

## 4. Instrukcja krok po kroku: Budowa kalkulatora usługi z podatkiem VAT i rabatem

1. **Krok 1:** Otwórz arkusz kalkulacyjny i utwórz nagłówki: *Nazwa materiału, Cena netto, Stawka VAT, Kwota VAT, Cena brutto*.
2. **Krok 2:** W osobnej komórce powyżej (np. `G1`) wpisz próg rabatowy `1000 PLN`.
3. **Krok 3:** W kolumnie *Stawka VAT* ustaw Poprawność Danych (Lista: `23%; 8%; 5%`).
4. **Krok 4:** W kolumnie *Kwota VAT* wpisz formułę `=ZAOKR(B2*C2; 2)` i przeciągnij w dół.
5. **Krok 5:** W kolumnie *Cena brutto* wpisz `=B2+D2`.
6. **Krok 6:** Pod tabelą stwórz komórkę *Wartość Razem*: `=SUMA(E2:E10)`.
7. **Krok 7:** W komórce *Cena Po Rabacie* wpisz formułę warunkową: `=JEŻELI(E11>$G$1; E11*0,9; E11)`.
8. **Krok 8:** Sformatuj wszystkie komórki finansowe na styl *Walutowy (PLN)*.
9. **Krok 9:** Przetestuj działanie kalkulatora, zmieniając stawki VAT i ilości materiałów.
10. **Krok 10:** Zapisz kalkulator pod nazwą `kalkulator_vat_uslugi.xlsx`.

!!! warning "Uważaj na wpisywanie stóp procentowych!"

    W arkuszu wartość `23%` to liczbowo `0,23`. Jeśli w formule wpiszesz `=A1*23`, pomnożysz kwotę przez 23 zamiast przez 0,23!

---

## Podsumowanie

Arkusz kalkulacyjny jest niezastąpionym narzędziem w zarządzaniu finansami małej firmy. Umiejętność obliczania podatku VAT, stosowania adresowania bezwzględnego (`$`), formuły `JEŻELI` oraz zaokrąglania kwót pozwala na tworzenie bezbłędnych wycen i kalkulacji finansowych.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Przygotuj prosty arkusz przeliczający 5 kwot netto na kwoty brutto przy stałej stawce VAT 23% umieszczonej w zablokowanej komórce `$B$1`.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Utwórz listę rozwijaną ze stawkami VAT (23%, 8%, 5%, 0%) i napisz formułę wyliczającą kwotę podatku z użyciem funkcji `ZAOKR`.
3. **Ćwiczenie 3 (Branżowe):** Zaprojektuj kalkulator usługowy dla Twojej branży (np. koszt wymiany części, robocizna, dojazd). Zastosuj funkcję `JEŻELI` naliczającą 10% zniżki dla stałych klientów.
4. **Ćwiczenie 4 (Zaawansowane):** Przygotuj arkusz symulacji finansowej zawierający dwa warianty wykonania usługi (Podstawowy i Premium), automatyczne wyliczenie podatku, marży zysku oraz wykres porównawczy obu wariantów.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Do czego służy znak dolara ($) w adresie komórki (np. $C$1) w arkuszu kalkulacyjnym?",
    "opcje": [
      "Do oznaczenia waluty amerykańskiej",
      "Do zablokowania adresu komórki (adresowanie bezwzględne), aby nie przesuwał się podczas kopiowania formuły",
      "Do usuwania błędów w tekstach",
      "Do automatycznego przeliczania na euro"
    ],
    "poprawna": 1,
    "wyjasnienie": "Znak $ blokuje kolumnę i/lub wiersz, gwarantując, że skopiowana formuła zawsze odwołuje się do tej samej komórki."
  },
  {
    "pytanie": "Jaka funkcja służy do zaokrąglania wyniku wyliczeń finansowych do 2 miejsc po przecinku?",
    "opcje": [
      "=ZAOKR(komórka; 2)",
      "=SUMA(komórka; 2)",
      "=SKRÓĆ(komórka)",
      "=PODATKI(2)"
    ],
    "poprawna": 0,
    "wyjasnienie": "Funkcja =ZAOKR(liczba; liczba_cyfr) matematycznie zaokrągla wartość do podanej liczby miejsc po przecinku."
  },
  {
    "pytanie": "Co się stanie, jeśli w formule wyliczającej VAT 23% zapiszesz wyrażenie =A1*23 zamiast =A1*23%?",
    "opcje": [
      "Obliczysz 23% kwoty",
      "Pomnożysz kwotę 23-krotnie zamiast obliczyć podatek",
      "Arkusz wyłączy komputer",
      "Nic się nie stanie, wynik będzie identyczny"
    ],
    "poprawna": 1,
    "wyjasnienie": "23% to w ułamku dziesiętnym 0,23. Wpisanie 23 oznacza pomnożenie wartości przez dwadzieścia trzy."
  },
  {
    "pytanie": "Jaka jest prawidłowa składnia funkcji warunkowej JEŻELI?",
    "opcje": [
      "=JEŻELI(Warunek; Wartość_Gdy_Prawda; Wartość_Gdy_Fałsz)",
      "=JEŻELI(Suma; Różnica)",
      "=JEŻELI(Prawda; Fałsz; Warunek)",
      "=JEŻELI(Data; Czas)"
    ],
    "poprawna": 0,
    "wyjasnienie": "Funkcja JEŻELI testuje warunek logiczny i zwraca pierwszą wartość, jeśli warunek jest spełniony, lub drugą, jeśli nie jest."
  },
  {
    "pytanie": "Gdzie w menu MS Excel / Calc znajduje się funkcja dodawania listy rozwijanej do komórki?",
    "opcje": [
      "Dane -> Poprawność danych / Walidacja danych (Data Validation)",
      "Widok -> Powiększenie",
      "Format -> Czcionka",
      "Wstaw -> Obraz"
    ],
    "poprawna": 0,
    "wyjasnienie": "Opcja Poprawność danych (Data Validation) pozwala ograniczyć wprowadzanie wartości do zdefiniowanej listy rozwijanej."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na MS Excel / LibreOffice Calc dla Szkół Branżowych.*
