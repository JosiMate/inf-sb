# Wizualizacja pomysłów, czyli projektujemy w edytorze 3D

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 12**

!!! abstract "O tym temacie"

    Wizualizacja 3D w edytorze CAD / budowlanym umożliwia szybkie przekształcenie szkicu w trójwymiarowy projekt architektoniczny lub wzorniczy. W ramach tego tematu (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się projektować obiekty architektoniczne i przestrzenne w edytorze SketchUp, lokalizować je w terenie oraz przygotowywać modele do prezentacji zawodowej.

!!! success "Kryteria sukcesu"

    Po tej lekcji:
    1. Uruchomię i nawigować w środowisku edytora 3D (np. SketchUp)
    2. Wymienię i zastosuję narzędzia rysowania 2D (linia, prostokąt, okrąg) do tworzenia rzutów
    3. Zastosuję narzędzie Push/Pull (Wyciągnij) do przekształcania płaskich kształtów w bryły
    4. Nałożę materiały, kolory oraz tekstury na poszczególne ściany modelu
    5. Zaimportuję i dopasowywać podkłady mapowe oraz zdjęcia obiektów
    6. Przeglądać i wykorzystywać trójwymiarowe modele z biblioteki chmurowej 3D Warehouse
    7. Grupować elementy i utworzę komponenty w celu usprawnienia edycji
    8. Wymiarować obiekty i sprawdzać ich zgodność ze specyfikacją
    9. Ustalać położenie geograficzne modelu i przeanalizuję jego nasłonecznienie
    10. Wyeksportuję gotowy widok 3D do pliku graficznego na potrzeby dokumentacji

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Czym różni się siatka wielokątów (mesh) od bryły podstawowej w edytorze 3D?
    2. **Sprzed kilku tygodni.** Jakie są trzy podstawowe osie w przestrzeni 3D?
    3. **Z dawniejszych tematów.** Do czego służy operacja grupowa grupuj/grupuj obiekty w programach graficznych?

    ??? success "Odpowiedzi"

        1. Bryła podstawowa to prosty obiekt (np. sześcian), a siatka składa się z wierzchołków, krawędzi i ścianek tworzących złożony kształt.
        2. Osie X (szerokość), Y (głębokość/długość) i Z (wysokość).
        3. Połączenie kilku obiektów w jeden, aby łatwiej nimi przesuwać, skalować lub obracać.

## 1. Wprowadzenie do projektowania architektonicznego 3D

W pracy zawodowej — niezależnie od tego, czy kształcisz się w zawodzie budowlanym, stolarstwie, meblarstwie, czy mechanice — wizualizacja pomysłu jest kluczem do komunikacji z klientem. Zamiast rysować skomplikowane rzuty na papierze, edytory 3D takie jak **SketchUp** pozwalają na intuicyjne budowanie modeli trójwymiarowych.

```
+-----------------------------------------------------------------+
|                    ŚRODOWISKO SKETCHUP                           |
|  [Pasek Narzędzi]   [Obszar Rysunkowy / Osie X, Y, Z]           |
|  - Rysowanie (2D)   - Czerwona (X), Zielona (Y), Niebieska (Z)  |
|  - Modyfikacje      - Model / Obiekt 3D                         |
|  - Materiały        - Okno Właściwości i Materiałów             |
+-----------------------------------------------------------------+
```

### Podstawowe narzędzia nawigacji

- **Orbit (Obróć):** pozwala krążyć wokół modelu we wszystkich kierunkach (użyj kółka myszy / wciśnij kółko).
- **Pan (Przesuń):** przesuwa widok w płaszczyźnie ekranu (Shift + kółko myszy).
- **Zoom (Powiększ/Zmniejsz):** przewijanie kółka myszy.

---

## 2. Tworzenie brył z płaskich konturów

Główną techniką pracy w SketchUp jest rysowanie płaskich kształtów na płaszczyźnie, a następnie wyciąganie ich w trzeci wymiar.

| Narzędzie | Działanie | Skrót / Ikona |
| --- | --- | --- |
| **Prostokąt (Rectangle)** | Tworzy płaską powierzchnię o podanych wymiarach | `R` |
| **Push/Pull (Wyciągnij)** | Rozciąga płaszczyznę w górę lub w dół, tworząc bryłę | `P` |
| **Miarka (Tape Measure)** | Wyznacza linie pomocnicze oraz mierzy odległości | `T` |
| **Przesuń (Move)** | Przesuwa lub kopiuje wybrane krawędzie i ściany | `M` |

!!! info "Precyzja wymiarowania"

    Podczas rysowania prostokąta lub wyciągania ściany nie musisz precyzyjnie trafiać myszką. Po rozpoczęciu ruchu wpisz na klawiaturze dokładne wymiary (np. `4,5` lub `400;300`) i naciśnij `Enter`.

---

## 3. Praca z materiałami, komponentami i chmurą 3D

Aby model wyglądał realistycznie, należy nałożyć na niego materiały oraz skorzystać z gotowych bibliotek.

```
1. Rysowanie obrysu (2D) -> 2. Wyciągnięcie (Push/Pull) -> 3. Nałożenie materiału (Pędzel) -> 4. Zapis jako Komponent
```

### Wzbogacanie modelu:

- **Narzędzie Wiadro z farbą (Paint Bucket):** Pozwala wybrać teksturę (drewno, cegła, szkło, metal, trawa) i nałożyć ją na wybrane ściany.
- **Grupy i Komponenty:** Zaznacz elementy obiektu i wybierz *Make Component*. Dzięki temu obiekt nie „skleja się” z innymi elementami, a jego modyfikacja automatycznie zmienia wszystkie jego kopie.
- **3D Warehouse:** Zintegrowana biblioteka chmurowa, z której można bezpłatnie pobierać modele mebli, pojazdów, roślinności czy wyposażenia warsztatu.

!!! tip "Geolokalizacja i cienie"

    W SketchUp możesz przypisać modelowi realne położenie geograficzne (np. wybraną działkę w Twoim mieście). Pozwala to włączyć **Analizę Cieni (Shadows)** i sprawdzić, jak słońce będzie oświetlać obiekt o różnej porze dnia i roku.

---

## 4. Instrukcja krok po kroku: Projekt prostego pawilonu / wiaty warsztatowej

1. **Krok 1:** Wybierz szablon z jednostkami metrycznymi (Metry lub Milimetry).
2. **Krok 2:** Wybierz narzędzie *Prostokąt* (`R`), kliknij w punkcie początkowym osi i wpisz `6;4` (budynek 6m x 4m).
3. **Krok 3:** Wybierz *Push/Pull* (`P`), kliknij wewnątrz prostokąta i wyciągnij go w górę na wysokość `3` metrów.
4. **Krok 4:** Za pomocą narzędzia *Rysuj linię* (`L`) podziel górną ścianę na pół i wyciągnij środkową krawędź w górę, tworząc dach dwuspadowy.
5. **Krok 5:** Narzędziem *Wiadro z farbą* nałóż cegłę na ściany oraz dachówkę na dach.
6. **Krok 6:** Otwórz okno *3D Warehouse*, wyszukaj „drzwi warsztatowe” i wstaw je do modelu.
7. **Krok 7:** Wykonaj eksport widoku: *File -> Export -> 2D Graphic* i zapisz plik jako JPG.

!!! warning "Częsty błąd: Sklejanie geometrii"

    Jeśli nie zamienisz narysowanego obiektu w Grupę (*Make Group*) przed dorysowaniem kolejnego elementu, krawędzie obu obiektów trwale się ze sobą połączą.

---

## Podsumowanie

Wizualizacja w edytorze 3D to potężne narzędzie do prezentowania pomysłów w pracy zawodowej. Znajomość układu osi, narzędzia Push/Pull, nakładania tekstur oraz korzystania z komponentów pozwala na szybkie przygotowanie profesjonalnego projektu wiaty, mebla lub detalu architektonicznego.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Zaprojektuj w edytorze 3D prostopadłościenny stolik warsztatowy o wymiarach 120 cm x 80 cm x 85 cm. Nałóż teksturę drewna na blat i metalu na nogi.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Utwórz model wiaty garażowej. Zastosuj narzędzie *Miarka* do wyznaczenia linii pomocniczych i wykonaj otwory okienne oraz drzwiowe.
3. **Ćwiczenie 3 (Branżowe):** Pobierz z *3D Warehouse* model maszyny lub mebla charakterystycznego dla Twojego zawodu, wstaw go do utworzonego pomieszczenia, ustaw odpowiednie oświetlenie/cienie i wyeksportuj plik JPG.
4. **Ćwiczenie 4 (Zaawansowane):** Zwymiaruj swój model za pomocą narzędzia *Dimension* i przygotuj prosty rzut z wymiarami do wydruku.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Które narzędzie w SketchUp służy do przekształcania płaskiego kształtu 2D w bryłę 3D?",
    "opcje": [
      "Orbit (Obróć)",
      "Push/Pull (Wyciągnij)",
      "Paint Bucket (Wiadro z farbą)",
      "Tape Measure (Miarka)"
    ],
    "poprawna": 1,
    "wyjasnienie": "Narzędzie Push/Pull (Wyciągnij) rozciąga płaską powierzchnię wzdłuż osi prostopadłej, tworząc bryłę 3D."
  },
  {
    "pytanie": "Co się stanie, jeśli przed dorysowaniem kolejnych elementów nie utworzysz Grupy ani Komponentu?",
    "opcje": [
      "Program automatycznie skasuje model",
      "Geometria nowych i starych obiektów trwale się sklei",
      "Model zmieni kolor na czerwony",
      "Plik zapisze się jako dokument tekstowy"
    ],
    "poprawna": 1,
    "wyjasnienie": "Niezgrupowana geometria w SketchUp 'skleja się' przy zetknięciu, co utrudnia późniejszą modyfikację poszczególnych elementów."
  },
  {
    "pytanie": "Czym jest biblioteka 3D Warehouse?",
    "opcje": [
      "Płatnym sklepem z narzędziami",
      "Chmurową biblioteką darmowych, gotowych modeli 3D",
      "Programem do antywirusowego skanowania modeli",
      "Wtyczką do przeliczania podatków"
    ],
    "poprawna": 1,
    "wyjasnienie": "3D Warehouse to oficjalna chmurowa biblioteka użytkowników SketchUp zawierająca miliony darmowych modeli 3D."
  },
  {
    "pytanie": "Skrót klawiszowy Shift + kółko myszy odpowiada w nawigacji za funkcję:",
    "opcje": [
      "Pan (Przesuń widok)",
      "Orbit (Acrobat)",
      "Eksport do PDF",
      "Kasowanie zaznaczenia"
    ],
    "poprawna": 0,
    "wyjasnienie": "Wciśnięcie kółka myszy wraz z klawiszem Shift aktywuje narzędzie Pan (przesuwanie widoku w płaszczyźnie ekranu)."
  },
  {
    "pytanie": "Do czego służy funkcja Analizy Cieni (Shadows)?",
    "opcje": [
      "Do wykrywania błędów w kodzie programu",
      "Do symulowania oświetlenia słonecznego w zależności od położenia i pory dnia",
      "Do zmniejszania rozmiaru pliku",
      "Do automatycznego malowania ścian"
    ],
    "poprawna": 1,
    "wyjasnienie": "Funkcja Cieni pozwala sprawdzić, jak słońce oświetla obiekt o konkretnej godzinie w danym dniu roku i w określonej lokalizacji."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na edytorze SketchUp dla Szkół Branżowych.*
