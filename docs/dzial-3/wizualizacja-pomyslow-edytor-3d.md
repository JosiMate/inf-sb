# Wizualizacja pomysłów, czyli projektujemy w edytorze 3D

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 12**

!!! abstract "O tym temacie"

    **1 godzina lekcyjna** · Dział III. Aplikacje komputerowe pomagają w pracy · rozdział 12

    Na poprzedniej lekcji poznałeś bryły, osie i operacje modelowania. Dziś
    robisz z tego **prawdziwy projekt**: ścienny uchwyt na śrubokręty, z
    dokładnymi wymiarami w milimetrach — taki, który dałoby się wydrukować
    na drukarce 3D i powiesić w warsztacie.

    Pracujesz w **Tinkercadzie** — edytorze 3D w przeglądarce. **Nie
    zakładasz konta**: wchodzisz kodem klasy i pseudonimem, a projekty
    zapisują się same i widzi je nauczyciel.

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Która oś układu współrzędnych 3D odpowiada
       zwykle za wysokość?
    2. **Sprzed kilku tygodni.** Zaszyfruj szyfrem Cezara z kluczem 3 słowo
       `KOT`.
    3. **Z dawniejszych tematów.** Ile wynosi NWD(12, 18)?

    ??? success "Odpowiedzi"

        1. Oś **Z**.
        2. **NRW** — każda litera przesunięta o 3 miejsca w prawo.
        3. **6** — największa liczba, przez którą dzielą się i 12, i 18.

!!! success "Kryteria sukcesu"

    Po tej lekcji:

    1. Wejdę do Tinkercada kodem klasy i pseudonimem i założę nowy projekt.
    2. Obrócę, przesunę i przybliżę widok tak, żeby zobaczyć model z każdej strony.
    3. Nadam bryle dokładne wymiary w milimetrach, wpisując je w pola wymiarów.
    4. Wytnę otwór: zamienię bryłę na otwór i zgrupuję ją z drugą bryłą.
    5. Ustawię elementy w równych odstępach linijką i powielaniem.

## 1. Tinkercad bez zakładania konta

Tinkercad działa w przeglądarce — nic nie instalujesz. Klasa ma w nim
**swoją grupę**, do której wchodzisz kodem od nauczyciela:

1. Otwórz `tinkercad.com` i kliknij **Join Class** (dołącz do klasy).
2. Wpisz **kod klasy** — poda go nauczyciel na lekcji.
3. Wpisz swój **pseudonim** (nickname) i kliknij **That's me!**
4. Kliknij **Create New Design** (nowy projekt).

Pierwszą rzeczą w nowym projekcie jest **nazwa**: kliknij losową nazwę
w lewym górnym rogu i wpisz `nr<numer w dzienniku>-uchwyt`, np. `nr07-uchwyt`.
Projekt zapisuje się sam co chwilę — nie ma przycisku „Zapisz”.

!!! info "Co widzi nauczyciel"

    Wszystkie projekty uczniów z klasy nauczyciel widzi w zakładce klasy.
    Dlatego nazwa z numerem jest ważna — po niej rozpoznaję Twoją pracę.
    Projekty klasy są prywatne: nikt spoza klasy ich nie zobaczy.

!!! tip "Nazwy przycisków"

    Jeśli Tinkercad wyświetla się po polsku, przyciski są w tych samych
    miejscach, tylko inaczej się nazywają. Dlatego na tej stronie podaję nazwy
    angielskie i skróty klawiszowe — te się nie zmieniają.

## 2. Ekran i widok

Na środku jest **płaszczyzna robocza** — niebieska siatka, na której stawiasz
bryły. Każde pole siatki to milimetry. Po prawej jest panel z bryłami
(*Basic Shapes*): wystarczy przeciągnąć bryłę na siatkę.

| Chcesz… | Zrób tak |
| --- | --- |
| obrócić widok dookoła modelu | przeciągnij **prawym** przyciskiem myszy |
| przesunąć widok | przeciągnij **środkowym** przyciskiem (kółkiem) |
| przybliżyć lub oddalić | kręć kółkiem myszy |
| pokazać zaznaczoną bryłę na cały ekran | klawisz ++f++ |
| cofnąć ostatni ruch | ++ctrl+z++ |

