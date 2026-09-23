# Jak to wykorzystać, czyli peryferia komputerowe ułatwiają pracę

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 21**

!!! abstract "O tym temacie"

    Urządzenia peryferyjne, takie jak skanery, czytniki kodów kreskowych, drukarki etykiet czy autoryzatory biometryczne, automatyzują pracę w warsztatach, magazynach i biurach. W ramach tej lekcji (1h) w Dziale IV serwisu `inf-sb` dla Szkoły Branżowej nauczysz się wykorzystywać skanery dokumentów, cyfryzować dokumentację papierową, stosować oprogramowanie OCR do rozpoznawania tekstu oraz poznasz standard TWAIN i różnice w konstrukcji przetworników optycznych (CIS vs CCD).

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. sklasyfikować urządzenia peryferyjne pod kątem ich zastosowania w pracy zawodowej
    2. wyjaśnić zasadę działania skanera optycznego i panelu sterowania urządzenia
    3. opisać różnice konstrukcyjne i jakościowe między przetwornikami CIS a CCD
    4. wyjaśnić pojęcie oraz skrót OCR (Optical Character Recognition)
    5. dobrać optymalną rozdzielczość skanowania (DPI) dla dokumentu tekstu oraz dla grafiki
    6. zdefiniować standard komunikacji TWAIN / WIA i wyjaśnić jego rolę
    7. cyfryzować drukowaną dokumentację i przekształcać ją w edytowalny plik tekstowy
    8. używać oprogramowania OCR (stacjonarnego lub w chmurze) do rozpoznawania tabel
    9. przygotowywać dokumentację warsztatową i magazynową do archiwizacji cyfrowej
    10. przestrzegać zasad bezpiecznej i ergonomicznej pracy z urządzeniami peryferyjnymi

## 1. Rola urządzeń peryferyjnych w pracy zawodowej

Urządzenia peryferyjne (zewnętrzne) to sprzęt podłączony do jednostki centralnej komputera, który umożliwia wprowadzanie danych (np. skanery, czytniki) lub ich wyprowadzanie (np. drukarki, plotery).

```
+-----------------------------------------------------------------------+
|  URZĄDZENIA WEJŚCIA  -->   KOMPUTER / SYSTEM  -->  URZĄDZENIA WYJŚCIA  |
|  - Skaner / OCR            (Przetwarzanie)         - Drukarka 3D      |
|  - Czytnik kodów QR                                - Ploter tnący     |
|  - Skaner biometryczny                             - Monitor          |
+-----------------------------------------------------------------------+
```

### Podstawowe peryferia wspomagające stanowisko pracy:

- **Skaner płaski / dokumentowy:** Przekształca fizyczny papier w obraz cyfrowy.
- **Czytnik kodów kreskowych i QR:** Błyskawicznie wprowadza identyfikatory części do systemu magazynowego.
- **Drukarka etykiet / kodów:** Drukuje samoprzylepne oznaczenia towarów i paczek.

---

## 2. Technologia skanowania: Przetworniki CIS vs CCD oraz TWAIN

Podczas wyboru skanera do firmy kluczowa jest technologia przechwytywania obrazu.

| Cecha | Przetwornik CIS (Contact Image Sensor) | Przetwornik CCD (Charge-Coupled Device) |
| --- | --- | --- |
| **Element oświetlający** | Diody LED (RGB) | Lampa z zimną katodą lub LED |
| **Głębia ostrości** | Bardzo mała (wymaga idealnie płaskiego papieru) | Duża (skanuje też grube książki i przedmioty 3D) |
| **Gabaryty urządzenia** | Bardzo cienkie, lekkie, zasilane z USB | Grubsze, cięższe, wymaga osobnego zasilacza |
| **Cena i pobór prądu** | Niska cena, niski pobór prądu | Wyższa cena, wysoka jakość odwzorowania |

!!! info "Co to jest sterownik TWAIN / WIA?"

    **TWAIN** to uniwersalny interfejs programistyczny (sterownik), który umożliwia programom graficznym i biurowym (np. GIMP, Word) bezpośrednie wywoływanie skanera bez konieczności uruchamiania zewnętrznych aplikacji producenta.

---

## 3. Rozpoznawanie tekstu (OCR) i dobór rozdzielczości DPI

Samo zeskanowanie dokumentu tworzy jedynie plik graficzny (obrazek). Aby móc edytować tekst w programie Word, należy zastosować oprogramowanie **OCR (Optical Character Recognition)**.

```
PAPIER  -->  SKANOWANIE (300 DPI)  -->  OBRAZ RASTROWY  -->  ANALIZA OCR  -->  EDYTOWALNY TEKST / TABELA
```

### Optymalne ustawienia rozdzielczości skanowania (DPI):

- **150–200 DPI:** Szybki podgląd i czarno-białe archiwum podręczne.
- **300 DPI:** **Idealna rozdzielczość dla programu OCR** (gwarantuje najwyższą trafność rozpoznawania liter).
- **600+ DPI:** Skanowanie niewielkich zdjęć, grafik i detali technicznych.

!!! tip "Dlaczego nie warto ustawiać 1200 DPI do tekstu?"

    Ustawienie zbyt wysokiej rozdzielczości (np. 1200 DPI) dla zwykłego pismu zwiększa rozmiar pliku z 2 MB do 100 MB i drastycznie wydłuża czas skanowania, nie poprawiając przy tym skuteczności programu OCR.

---

## 4. Instrukcja krok po kroku: Przekształcanie dokumentu papierowego na edytowalny tekst

