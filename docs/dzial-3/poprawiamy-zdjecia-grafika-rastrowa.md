# Szturmowiec w chmurze, czyli poprawiamy zdjęcia w edytorze grafiki rastrowej

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 14**

!!! abstract "O tym temacie"

    Korekta i retusz zdjęć zrobionych smartfonem w warsztacie lub na budowie to niezbędny etap przygotowania profesjonalnej dokumentacji technicznej i materiałów ofertowych. W ramach tej lekcji (1h) w Dziale III serwisu `inf-sb` dla Szkoły Branżowej nauczysz się wyostrzania, retuszowania skaz i niedoskonałości, kadrowania oraz korekcji tonalnej zdjęć przy użyciu edytorów rastrowych w chmurze (np. Pixlr.com) oraz stacjonarnych (GIMP).

??? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania"

    Odpowiedz w zeszycie, zanim zaczniesz nowy temat. Odpowiedzi rozwiń
    dopiero wtedy, gdy wszyscy skończą — nie liczą się do oceny.

    1. **Z poprzedniej lekcji.** Do czego służą warstwy w edytorze grafiki rastrowej?
    2. **Sprzed kilku tygodni.** Co określa kanał alfa (Alpha) w plikach graficznych?
    3. **Z dawniejszych tematów.** Jaki format pliku graficznego obsługuje przezroczystość tła?

    ??? success "Odpowiedzi"

        1. Pozwalają układać i modyfikować poszczególne elementy obrazu niezależnie od siebie.
        2. Stopień przezroczystości poszczególnych pikseli obrazu.
        3. Format PNG (oraz WEBP).

!!! success "Kryteria sukcesu"

    Po tej lekcji:

    1. Sprawnie zaloguję się i skorzystam z chmurowego edytora grafiki (np. Pixlr.com).
    2. Skadruję zdjęcia i sprostuję horyzont zgodnie z zasadą trójpodziału.
    3. Skoryguję jasność, kontrast, ekspozycję i poziom bieli/czerni.
    4. Skoryguję temperaturę barwową i balans bieli na zdjęciach warsztatowych.
    5. Usunę niechciane obiekty i skazy za pomocą narzędzia Stempel (Clone Stamp) oraz Naprawianie (Heal).
    6. wyostrzę oraz rozmyję wybrane partie obrazu w celu wyeksponowania detalu.
    7. zredukuję szumy cyfrowe powstałe przy słabym oświetleniu.
    8. Zastosuję filtry i korekty automatyczne z wyczuciem estetycznym.
    9. porównam efekty przed i po retuszu na osobnych warstwach.
    10. zapiszę poprawione pliki z optymalizacją rozmiaru na potrzeby sieci i druku.

## 1. Dlaczego zdjęcia wymagają korekty?

Zdjęcia robione smartfonem w trudnych warunkach warsztatowych często cierpią na:
- nieprawidłowe oświetlenie (za ciemne lub prześwietlone kadry),
- żółte/niebieskie zabarwienie (błędny balans bieli przy świetle jarzeniowym),
- niepotrzebny bałagan w tle lub drobne uszkodzenia powierzchni,
- brak ostrości na kluczowym detalu.

```
+-----------------------------------------------------------------------+
|  ZDJĘCIE SUROWE (Z APARATU)  -->  EDYCJA W CHMURZE / GIMP            |
|  - Złe oświetlenie                1. Kadrowanie i prostowanie        |
|  - Skazy na powierzchni           2. Korekcja tonalna (Poziomy)      |
|  - Plamy w tle                    3. Stempel / Retusz (Healing)      |
|                                   4. Wyostrzanie detalu              |
|                              -->  GOTOWA ILUSTRACJA TECHNICZNA       |
+-----------------------------------------------------------------------+
```

---

## 2. Podstawowe narzędzia retuszu i korekty

W chmurowych edytorach grafiki (np. Pixlr E / Photopea) oraz w programie GIMP znajdziemy dedykowane narzędzia naprawcze.

| Narzędzie | Działanie | Zastosowanie |
| --- | --- | --- |
| **Kadr (Crop)** | Odtcina zbędne krawędzie obrazu i prostuje kadry | Poprawa kompozycji, usunięcie tła |
| **Stempel (Clone Stamp)** | Klonuje piksele z wybranego źródła w inne miejsce | Usunięcie plam, rys, zasłonięcie tablic |
| **Łatka / Naprawianie (Healing)** | Miesza strukturę źródła z kolorem otoczenia | Retusz rys na lakierze, uszkodzeń mebli |
| **Wyostrzanie / Rozmycie** | Lokalnie zwiększa lub zmniejsza mikrokontrast | Podkreślenie krawędzi elementu |