## 3. Bryła o dokładnych wymiarach

Przeciągnij na siatkę **Box** (prostopadłościan) i kliknij go. Pojawią się
białe uchwyty, a przy krawędziach — **liczby z wymiarami**. Kliknij liczbę,
wpisz nową wartość i naciśnij ++enter++. Tak samo ustawisz wysokość (czarny
uchwyt na górze bryły).

Szerokość to kierunek osi X, głębokość — osi Y, wysokość — osi Z. Wymiary
są w milimetrach.

| Przydatne klawisze | Co robią |
| --- | --- |
| strzałki | przesuwają bryłę po siatce |
| ++ctrl+arrow-up++ / ++ctrl+arrow-down++ | podnoszą i opuszczają bryłę (oś Z) |
| ++d++ | opuszcza bryłę z powrotem na płaszczyznę roboczą |
| ++ctrl+d++ | powiela bryłę |

## 4. Otwór — wycinanie jednej bryły z drugiej

W Tinkercadzie nie ma „wiertarki”. Otwór robisz z **bryły-otworu**: zaznacz
bryłę i w okienku *Shape* wybierz **Hole** (klawisz ++h++) — bryła zrobi się
przezroczysta i zakreskowana. Teraz zaznacz ją razem z bryłą, w której ma być
otwór (przytrzymaj ++shift++ i kliknij obie), i **zgrupuj**: przycisk *Group*
albo ++ctrl+g++. Otwór wytnie się w miejscu, gdzie obie bryły na siebie
zachodzą.

To jest operacja boole'owska **różnicy** z poprzedniej lekcji: od bryły
odejmujemy otwór.

!!! example "Przewiduj"

    Podstawa ma 15 mm wysokości. Walec-otwór o wysokości 20 mm stoi na
    płaszczyźnie roboczej, czyli wystaje 5 mm ponad podstawę. Co zostanie po
    zgrupowaniu — otwór na wylot, a nad nim dodatkowy „kominek” 5 mm?

    ??? success "Przewiduj, potem sprawdź wynik"

        **Otwór na wylot, bez żadnego kominka.** Otwór tylko **zabiera**
        materiał tam, gdzie zachodzi na bryłę. Część, która wystaje w
        powietrze, po prostu znika. Dlatego otwór robi się zawsze trochę
        wyższy niż bryła — wtedy na pewno przetnie ją do końca.

## 5. Równe odstępy — linijka i powielanie

Na oko otwory nigdy nie wyjdą równo. Są dwa sposoby, żeby było dokładnie:

- **Linijka** (*Ruler*, klawisz ++r++): postaw ją w rogu podstawy. Kiedy
  klikniesz bryłę, przy linijce pojawią się jej **odległości od narożnika** —
  kliknij liczbę i wpisz dokładną wartość.
- **Powielanie z powtórzeniem**: zaznacz bryłę, naciśnij ++ctrl+d++ i przesuń
  kopię o potrzebną odległość. Każde kolejne ++ctrl+d++ zrobi następną kopię
  **przesuniętą o tyle samo**.

Do ustawiania w jednej linii służy **Align** (wyrównaj, klawisz ++l++):
zaznacz kilka brył, naciśnij ++l++ i kliknij kropkę, do której mają się
wyrównać — np. środek.

!!! warning "Najczęstsze błędy w Tinkercadzie"

    | Objaw | Przyczyna | Co zrobić |
    | --- | --- | --- |
    | Otwór nie wycina, tylko leży w bryle | bryły nie są zgrupowane | zaznacz obie i ++ctrl+g++ |
    | Otwór wycina tylko do połowy | walec-otwór jest za niski albo stoi za wysoko | ustaw wysokość otworu większą niż bryła |
    | Bryła „wisi” w powietrzu | była podnoszona albo stała na innej bryle | zaznacz ją i naciśnij ++d++ |
    | Wymiar zmienił się w złym kierunku | wpisany przy złej krawędzi | szerokość — oś X, głębokość — Y, wysokość — Z |
    | Nie ma mojego projektu | wejście bez kodu klasy albo inny pseudonim | zawsze przez **Join Class**, zawsze ten sam pseudonim |