1. **Krok 1:** Umieść dokument papierowy (np. instrukcję lub umowę) na szybie skanera.
2. **Krok 2:** Otwórz program do obsługi skanera lub edytor tekstu/grafiki wspierający TWAIN.
3. **Krok 3:** Ustaw tryb skanowania: *Odcienie szarości (Grayscale)* oraz rozdzielczość *300 DPI*.
4. **Krok 4:** Wykonaj skanowanie i zapisz plik jako obraz (PNG lub TIFF).
5. **Krok 5:** Otwórz program OCR (np. ABBYY FineReader, NAPS2 lub darmowy konwerter chmurowy `onlineocr.net`).
6. **Krok 6:** Wczytaj zeskanowany plik obrazu do programu OCR.
7. **Krok 7:** Wybierz język dokumentu (*Polski*) i kliknij *Convert / Rozpoznaj*.
8. **Krok 8:** Sprawdź poprawność rozpoznanych znaków (zwróć uwagę na polskie litery `ą, ę, ś, ż`).
9. **Krok 9:** Skopiuj rozpoznany tekst lub wyeksportuj wynik bezpośrednio do pliku `DOCX`.
10. **Krok 10:** Otwórz dokument w edytorze i sformatuj go według potrzeb.

!!! warning "Uważaj na zagięcia i plamy!"

    Plamy oleju, zagięcia papieru czy słaby kontrast pisma na dokumentach warsztatowych obniżają skuteczność OCR. Zawsze przetrzyj szybę skanera przed pracą!

---

## Podsumowanie

Urządzenia peryferyjne, a w szczególności skanery w połączeniu z technologią OCR, odgrywają kluczową rolę w cyfryzacji procesów w firmie. Znajomość różnic między przetwornikami CIS i CCD, sterownika TWAIN oraz doboru optymalnej rozdzielczości 300 DPI do OCR pozwala na szybką i bezbłędną archiwizację dokumentacji.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Zeskanuj dokument papierowy lub zrób czytelne zdjęcie smartfonem, ustawiając odpowiednie kadrowanie.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Użyj bezpłatnego narzędzia OCR w chmurze do przekształcenia zdjęcia jednostronicowej instrukcji na edytowalny tekst.
3. **Ćwiczenie 3 (Branżowe):** Zeskanuj tabelę cennikową z papierowego katalogu i użyj oprogramowania OCR, aby zaimportować dane w postaci komórek do arkusza kalkulacyjnego.
4. **Ćwiczenie 4 (Zaawansowane):** Przeprowadź analizę porównawczą jakości skanowania tego samego dokumentu w rozdzielczościach 100 DPI, 300 DPI i 600 DPI. Porównaj czas skanowania, rozmiar pliku oraz skuteczność OCR.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Co oznacza skrót OCR w technice komputerowej?",
    "opcje": [
      "Optical Character Recognition (Optyczne rozpoznawanie znaków / tekstu)",
      "Online Computer Recovery (Odzyskiwanie komputera w sieci)",
      "Optimal Color Rendering (Optymalne renderowanie kolorów)",
      "Office Control Reader (Biurowy czytnik kart)"
    ],
    "poprawna": 0,
    "wyjasnienie": "OCR to technologia służąca do przekształcania obrazu rastrowego zawierającego tekst na postać edytowalną."
  },
  {
    "pytanie": "Jaka rozdzielczość skanowania (DPI) jest uznawana za standardową i optymalną dla programu OCR?",
    "opcje": [
      "72 DPI",
      "300 DPI",
      "2400 DPI",
      "12000 DPI"
    ],
    "poprawna": 1,
    "wyjasnienie": "Rozdzielczość 300 DPI zapewnia idealny kompromis między precyzją obrysu liter dla programu OCR a rozmiarem pliku."
  },
  {
    "pytanie": "Główną zaletą skanerów z przetwornikiem CCD w porównaniu do CIS jest:",
    "opcje": [
      "Brak konieczności zasilania",
      "Duża głębia ostrości umożliwiająca skanowanie grubych książek i trójwymiarowych obiektów",
      "Cieńsza obudowa o grubości 1 cm",
      "Niższa cena zakupu"
    ],
    "poprawna": 1,
    "wyjasnienie": "Przetwornik CCD posiada układ optyczny z soczewką, co zapewnia dużą głębię ostrości w przeciwieństwie do stykowej technologii CIS."
  },
  {
    "pytanie": "Do czego służy standard TWAIN w systemie operacyjnym?",
    "opcje": [
      "Umożliwia bezpośrednie pobieranie obrazu ze skanera z poziomu aplikacji (np. Word, GIMP)",
      "Służy do odtwarzania muzyki w tle",
      "Zabezpiecza dysk przed wyciekiem danych",
      "Formatuje karty pamięci"
    ],
    "poprawna": 0,
    "wyjasnienie": "TWAIN to uniwersalny interfejs komunikacyjny łączący oprogramowanie użytkownika ze sterownikiem skanera."
  },
  {
    "pytanie": "Które z poniższych urządzeń zaliczamy do peryferyjnych urządzeń WEJŚCIA?",
    "opcje": [
      "Drukarka laserowa",
      "Czytnik kodów kreskowych",
      "Ploter tnący",
      "Głośnik komputerowy"
    ],
    "poprawna": 1,
    "wyjasnienie": "Czytnik kodów kreskowych wprowadza dane z otoczenia do komputera, więc jest urządzeniem wejścia."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na standardach TWAIN / OCR dla Szkół Branżowych.*
