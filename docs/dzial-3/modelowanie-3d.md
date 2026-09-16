# Modelujemy, czyli jak projektować obiekty 3D

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 11**

Wyobraź sobie, że chcesz stworzyć nową obudowę do telefonu, uchwyt na narzędzia w warsztacie albo element maszyny, którego nie można kupić w sklepie. Zamiast rzeźbić w plastiku czy drewnie metodą prób i błędów, możesz najpierw stworzyć idealny model w komputerze. Modelowanie 3D to dzisiaj nie tylko domena gier i filmów, ale przede wszystkim potężne narzędzie w przemyśle, budownictwie i rzemiośle.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. zdefiniować pojęcie modelowania 3D i odróżnić je od rysunku 2D
    2. zidentyfikować trzy osie układu współrzędnych (X, Y, Z) i ich znaczenie
    3. wymienić podstawowe bryły (prymitywy) używane w modelowaniu
    4. wyjaśnić podstawowe operacje modelowania: wyciąganie, skalowanie i operacje boole'owskie
    5. odróżnić modelowanie parametryczne (CAD) od rzeźbienia cyfrowego (sculpting)

## 1. Czym jest modelowanie 3D?

W tradycyjnym rysunku (2D) mamy tylko dwa wymiary: szerokość i wysokość. W modelowaniu 3D dodajemy trzeci wymiar — **głębię**.

**Modelowanie 3D** to proces tworzenia matematycznej reprezentacji dowolnego trójwymiarowego obiektu za pomocą specjalistycznego oprogramowania. Wynikiem pracy jest tzw. **model 3D**, który możemy oglądać z każdej strony, obracać, a w wielu przypadkach — wydrukować na drukarce 3D.

---

## 2. Przestrzeń 3D: Osie X, Y i Z

Aby komputer wiedział, gdzie w przestrzeni znajduje się dany punkt, używa układu współrzędnych. W 3D mamy trzy wzajemnie prostopadłe osie:

- **Oś X (szerokość)** — ruch w lewo i w prawo.
- **Oś Y (wysokość / głębokość)** — zależnie od programu, odpowiada za wysokość lub głębię.
- **Oś Z (głębokość / wysokość)** — trzecia oś, która nadaje obiektowi objętość.

!!! tip "Jak to zapamiętać?"
    Wyobraź sobie róg pokoju. Linia styku podłogi z jedną ścianą to oś X, linia styku podłogi z drugą ścianą to oś Y, a pionowy narożnik idący w górę do sufitu to oś Z.

---

## 3. Klocki budulcowe: Prymitywy

Większość skomplikowanych obiektów (np. silnik samochodu czy dom) powstaje z połączenia bardzo prostych brył, które nazywamy **prymitywami**.

Najpopularniejsze prymitywy to:
- **Sześcian (Cube)** — podstawa większości konstrukcji technicznych.
- **Sfera (Sphere)** — używana do tworzenia obłych kształtów.
- **Walec (Cylinder)** — idealny do rur, śrub i osi.
- **Stożek (Cone)** — stosowany w elementach stożkowych i ostrzach.
- **Torus (Torus)** — kształt pączka z dziurką, używany do uszczelek i pierścieni.

---

## 4. Podstawowe operacje modelowania

Samo postawienie sześcianu to nie projektowanie. Prawdziwa magia dzieje się, gdy zaczynamy modyfikować prymitywy:

### Wyciąganie (Extrude)
To jedna z najważniejszych funkcji. Polega na „wyciągnięciu” płaskiej powierzchni (2D) w głąb lub w górę, aby stworzyć bryłę (3D). 
*Przykład: Rysujesz na podłodze kwadrat (2D), a potem go „wyciągasz” w górę, by powstał prostopadłościan (3D).*

### Skalowanie i Obracanie (Scale & Rotate)
- **Skalowanie**: Zmiana rozmiaru obiektu w jednej lub wszystkich osiach (np. rozciągnięcie sześcianu, by zrobić z niego deskę).
- **Obracanie**: Zmiana orientacji obiektu wokół jednej z osi.

