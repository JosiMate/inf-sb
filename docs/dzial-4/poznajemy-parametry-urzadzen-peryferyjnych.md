# Kupujemy świadomie, czyli poznajemy parametry urządzeń peryferyjnych

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 22**

!!! abstract "O tym temacie"

    Świadomy dobór urządzeń peryferyjnych do stanowiska pracy w firmie pozwala zoptymalizować koszty eksploatacji, zapewnić odpowiednią jakość wydruków oraz ergonomię pracy. W ramach tej lekcji (1h) w Dziale IV serwisu `inf-sb` dla Szkoły Branżowej nauczysz się analizować parametry techniczne drukarek (atramentowych, laserowych, igłowych, termicznych), monitorów (przekątna, matryca, interfejsy) oraz szacować Całkowity Koszt Posiadania (TCO - Total Cost of Ownership).

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wymienić i wyjaśnić podstawowe parametry drukarek (DPI, PPM, duplex, cykl pracy)
    2. porównać technologie druku: atramentową, laserową (monochromatyczną i kolorową), termiczną oraz igłową
    3. oszacować koszt jednostkowy wydruku jednej strony i wyliczyć wskaźnik TCO
    4. identyfikować i dobierać złącza i interfejsy wideo monitorów (HDMI, DisplayPort, USB-C, VGA)
    5. wyjaśnić kluczowe parametry monitorów (przekątna, rozdzielczość, typ matrycy IPS/VA/TN, jasność, czas reakcji)
    6. stosować zasady doboru monitora do wymogów ergonomii na stanowisku pracy
    7. interpretować parametry skanerów (rozdzielczość optyczna vs interpolowana, głębia koloru)
    8. dobierać drukarkę etykiet / kodów kreskowych do pracy w magazynie lub warsztacie
    9. analizować specyfikacje katalogowe urządzeń peryferyjnych pod kątem wymagań branżowych
    10. wybierać urządzenia peryferyjne spełniające kryteria ekologiczne i oszczędności energii (Energy Star)

## 1. Technologie i parametry drukarek

Dobór drukarki do firmy zależy od wolumenu druku, wymaganej trwałości oraz budżetu na materiały eksploatacyjne.

```
+-----------------------------------------------------------------------+
|  PARAMETRY KLUCZOWE DRUKARKI                                          |
|  - DPI (Dots Per Inch)     --> Rozdzielczość punktów na cal          |
|  - PPM (Pages Per Minute)  --> Szybkość druku (stron na minutę)      |
|  - Duplex                  --> Automatyczny druk dwustronny           |
|  - TCO                     --> Całkowity koszt posiadania urządzenie  |
+-----------------------------------------------------------------------+
```

### Porównanie technologii druku:

- **Laserowa (Monochromatyczna / Kolor):** Wysoka szybkość, niski koszt strony przy dużych nakładach, odporność toneru na wilgoć. Idealna do biura i warsztatu.
- **Atramentowa:** Wysoka jakość wydruku zdjęć i grafik, wyższy koszt przy rzadkim używaniu (ryzyko zasychania głowicy).
- **Termiczna / Termotransferowa:** Szybki druk etykiet, paragonów i kodów kreskowych bez użycia tuszu (papier termiczny).
- **Igłowa (Mozaikowa):** Druk wielokrotny na papierze samokopiującym (faktury, list przewozowy).

---

## 2. Szacowanie kosztów eksploatacji (TCO)

Sama cena zakupu drukarki bywa złudna. Drukarka za 200 zł może generować koszt wydruku jednej strony na poziomie 50 groszy, podczas gdy urządzenie za 800 zł drukuje tę samą stronę za 5 groszy!

| Element kalkulacji TCO | Opis |
| --- | --- |
| **Cena zakupu sprzętu** | Koszt początkowy |
| **Wydajność bębna / toneru** | Liczba stron wydrukowanych z jednego kartridża (np. 3000 stron) |
| **Cena toneru / tuszu** | Koszt zakupu nowego materiału eksploatacyjnego |
| **Wzór na koszt 1 strony** | `Cena_toneru / Wydajność_toneru` |

!!! info "Przykład kalkulacji TCO"

    Toner do drukarki A kosztuje 150 zł i wystarcza na 3000 stron. Koszt 1 strony wynosi: `150 / 3000 = 0,05 zł (5 groszy)`. Jeśli firma drukuje 2000 stron miesięcznie, oszczędność w skali roku wyniesie kilkaset złotych.

---

## 3. Parametry monitorów i złącza sygnałowe

Monitor na stanowisku pracy odpowiada za wzrok i komfort pracownika.

```
+-----------------------------------------------------------------------+
|  INTERFEJSY WIDEO:                                                    |
|  - HDMI        --> Cyfrowy przesył obrazu i dźwięku (standard)         |
|  - DisplayPort --> Cyfrowy interfejs profesjonalny / przemysłowy      |
|  - USB-C (DP)  --> Jeden przewód: obraz, dane i zasilanie laptopa     |
|  - VGA (D-Sub) --> Przestarzały interfejs analogowy (niebieska wtyczka) |
+-----------------------------------------------------------------------+
```

### Typy matryc w monitorach:

- **IPS:** Bardzo dobre odwzorowanie kolorów i szerokie kąty widzenia (idealny do grafiki i pracy biurowej).
- **VA:** Wysoki kontrast i głęboka czerń (dobry do tekstów i multimediów).
- **TN:** Szybki czas reakcji, ale słabsze kolory i kąty widzenia.

!!! tip "Ergonomia stanowiska"

    Monitor powinien posiadać regulację wysokości (HAS), funkcję usuwania migotania (*Flicker-Free*) oraz filtr światła niebieskiego (*Low Blue Light*).

---

