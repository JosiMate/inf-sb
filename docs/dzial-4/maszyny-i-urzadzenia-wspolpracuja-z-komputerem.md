# Nie tylko w biurze, czyli maszyny i urządzenia także współpracują z komputerem

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 23**

!!! abstract "O tym temacie"

    Nowoczesne przetwórstwo, przemysł, elektronika i automatyka bazują na maszynach sterowanych komputerowo. W ramach tej lekcji (1h) w Dziale IV serwisu `inf-sb` dla Szkoły Branżowej nauczysz się rozpoznawać rolę mikrosterowników, komputerów jednopłytkowych (np. Raspberry Pi, Arduino), maszyn CNC, obrabiarek oraz robotów przemysłowych. Poznasz również zasady sterowania algorytmicznego i symulowania pracy robotów w środowiskach bloczkowych (np. Scratch).

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie mikrosterownika i mikrokontrolera jednopłytkowego
    2. rozróżniać zadania komputera biurowego od komputera sterującego procesem technologicznym
    3. wyjaśnić pojęcie i rozwinięcie skrótu CNC (Computer Numerical Control)
    4. opisać cykl powstawania wyrobu na maszynach CNC (Projekt CAD -> Program CAM / G-Code -> Obróbka CNC)
    5. wymieniać rodzaje maszyn sterowanych numerycznie (frezarki, tokarki, wycinarki laserowe, drukarki 3D)
    6. opisać rolę robotów przemysłowych w automatyzacji linii produkcyjnych i warsztatowych
    7. układać schemat blokowy / algorytm sterowania pracą prostego robota
    8. pisać i testować programy symulujące pracę robota (np. segregowanie detali wg koloru w Scratch)
    9. identyfikować czujniki (sensory) i elementy wykonawcze (aktulatory) w maszynach
    10. przestrzegać zasad BHP przy pracy i przebywaniu w strefie działania maszyn i robotów CNC

## 1. Komputery jednopłytkowe i mikrosterowniki w technice

Komputer w pracy zawodowej to nie tylko jednostka stacjonarna pod biurkiem. Sercem nowoczesnych maszyn, podnośników, obrabiarek czy pieców są **mikrosterowniki** i **komputery jednopłytkowe** (SBC - Single Board Computer).

```
+-----------------------------------------------------------------------+
|  ARCHITEKTURA STEROWANIA MASZYNĄ                                      |
|  CZUJNIKI (Sensory)  -->  MIKROSTEROWNIK / PLC  -->  ELEMENTY WYKONAWCZE|
|  - Czujnik koloru         (Przetwarzanie             - Silnik krokowy |
|  - Czujnik zbliżeniowy     wg algorytmu)             - Siłownik       |
|  - Przycisk stopu                                    - Chwytak        |
+-----------------------------------------------------------------------+
```

### Przykłady platform sterujących:

- **Mikrosterowniki (np. Arduino, sterowniki PLC):** Przeznaczone do odczytywania sygnałów z czujników i natychmiastowego sterowania przekaźnikami i silnikami.
- **Komputery jednopłytkowe (np. Raspberry Pi):** Posiadają pełny system operacyjny, złącza sieciowe oraz uogólnione wejścia/wyjścia (GPIO).

---

## 2. Maszyny CNC (Computer Numerical Control)

Maszyny **CNC** to urządzenia produkcyjne sterowane numerycznie za pomocą programu komputerowego (tzw. kodu G / *G-Code*).

| Etap procesu CNC | Narzędzie / Oprogramowanie | Rola w procesie |
| --- | --- | --- |
| **1. Projektowanie (CAD)** | Fusion 360, AutoCAD, SolidWorks | Stworzenie modelu 3D wyrobu |
| **2. Wytwarzanie (CAM)** | Oprogramowanie CAM | Wygenerowanie ścieżki narzędzia i kodu G |
| **3. Obróbka (CNC)** | Frezarka, tokarka, laser | Wycięcie wyrobu ze stali, drewna lub tworzywa |

!!! info "Dlaczego obróbka CNC zastępuje pracę ręczną?"

    Maszyny CNC zapewniają **powtarzalność z dokładnością do setnych części milimetra**, eliminują błędy ludzkie, drastycznie skracają czas wykonania i pozwalają na bezpieczną pracę w trudnych warunkach.

---

## 3. Algorytmy sterowania robotem (Scratch / Schematy)

Praca każdego robota przemysłowego (np. ramienia spawalniczego lub robota paletyzującego) opiera się na **pętli algorytmicznej** sprawdzającej warunki.

```
PĘTLA (Zawsze):
  Odczytaj czujnik koloru.
  JEŻELI Kolor == "Czerwony" TO:
    Uruchom siłownik 1 (Odrzuć do pojemnika A)
  W PRZECIWNYM RAZIE:
    Uruchom taśmociąg (Przesuń do pojemnika B)
```

!!! tip "Bezpieczeństwo w strefie robota"

    Roboty przemysłowe poruszają się z dużymi prędkościami i siłą. Strefa pracy robota musi być wygrodzona barierkami lub kurtynami świetlnymi (czujnikami optycznymi), które natychmiast zatrzymują maszynę w przypadku wejścia człowieka.

---

## 4. Instrukcja krok po kroku: Programowanie symulacji robota segregującego detale w Scratch