!!! info "Retusz niedestrukcyjny"

    Nigdy nie wykonuj retuszu bezpośrednio na warstwie tła! Przed rozpoczęciem pracy zawsze powiel warstwę główną (`Ctrl + J` lub prawy przycisk myszy -> *Duplikuj warstwę*). Dzięki temu w każdej chwili możesz porównać efekt z oryginałem lub cofnąć błędy.

---

## 3. Korekcja jasności, kontrastu i koloru

Kluczem do uzyskania naturalnego wyglądu zdjęcia jest praca na histogramie oraz poziomach kolorów.

```
[Ciemne partie (Cienie)] <-------- [Półtony] --------> [Jasne partie (Światła)]
```

- **Balans bieli (White Balance):** Koryguje niepożądane odcienie (np. usuwa żółtą poświatę światła żarowego).
- **Poziomy (Levels):** Pozwalają ustawić punkt czerni i punkt bieli, co natychmiast usuwa efekt „mgły” ze zdjęcia.
- **Jaskrawość (Vibrance) vs Nasycenie (Saturation):** Jaskrawość podbija tylko mniej nasycone kolory, chroniąc naturalny odcień skóry i drewna przed przesyconą plamą.

!!! tip "Zasada trójpodziału przy kadrowaniu"

    Włącz siatkę kadrowania w edytorze. Umieszczaj najważniejszy element projektu (np. tabliczkę znamionową, złącze stolarskie, spoinę) na przecięciu linii siatki (w tzw. „mocnych punktach”).

---

## 4. Instrukcja krok po kroku: Retusz zdjęcia detalu w Pixlr / GIMP

1. **Krok 1:** Wejdź na stronę `pixlr.com/express` lub otwórz program GIMP.
2. **Krok 2:** Otwórz zdjęcie wykonane w trudnych warunkach oświetleniowych (*Open Image*).
3. **Krok 3:** Wybierz narzędzie *Crop (Kadr)*, włącz prostowanie i wyrównaj linię stołu/horyzontu.
4. **Krok 4:** Duplikuj warstwę ze zdjęciem (*Duplicate Layer*).
5. **Krok 5:** Otwórz menu *Adjust -> Levels (Poziomy)* i przesuń skrajne suwaki do krawędzi wykresu histogramu.
6. **Krok 6:** Wybierz narzędzie *Spot Heal (Naprawianie)* lub *Clone Stamp (Stempel)*. Alt-kliknij czysty fragment powierzchni i zamaluj rysę lub plamę na elemencie.
7. **Krok 7:** Wybierz filtr *Sharpen (Wyostrzanie)*, aby uwypuklić detale i krawędzie wyrobu.
8. **Krok 8:** Włączaj i wyłączaj widoczność edytowanej warstwy (ikona oka), oceniając naturalność retuszu.
9. **Krok 9:** Zapisz plik w formacie JPG z jakością 80–85% (*Save / Export*), optymalizując rozmiar pliku.

!!! warning "Nie przesadzaj z wyostrzaniem i nasyceniem!"

    Nadmierne wyostrzenie tworzy wokół krawędzi białe „poświaty” (artefakty), a zbyt wysokie nasycenie sprawia, że zdjęcie wygląda sztucznie i nieprofesjonalnie.

---

## Podsumowanie

Poprawianie zdjęć w edytorze grafiki rastrowej pozwala przekształcić surowe, ciemne lub uszkodzone kadry ze smartfona w profesjonalne ilustracje do katalogów i dokumentacji. Umiejętność kadrowania, retuszu stemplem oraz poziomowania kontrastu to podstawowy warsztat w nowoczesnej firmie.

---

## Ćwiczenia

!!! note "Ćwiczenie 1 (Podstawowe):"

    Otwórz w edytorze chmurowym przechylone zdjęcie i skoryguj jego kadrowanie oraz prostoliniowość horyzontu.