## 4. Instrukcja krok po kroku: Analiza karty katalogowej i dobór urządzenia peryferyjnego

1. **Krok 1:** Otwórz specyfikację katalogową wybranego urządzenia (np. drukarki wielofunkcyjnej).
2. **Krok 2:** Odczytaj podaną przez producenta rozdzielczość `DPI` (np. 1200x1200 DPI) oraz szybkość `PPM`.
3. **Krok 3:** Odczytaj normatywny miesięczny cykl pracy (np. do 10 000 stron/miesiąc).
4. **Krok 4:** Znajdź symbol dedykowanego toneru/tuszu oraz jego deklarowaną wydajność wg normy ISO.
5. **Krok 5:** Oblicz koszt wydruku jednej strony (`Cena_toneru / Liczba_stron`).
6. **Krok 6:** Sprawdź dostępne interfejsy komunikacyjne (USB, LAN, Wi-Fi, AirPrint).
7. **Krok 7:** Sprawdź w specyfikacji monitora obecność wejść `HDMI` i `DisplayPort` oraz typ matrycy.
8. **Krok 8:** Zestaw ze sobą dwa konkurencyjne modele w arkuszu kalkulacyjnym.
9. **Krok 9:** Wskaż model optymalny dla małego warsztatu / biura z uzasadnieniem ekonomicznym.
10. **Krok 10:** Zapisz analizę do pliku PDF.

!!! warning "Unikaj rozdzielczości interpolowanej!"

    Producenci skanerów i aparatów podają czasem tzw. *rozdzielczość interpolowaną* (sztucznie powiększoną przez algorytm komputera). Zawsze należy kierować się **rozdzielczością optyczną** przetwornika!

---

## Podsumowanie

Świadomy zakup urządzeń peryferyjnych wymaga analizy parametrów technicznych i szacowania kosztów eksploatacji. Wybór drukarki laserowej do dużych nakładów, znajomość typów matryc monitorów (IPS, VA) oraz złączy sygnałowych (HDMI, DisplayPort) pozwala stworzyć wydajne i bezpieczne dla zdrowia stanowisko pracy.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Rozpoznaj i opisz złącza sygnałowe z tyłu komputera/monitora (HDMI, DisplayPort, USB, VGA).
2. **Ćwiczenie 2 (Średnio zaawansowane):** Porównaj koszty wydruku 1000 stron na podstawie cen tonerów dla dwóch wybranych modeli drukarek laserowych.
3. **Ćwiczenie 3 (Branżowe):** Dobierz zestaw urządzeń peryferyjnych (monitor, drukarka, skaner/czytnik) dla stanowiska przyjęć w Twojej branży (np. serwis samochodowy, recepcja, magazyn). Uzasadnij wybór.
4. **Ćwiczenie 4 (Zaawansowane):** Przygotuj w arkuszu kalkulacyjnym pełną symulację TCO (Total Cost of Ownership) dla 3-letniego okresu użytkowania drukarki atramentowej i laserowej przy założeniu druku 500 stron miesięcznie.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Co oznacza wskaźnik PPM w specyfikacji technicznej drukarki?",
    "opcje": [
      "Pages Per Minute (Liczba stron wydrukowanych na minutę)",
      "Pixels Per Meter (Liczba pikseli na metr)",
      "Price Per Month (Cena miesięczna)",
      "Paper Power Mode (Oszczędzanie papieru)"
    ],
    "poprawna": 0,
    "wyjasnienie": "PPM (Pages Per Minute) określa szybkość druku wyrażoną w liczbie stron A4 wydrukowanych w ciągu jednej minuty."
  },
  {
    "pytanie": "Która technologia druku najlepiej sprawdza się w magazynie do drukowania samoprzylepnych etykiet z kodami kreskowymi?",
    "opcje": [
      "Druk termiczny / termotransferowy",
      "Druk igłowy",
      "Atramentowy druk fotograficzny",
      "Druk żelowy"
    ],
    "poprawna": 0,
    "wyjasnienie": "Drukarki termiczne są szybkie, tanie w eksploatacji (brak tuszu) i idealnie nadają się do etykiet i kodów kreskowych."
  },
  {
    "pytanie": "Jak obliczyć szacunkowy koszt toneru przypadający na jedną wydrukowaną stronę?",
    "opcje": [
      "Podzielić cenę zakupu toneru przez deklarowaną przez producenta wydajność w liczbie stron",
      "Pomnożyć wagę toneru przez cenę papieru",
      "Dodać cenę monitora do ceny drukarki",
      "Podzielić rozdzielczość DPI przez 100"
    ],
    "poprawna": 0,
    "wyjasnienie": "Koszt jednostkowy strony wylicza się ze wzoru: Cena_materiału / Wydajność_w_stronach."
  },
  {
    "pytanie": "Który typ matrycy monitora oferuje najlepsze odwzorowanie kolorów i najszersze kąty widzenia?",
    "opcje": [
      "IPS",
      "TN",
      "CGA",
      "Mono"
    ],
    "poprawna": 0,
    "wyjasnienie": "Matryce IPS słyną z bardzo wiernego odwzorowania barw oraz szerokich kątów widzenia (do 178 stopni)."
  },
  {
    "pytanie": "Które złącze jest przestarzałym interfejsem ANALOGOWYM do przesyłania obrazu do monitora?",
    "opcje": [
      "VGA (D-Sub)",
      "DisplayPort",
      "HDMI",
      "USB-C"
    ],
    "poprawna": 0,
    "wyjasnienie": "Złącze VGA (D-Sub) to starszy standard przesyłu sygnału analogowego, zastąpiony przez cyfrowe HDMI i DisplayPort."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na normach ISO i specyfikacjach sprzętowych dla Szkół Branżowych.*