1. **Krok 1:** Otwórz środowisko Scratch (`scratch.mit.edu`).
2. **Krok 2:** Stwórz duszka reprezentującego ramie robota oraz duszka reprezentującego taśmociąg.
3. **Krok 3:** Utwórz zmienną `CzujnikKoloru`.
4. **Krok 4:** Dodaj bloki pętli głównej: `Zawsze (Forever)`.
5. **Krok 5:** Wstaw blok warunkowy `Jeżeli <dotyka koloru [czerwony]> to`.
6. **Krok 6:** Wewnątrz warunku dodaj komendę przesunięcia ramienia robota o 100 kroków w prawo (pojemnik A).
7. **Krok 7:** W sekcji `W przeciwnym razie` przesuń detal prosto po taśmie (pojemnik B).
8. **Krok 8:** Przetestuj działanie symulacji, przesuwając obiekty o różnych kolorach.
9. **Krok 9:** Przeanalizuj, jak dodać czujnik awaryjny *STOP*.
10. **Krok 10:** Zapisz projekt pod nazwą `symulacja_robota_cnc.sb3`.

!!! warning "Uwaga na pętle zawieszenia!"

    W algorytmach sterowania maszyn każdy stan musi mieć określony czas trwania lub warunek wyjścia. Pętla bez warunku przerwania powoduje zablokowanie programu sterującego.

---

## Podsumowanie

Komputery i urządzenia peryferyjne to nie tylko sprzęt biurowy, ale przede wszystkim systemy sterowania maszyn przemysłowych. Znajomość pojęć CNC, mikrosterowników, czujników oraz układania algorytmów sterowania robotami stanowi fundament nowoczesnej automatyki w każdym zawodzie.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Wyjaśnij rozwinięcie skrótu CNC oraz podaj 3 przykłady maszyn sterowanych numerycznie stosowanych w Twoim zawodzie.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Narysuj schemat blokowy algorytmu sterującego automatyczną bramą wjazdową (czujnik ruchu, otwieranie, odczekanie 10 sekund, zamykanie).
3. **Ćwiczenie 3 (Branżowe):** Przygotuj w środowisku Scratch lub w postaci kroków algorytmu program symulujący pracę robota lakierniczego/sortującego wyroby w Twojej branży.
4. **Ćwiczenie 4 (Zaawansowane):** Opracuj kompletny opis procesu produkcyjnego wybranego elementu: od trójwymiarowego projektu CAD, przez wygenerowanie kodu G w programie CAM, po obróbkę na frezarce CNC.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Co oznacza skrót CNC w odniesieniu do maszyn produkcyjnych?",
    "opcje": [
      "Computer Numerical Control (Komputerowe Sterowanie Numeryczne)",
      "Central Network Center (Centralny Ośrodek Sieciowy)",
      "Cut and Clean (Tnij i Czyść)",
      "Control New Car (Sterowanie Nowym Autem)"
    ],
    "poprawna": 0,
    "wyjasnienie": "CNC to skrót od Computer Numerical Control, czyli automatycznego sterowania obrabiarek za pomocą programu komputerowego."
  },
  {
    "pytanie": "Jaka jest prawidłowa kolejność etapów cyklu produkcyjnego elementu na maszynie CNC?",
    "opcje": [
      "Projekt CAD -> Kod G w programie CAM -> Obróbka na maszynie CNC",
      "Obróbka CNC -> Projekt CAD -> Sprzedaż",
      "Rysunek ołówkiem -> Formatowanie dysku -> Malowanie",
      "Wykres w Excelu -> Druk na papierze -> Montaż"
    ],
    "poprawna": 0,
    "wyjasnienie": "Proces rozpoczyna się od projektu 3D w CAD, następnie w CAM generuje się ścieżkę narzędzia (kod G), a na końcu maszyna CNC wykonuje obróbkę."
  },
  {
    "pytanie": "Czym różni się mikrosterownik (np. w pralce lub maszynie CNC) od zwykłego komputera biurowego?",
    "opcje": [
      "Jest wyspecjalizowany do realizowania jednego konkretnego programu sterującego urządzeniem w czasie rzeczywistym",
      "Mikrosterownik nie potrzebuje prądu",
      "Mikrosterownik służy tylko do grania w gry",
      "Nie ma żadnych różnic"
    ],
    "poprawna": 0,
    "wyjasnienie": "Mikrosterowniki są zaprojektowane do dedykowanych zadań sterowania i pomiarów bez konieczności obsługi pełnego systemu operacyjnego."
  },
  {
    "pytanie": "Do czego służą sensory (czujniki) w robotach przemysłowych?",
    "opcje": [
      "Do zbierania informacji z otoczenia (np. temperatura, kolor, odległość, położenie)",
      "Do ozdabiania obudowy",
      "Do odtwarzania muzyki",
      "Do kasowania plików"
    ],
    "poprawna": 0,
    "wyjasnienie": "Sensory przekazują do sterownika dane o stanie otoczenia i pozycji detali, co pozwala robotowi podjąć decyzję."
  },
  {
    "pytanie": "Co to jest sterowanie w pętli zamkniętej w automatyce?",
    "opcje": [
      "Sterowanie, w którym sygnał z czujnika powraca do sterownika (sprzężenie zwrotne) w celu korekty działania maszyny",
      "Zamknięcie drzwiczek od szafy",
      "Brak połączenia z internetem",
      "Wyłączenie zasilania"
    ],
    "poprawna": 0,
    "wyjasnienie": "Sprzężenie zwrotne pozwala sterownikowi sprawdzić, czy ruch został wykonany poprawnie i ewentualnie skorygować pozycję ramienia."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na standardach CNC i Scratch dla Szkół Branżowych.*