## Zadanie: uchwyt na śrubokręty

Projektujesz ścienny uchwyt na cztery śrubokręty: płytkę z czterema
otworami, przykręcaną do ściany. Ćwiczenia 1 i 2 robi każdy — to wymagania
na oceny 2–3. Ćwiczenie 3 jest na ocenę 4, a 4 — na ocenę 5.

```text
widok z góry (podstawa 120 × 40 mm)

  ┌────────────────────────────────────────┐   ← ściana tylna (ćw. 3)
  │                                        │
  │    ○        ○        ○        ○        │   otwory Ø 10 mm
  │                                        │
  └────────────────────────────────────────┘
       ↑ 22,5 mm  ↔ 25 mm ↔ 25 mm ↔ 25 mm
```

!!! note "Ćwiczenie 1. Podstawa"

    Wejdź do klasy, załóż projekt `nr<numer>-uchwyt` i postaw na siatce
    **Box** o wymiarach **120 × 40 × 15 mm** (szerokość × głębokość × wysokość).
    Obejrzyj go z każdej strony: obróć widok prawym przyciskiem i naciśnij ++f++.

!!! note "Ćwiczenie 2. Cztery otwory"

    Zrób w podstawie **cztery otwory na wylot o średnicy 10 mm**, w jednej
    linii, na środku głębokości podstawy. Środki otworów mają być co
    **25 mm**, a pierwszy — **22,5 mm** od lewej krawędzi. Sprawdź: ostatni
    środek wypada wtedy 22,5 mm od prawej krawędzi.

    ??? tip "Podpowiedź 1"

        Otwór to **Cylinder** (walec) o wymiarach 10 × 10 mm, zamieniony na
        **Hole**. Wysokość daj większą niż 15 mm — np. 20 mm.

    ??? tip "Podpowiedź 2"

        Postaw **linijkę** (++r++) w lewym przednim rogu podstawy. Walec ma
        10 mm średnicy, więc jego lewa krawędź ma być 22,5 − 5 = **17,5 mm**
        od rogu, a przednia: 20 − 5 = **15 mm**.

    ??? tip "Podpowiedź 3"

        Gdy pierwszy otwór stoi dobrze: ++ctrl+d++, przesuń kopię o 25 mm
        w prawo (przy linijce: 17,5 + 25 = 42,5 mm), potem jeszcze dwa razy
        ++ctrl+d++. Na koniec zaznacz wszystko (++ctrl+a++) i ++ctrl+g++.

!!! note "Ćwiczenie 3. Ściana do przykręcenia (ocena 4)"

    Uchwyt trzeba przykręcić do ściany. Dostaw z tyłu podstawy pionową
    ściankę **120 × 4 × 50 mm** — dolną krawędzią równo z dołem podstawy,
    tylną ścianą równo z tyłem podstawy (użyj **Align**, ++l++). W ściance zrób
    **dwa otwory na wkręty o średnicy 4 mm**, 15 mm od bocznych krawędzi
    i 40 mm nad dołem. Zgrupuj wszystko w jeden obiekt.

    ??? tip "Podpowiedź 1"

        Otwór na wkręt idzie **w poprzek ścianki** — poziomo, wzdłuż osi Y.
        Postaw walec 4 × 4 mm i obróć go o 90° (strzałka obrotu przy bryle;
        z ++shift++ obraca co 45°).

    ??? tip "Podpowiedź 2"

        Walec po obróceniu musi być dłuższy niż grubość ścianki, np. 10 mm,
        i przechodzić przez nią na wylot. Wysokość ustawisz ++ctrl+arrow-up++
        albo wpisując odległość od płaszczyzny roboczej.

    ??? tip "Podpowiedź 3"

        Środek otworu 40 mm nad dołem, a walec ma 4 mm średnicy — więc jego
        dolna krawędź jest na wysokości 38 mm. Drugi otwór: ++ctrl+d++
        i przesunięcie o 120 − 2 × 15 = 90 mm.

