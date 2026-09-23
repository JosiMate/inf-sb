# To nie jest trudne, czyli montujemy zdjęcie reklamowe

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 13**

!!! abstract "O tym temacie"

    Fotomontaż i przygotowanie grafiki promocyjnej to podstawowa umiejętność w marketingu i prezentacji produktów własnej firmy. W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się wykorzystywać mechanizm warstw, narzędzia zaznaczania, wycinania oraz dopasowania kolorystycznego w programie GIMP lub edytorze rastrowym do stworzenia profesjonalnego zdjęcia reklamowego.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie grafiki rastrowej oraz różnicę między nią a grafiką wektorową
    2. zdefiniować pojęcie i działanie warstw w edytorze graficznym (np. GIMP)
    3. stosować narzędzia zaznaczania (Prostokątne, Elipsa, Lasso, Różdżka)
    4. wycinać obiekty z tła z wykorzystaniem masek warstw lub przezroczystości (kanał Alpha)
    5. dodawać i formatować warstwy tekstowe na potrzeby haseł reklamowych
    6. dopasowywać jasność, kontrast, nasycenie i poziom kolorów montowanych elementów
    7. skalować, obracać i przekształcać obiekty na osobnych warstwach
    8. stosować tryby mieszania warstw (Mnożenie, Nakładka, Ekran) dla uzyskania efektów specjalnych
    9. eksportować gotowy projekt do formatu produkcyjnego (PNG, JPG) oraz zapisywać plik roboczy (XCF)
    10. przestrzegać praw autorskich przy doborze zdjęć składowych do fotomontażu

## 1. Zasada działania warstw w edytorze graficznym

Warstwy w programie graficznym (takim jak GIMP, Photoshop czy Photopea) przypominają **przezroczyste folie ułożone jedna na drugiej**. Każda folia może zawierać osobny element: tło, wycięty produkt, napis reklamowy czy logo.

```
+---------------------------------------------------+
| [Warstwa 3] Narzutka tekstowa / Logo (.PNG)       |  <- Na samej górze
+---------------------------------------------------+
| [Warstwa 2] Wycięty produkt (z kanałem Alpha)    |  <- W środku
+---------------------------------------------------+
| [Warstwa 1] Tło reklamowe / Zdjęcie plenerowe     |  <- Na samym dole
+---------------------------------------------------+
```

### Dlaczego warto stosować warstwy?

- **Bezpieczeństwo edycji:** Modyfikacja jednego elementu (np. zmiana koloru napisu) nie niszczy zdjęcia tła.
- **Niezależne przekształcenia:** Każdy obiekt można osobno skalować, obracać, przesuwać i filtrować.
- **Kanał Alpha (Przezroczystość):** Pozwala na łagodne wycinanie obiektów z tła bez białych ramki.

---

## 2. Narzędzia zaznaczania i wycinania obiektów

Kluczem do udanego montażu jest precyzyjne odseparowanie produktu od pierwotnego tła.

| Narzędzie GIMP | Zastosowanie | Skrót |
| --- | --- | --- |
| **Różdżka (Fuzzy Select)** | Zaznacza obszary o podobnym kolorze (idealna dla jednolitego tła) | `U` |
| **Lasso (Free Select)** | Ręczne obrysowywanie nieregularnych kształtów | `F` |
| **Inteligentne Nożyce (Scissors)** | Automatycznie przyciągają krawędź do linii kontrastu | `I` |
| **Ścieżki (Paths)** | Najbardziej precyzyjne wycinanie wektorowe krawędzi | `B` |

!!! info "Co to jest kanał Alpha?"

    Kanał Alpha odpowiada za informację o przezroczystości pikseli. Jeśli warstwa nie posiada kanału Alpha, usunięcie zaznaczonego tła odsłoni domyślny kolor tła (np. biały) zamiast przezroczystości (szarej kratki). W GIMP dodasz go, klikając prawym przyciskiem myszy na warstwę i wybierając *Dodaj kanał alpha*.

---

## 3. Dopasowanie kolorystyczne i formatowanie tekstu

Po umieszczeniu produktu na nowym tle należy zadbać o spójność oświetlenia i kolorów:

- **Kolory -> Poziomy (Levels) / Krzywe (Curves):** Pozwalają wyrównać jasność i kontrast wklejonego obiektu z tłem.
- **Kolory -> Odcień i nasycenie (Hue-Saturation):** Służy do dopasowania temperatury barwowej.
- **Narzędzie Tekst (`T`):** Umożliwia wstawienie nagłówka promocyjnego. Pamiętaj o użyciu czytelnego kroju pisma i kontrastowego koloru.

```
Zdj. Surowe -> Wycięcie (Alpha) -> Nałożenie na tło -> Korekta kolorów -> Dodanie tekstu
```

!!! tip "Tryby mieszania warstw"

    Eksperymentuj z trybami mieszania warstw (Layer Modes). Tryb *Mnożenie (Multiply)* świetnie nadaje się do nakładania cieni, a tryb *Ekran (Screen)* do efektów świetlnych i błysków.

---

## 4. Instrukcja krok po kroku: Tworzenie baneru reklamowego narzędzia / usługi