!!! note "Ćwiczenie 2 (Średnio zaawansowane):"

    Za pomocą narzędzi korekcji tonalnej (*Poziomy* lub *Jasność/Kontrast*) popraw niedoświetlone zdjęcie wykonane w ciemnym pomieszczeniu.

!!! note "Ćwiczenie 3 (Branżowe):"

    Pobierz zdjęcie elementu technicznego z rysą lub zabrudzeniem. Użyj narzędzia *Stempel* / *Naprawianie*, aby bezśladowo usunąć uszkodzenie z powierzchni.

!!! note "Ćwiczenie 4 (Zaawansowane):"

    Wykonaj pełną korektę zdjęcia produktowego dla swojej branży: skadruj obraz, popraw balans bieli, wyretuszuj tło, wyostrz kluczowy detal i wyeksportuj wynik w dwóch wersjach (do druku i na stronę www).

??? tip "Podpowiedź 1"

    Kierunek: Zastanów się, od czego zacząć i jakich narzędzi z tej lekcji użyć do wykonania zadania.

??? tip "Podpowiedź 2"

    Konkretne narzędzie: Przejrzyj sekcję w treści lekcji z dokładnym opisem wymaganej funkcji lub polecenia menu.

??? tip "Podpowiedź 3"

    Prawie gotowe rozwiązanie: Wykonaj czynności krok po kroku według instrukcji i zweryfikuj efekt w karcie pracy.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Do czego służy narzędzie Stempel (Clone Stamp) w edytorze graficznym?",
    "opcje": [
      "Do wpisywania tekstu nagłówka",
      "Do pobierania próbki z jednego miejsca obrazu i kopiowania jej w inne miejsce",
      "Do zmieniania formatu pliku z JPG na PDF",
      "Do automatycznego przeliczania wymiarów"
    ],
    "poprawna": 1,
    "wyjasnienie": "Stempel klonuje piksele ze wskazanego obszaru źródłowego, co pozwala maskować plamy, rysy i niechciane obiekty."
  },
  {
    "pytanie": "Dlaczego retusz należy wykonywać na zduplikowanej warstwie, a nie bezpośrednio na tle?",
    "opcje": [
      "Ponieważ komputer inaczej zablokuje plik",
      "Aby w dowolnym momencie móc cofnąć błędy i porównać efekt z oryginałem",
      "Ponieważ tło nie przyjmuje kolorów",
      "Jest to jedyny sposób na zapisanie pliku"
    ],
    "poprawna": 1,
    "wyjasnienie": "Praca na osobnej warstwie (retusz niedestrukcyjny) zabezpiecza oryginalny obraz przed nieodwracalnymi uszkodzeniami."
  },
  {
    "pytanie": "Co powoduje błędnie ustawiony balans bieli na zdjęciu?",
    "opcje": [
      "Zmniejszenie rozdzielczości obrazu",
      "Niepożądaną dominantę kolorystyczną (np. zbyt żółty lub zbyt niebieski odcień całego zdjęcia)",
      "Automatyczne usunięcie pliku z pamięci",
      "Niewyraźne litery w opisie"
    ],
    "poprawna": 1,
    "wyjasnienie": "Balans bieli dostosowuje temperaturę barwową do źródła światła – nieprawidłowy daje obcy odcień na białych powierzchniach."
  },
  {
    "pytanie": "Co przedstawia histogram w edytorze grafiki rastrowej?",
    "opcje": [
      "Wykres rozkładu jasności pikseli od czerni do bieli",
      "Listę zainstalowanych czcionek",
      "Czas pracy nad projektem",
      "Poziom zużycia pamięci RAM"
    ],
    "poprawna": 0,
    "wyjasnienie": "Histogram ukazuje graficzny wykres ilości pikseli w poszczególnych zakresach tonalnych (cienie, półtony, światła)."
  },
  {
    "pytanie": "Która funkcja pozwala na usunięcie zbędnych obszarów przy krawędziach zdjęcia i zmianę kompozycji?",
    "opcje": [
      "Pędzel",
      "Kadrowanie (Crop)",
      "Wypełnienie kubełkiem",
      "Krzywe Beziera"
    ],
    "poprawna": 1,
    "wyjasnienie": "Narzędzie Kadrowanie (Crop) odcina niepotrzebne brzegi zdjęcia, skupiając uwagę na kluczowym fragmencie kadru."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na chmurowym Pixlr oraz edytorze GIMP dla Szkół Branżowych.*