!!! note "Ćwiczenie 4. Uchwyt do Twojego narzędzia (ocena 5)"

    Zaprojektuj w nowym projekcie (`nr<numer>-uchwyt-zawod`) uchwyt albo
    organizer na **narzędzie z Twojego zawodu** — klucze, pędzle, nożyczki,
    końcówki. Zmierz prawdziwe narzędzie linijką albo suwmiarką i zapisz
    wymiary. W projekcie mają być: co najmniej jeden otwór lub wycięcie
    dopasowane do zmierzonego narzędzia (z zapasem 1 mm) i **napis** z Twoim
    numerem — bryła *Text* zamieniona na otwór i wycięta na 1 mm w głąb.

### Co oddajesz

Zadanie wpisujesz do **karty pracy działu III**, w temacie „Wizualizacja
pomysłów”:

- **nazwa pliku albo tytuł pracy** — nazwa projektu, np. `nr07-uchwyt`;
- **program** — Tinkercad;
- **co zrobiłeś** — które ćwiczenia, jakie wymiary, co sprawiło kłopot; przy
  ćwiczeniu 4 — wymiary zmierzonego narzędzia;
- **zrzut ekranu** gotowego modelu, obróconego tak, żeby było widać otwory.

Projekt w Tinkercadzie zostaw — sprawdzam go w zakładce klasy.

!!! info "Wymagania mówią o SketchUpie"

    W wymaganiach na oceny do tego tematu jest program SketchUp. Na lekcji
    używamy Tinkercada, bo nie wymaga zakładania konta. Umiejętności są te
    same: kreślenie brył, projekt z wymiarami, kolory i otwory.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Jak wejść do Tinkercada na lekcji bez zakładania konta?",
    "opcje": [
      "Zalogować się kontem Google kolegi",
      "Kliknąć Join Class, wpisać kod klasy i swój pseudonim",
      "Pobrać program na pendrive",
      "Nie da się — konto jest zawsze potrzebne"
    ],
    "poprawna": 1,
    "wyjasnienie": "Nauczyciel zakłada klasę w Tinkercadzie i podaje kod. Uczeń wchodzi przez Join Class, kodem i pseudonimem — bez e-maila i hasła."
  },
  {
    "pytanie": "Walec ustawiony jako Hole stoi w prostopadłościanie, ale nic się nie wycina. Czego brakuje?",
    "opcje": [
      "Zmiany koloru walca",
      "Zgrupowania obu brył (Ctrl + G)",
      "Zapisania projektu",
      "Obrócenia widoku"
    ],
    "poprawna": 1,
    "wyjasnienie": "Otwór wycina materiał dopiero po zgrupowaniu z bryłą. Zapisywać nie trzeba — Tinkercad robi to sam."
  },
  {
    "pytanie": "Podstawa ma 15 mm wysokości. Jaką wysokość dać walcowi-otworowi, żeby na pewno przeciął ją na wylot?",
    "opcje": ["10 mm", "14 mm", "20 mm", "Wysokość nie ma znaczenia"],
    "poprawna": 2,
    "wyjasnienie": "Otwór musi być wyższy niż bryła. Część wystająca w powietrze znika po zgrupowaniu, a za niski otwór wytnie tylko część głębokości."
  },
  {
    "pytanie": "Cztery otwory mają środki co 25 mm, pierwszy 22,5 mm od lewej krawędzi podstawy o szerokości 120 mm. Gdzie wypada środek ostatniego?",
    "opcje": ["97,5 mm od lewej krawędzi", "100 mm od lewej krawędzi", "75 mm od lewej krawędzi", "120 mm od lewej krawędzi"],
    "poprawna": 0,
    "wyjasnienie": "22,5 + 3 × 25 = 97,5 mm — czyli 22,5 mm od prawej krawędzi, symetrycznie."
  },
  {
    "pytanie": "Który klawisz pokazuje zaznaczoną bryłę na całym ekranie?",
    "opcje": ["F", "H", "D", "L"],
    "poprawna": 0,
    "wyjasnienie": "F dopasowuje widok do zaznaczenia. H zamienia bryłę na otwór, D opuszcza ją na płaszczyznę roboczą, a L otwiera wyrównywanie."
  }
]
</script>
</div>

---

*Stan sprawdzony 30 października 2026 r. Skróty klawiszowe według oficjalnej
ściągi Tinkercada; logowanie uczniów kodem klasy według opisu Tinkercad
Classrooms.*