1. **Krok 1:** Otwórz program GIMP i utwórz nowy dokument o wymiarach `1920x1080` pikseli (*Plik -> Nowy*).
2. **Krok 2:** Wczytaj zdjęcie tła warsztatu (*Plik -> Otwórz jako warstwy*).
3. **Krok 3:** Wczytaj zdjęcie produktu (np. wkrętarki lub wyrobu stolarskiego) jako kolejną warstwę.
4. **Krok 4:** Kliknij prawym przyciskiem myszy na warstwę z produktem i wybierz *Dodaj kanał alpha*.
5. **Krok 5:** Wybierz narzędzie *Różdżka* lub *Lasso*, zaznacz tło wokół produktu i naciśnij `Delete`.
6. **Krok 6:** Użyj narzędzia *Skalowanie* (`Shift + S`), aby dopasować wielkość produktu do baneru.
7. **Krok 7:** Wybierz menu *Kolory -> Jasność i kontrast*, aby zsynchronizować oświetlenie produktu z tłem.
8. **Krok 8:** Wybierz narzędzie *Tekst* (`T`) i dodaj napis „PROMOCJA -20%” oraz logo.
9. **Krok 9:** Zapisz plik roboczy projektu jako `reklama.xcf` (*Plik -> Zapisz jako*).
10. **Krok 10:** Wyeksportuj gotową grafikę do formatu JPG lub PNG (*Plik -> Wyeksportuj jako*).

!!! warning "Pamiętaj o pliku roboczym!"

    Pliki PNG i JPG scalają wszystkie warstwy w jeden obraz. Aby zachować możliwość późniejszej edycji tekstu lub wyciętego obiektu, zawsze zachowaj plik projektowy (`.xcf` w GIMP, `.psd` w Photoshopie/Photopea).

---

## Podsumowanie

Montaż zdjęcia reklamowego w edytorze grafiki rastrowej polega na umiejętnej pracy z warstwami, precyzyjnym wycinaniu elementów, dopasowaniu tonalnym oraz doborze czytelnej typografii. Zrozumienie kanału Alpha oraz trybów mieszania pozwala tworzyć estetyczne i skuteczne materiały promocyjne.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Utwórz prosty dokument z dwoma warstwami: tłem jednokolorowym oraz wyciętym prostokątnym zdjęciem wyrobu branżowego. Dodaj prosty napis z nazwą firmy.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Wytnij za pomocą *Różdżki* lub *Lasso* skomplikowany produkt ze zdjęcia z niejednolitym tłem i wklej go na plenerowe tło reklamowe. Dodaj cień pod obiektem.
3. **Ćwiczenie 3 (Branżowe):** Przygotuj grafikę promocyjną na portal społecznościowy przedstawiającą produkt lub usługę z Twojej branży (np. naprawa auta, mebel na wymiar, usługa fryzjerska/gastronomiczna). Użyj tekstu, logo i ozdobnej ramki.
4. **Ćwiczenie 4 (Zaawansowane):** Zastosuj maskę warstwy (Layer Mask) oraz gradient do łagodnego przejścia (przenikania) dwóch zdjęć tła w projekcie reklamowym.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Do czego służą warstwy w programie graficznym?",
    "opcje": [
      "Do szybszego drukowania dokumentów",
      "Do układania elementów obrazu na osobnych przezroczystych foliach pozwalających na ich niezależną edycję",
      "Do automatycznego tłumaczenia tekstu",
      "Do zabezpieczania komputera przed wirusami"
    ],
    "poprawna": 1,
    "wyjasnienie": "Warstwy pozwalają modyfikować, przesuwać i filtrować poszczególne elementy grafiki bez niszczenia pozostałych."
  },
  {
    "pytanie": "Co odpowiada za przezroczystość w plikach graficznych i edytorach rastrowych?",
    "opcje": [
      "Kanał Alpha",
      "Format MP3",
      "Paleta CMYK",
      "Filtr Rozmycie Gaussa"
    ],
    "poprawna": 0,
    "wyjasnienie": "Kanał Alpha przechowuje informacje o stopniu przezroczystości poszczególnych pikseli obrazu."
  },
  {
    "pytanie": "Który format pliku zachowuje niewykasowane warstwy i pozwala na późniejszą edycję projektu w programie GIMP?",
    "opcje": [
      ".JPG",
      ".PNG",
      ".XCF",
      ".MP4"
    ],
    "poprawna": 2,
    "wyjasnienie": "Format .XCF jest natywnym formatem projektu programu GIMP, który przechowuje wszystkie warstwy, maski i ścieżki."
  },
  {
    "pytanie": "Które narzędzie w programie GIMP najlepiej sprawdza się przy zaznaczaniu jednolitego tła (np. białego ściany)?",
    "opcje": [
      "Różdżka (Fuzzy Select)",
      "Pędzel",
      "Gumka",
      "Kadrowanie"
    ],
    "poprawna": 0,
    "wyjasnienie": "Różdżka automatycznie zaznacza ciągłe obszary o podobnym kolorze lub odcieniu."
  },
  {
    "pytanie": "Dlaczego do publikacji w internecie grafiki z przezroczystym tłem wybieramy format PNG zamiast JPG?",
    "opcje": [
      "Format JPG nie obsługuje kanału Alpha (przezroczystości)",
      "Format PNG jest zawsze mniejszy o 90%",
      "Format JPG można otworzyć tylko w kalkulatorze",
      "Nie ma żadnej różnicy"
    ],
    "poprawna": 0,
    "wyjasnienie": "Standard JPG nie obsługuje przezroczystości – piksele przezroczyste są zastępowane jednokolorowym (zazwyczaj białym) tłem."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na edytorze GIMP / Photopea dla Szkół Branżowych.*