### Operacje Boole'owskie (Łączenie i Wycinanie)
To matematyczny sposób modyfikowania brył:
- **Suma (Union)** $\rightarrow$ Łączy dwie bryły w jedną całość.
- **Różnica (Difference)** $\rightarrow$ Wycina jedną bryłę z drugiej. (To najczęstszy sposób robienia dziur w obiektach!).
- **Iloczyn/Przecięcie (Intersection)** $\rightarrow$ Zostawia tylko tę część obiektu, w której obie bryły się nakładały.

---

## 5. Rodzaje modelowania

W zależności od tego, co chcemy stworzyć, używamy różnych metod:

| Metoda | Na czym polega? | Zastosowanie | Przykłady narzędzi |
| --- | --- | --- | --- |
| **Parametryczne (CAD)** | Opiera się na precyzyjnych wymiarach i szkicach. Można wrócić do dowolnego wymiaru i go zmienić. | Części maszyn, architektura, inżynieria | Fusion 360, FreeCAD, Tinkercad |
| **Poligonalne** | Obiekt składa się z siatki wierzchołków, krawędzi i ścianek (poligonów). | Gry komputerowe, animacje | Blender, Maya |
| **Rzeźbienie (Sculpting)** | Praca z obiektem jak z cyfrową gliną — wygładzanie, wyciąganie, wgniatanie. | Postacie, potwory, detale organiczne | ZBrush, SculptGL |

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Czym różni się modelowanie 3D od rysunku 2D?",
    "opcje": [
      "Modelowanie 3D jest zawsze kolorowe, a 2D czarno-białe",
      "Modelowanie 3D dodaje trzeci wymiar — głębię/objętość",
      "Rysunek 2D jest tworzony w komputerze, a modelowanie ręcznie",
      "Nie ma żadnej różnicy, to tylko inne nazwy"
    ],
    "poprawna": 1,
    "wyjasnienie": "Kluczową różnicą jest dodanie trzeciego wymiaru, co pozwala na oglądanie obiektu z każdej strony i jego późniejszy wydruk 3D."
  },
  {
    "pytanie": "Która z wymienionych osi w układzie współrzędnych 3D zazwyczaj odpowiada za wysokość (pion)",
    "opcje": [
      "Oś X",
      "Oś Y",
      "Oś Z",
      "Oś W"
    ],
    "poprawna": 2,
    "wyjasnienie": "W większości programów do modelowania technicznego oś Z odpowiada za wysokość (kierunek w górę i w dół)."
  },
  {
    "pytanie": "Która operacja boole'owska służy do robienia otworów w obiekcie?",
    "opcje": [
      "Suma (Union)",
      "Różnica (Difference)",
      "Iloczyn (Intersection)",
      "Skalowanie (Scale)"
    ],
    "poprawna": 1,
    "wyjasnienie": "Operacja różnicy pozwala 'odjąć' jedną bryłę od drugiej, co w praktyce tworzy w obiekcie otwór o kształcie odjętej bryły."
  },
  {
    "pytanie": "Co to jest 'prymityw' w modelowaniu 3D?",
    "opcje": [
      "Błąd w modelu, który trzeba naprawić",
      "Najprostsza, bazowa bryła geometryczna (np. sześcian, sfera)",
      "Sposób na bardzo szybkie renderowanie obrazu",
      "Specjalny rodzaj myszki do projektowania"
    ],
    "poprawna": 1,
    "wyjasnienie": "Prymitywy to podstawowe klocki (sześcian, walec, sfera), z których poprzez modyfikacje buduje się złożone obiekty."
  },
  {
    "pytanie": "Do czego najlepiej nadaje się modelowanie parametryczne (CAD)?",
    "opcje": [
      "Do tworzenia postaci do gier wideo",
      "Do projektowania precyzyjnych części technicznych i maszyn",
      "Do malowania cyfrowych obrazów",
      "Do edycji zdjęć fotograficznych"
    ],
    "poprawna": 1,
    "wyjasnienie": "Modelowanie parametryczne pozwala na określanie dokładnych wymiarów i łatwe wprowadzanie poprawek w projekcie inżynieryjnym."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady oparte na standardach oprogramowania CAD i modelowania poligonalnego.*
