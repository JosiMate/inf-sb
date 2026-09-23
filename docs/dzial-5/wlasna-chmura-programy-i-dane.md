# Własna chmura, czyli programy i dane poza firmą

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 26**

!!! abstract "O tym temacie"

    Przetwarzanie w chmurze obliczeniowej (Cloud Computing) umożliwia bezpieczne przechowywanie danych firmowych, pracę zdalną oraz dostęp do zaawansowanego oprogramowania bez konieczności inwestowania we własne kosztowne serwery. W ramach tej lekcji (1h) w Dziale V serwisu `inf-sb` dla Szkoły Branżowej nauczysz się korzystać z dysków chmurowych (Google Drive, OneDrive, Nextcloud), edytować dokumenty online, udostępniać pliki z odpowiednimi uprawnieniami oraz organizować e-pracę.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie chmury obliczeniowej (Cloud Computing) i zasady jej działania
    2. wymieniać modele usług chmurowych (IaaS, PaaS, SaaS) i podawać przykłady
    3. zakładać konto i korzystać z dysków chmurowych (Google Drive, MS OneDrive, Nextcloud)
    4. pakować, wysyłać i synchronizować pliki pomiędzy komputerem a chmurą
    5. tworzyć i edytować dokumenty, arkusze i prezentacje bezpośrednio w przeglądarce
    6. udostępniać pliki innym użytkownikom z ograniczeniem uprawnień (Podgląd, Komentowanie, Edycja)
    7. zarządzać łączami publicznymi z zabezpieczeniem hasłem i terminem wygaśnięcia
    8. prowadzić współedycję dokumentów w czasie rzeczywistym z zespołem
    9. organizować bezpieczną e-pracę i zdalny dostęp do zasobów warsztatu
    10. oceniać zagrożenia prywatności i stosować dwuskładnikowe uwierzytelnianie (2FA) w chmurze

## 1. Co to jest chmura obliczeniowa (Cloud Computing)?

Tradycyjny model IT wymagał zakupu własnego serwera, zainstalowania na nim oprogramowania oraz dbania o jego chłodzenie i zasilanie. **Chmura obliczeniowa** przenosi ten ciężar na wyspecjalizowane centra danych (Data Center).

```
+-----------------------------------------------------------------------+
|  MODELE USŁUG CHMUROWYCH                                              |
|  - SaaS (Software as a Service)  --> Gotowe aplikacje (Google Docs)   |
|  - PaaS (Platform as a Service)  --> Środowisko dla programistów      |
|  - IaaS (Infrastructure as Service) -> Wirtualne serwery i dyski    |
+-----------------------------------------------------------------------+
```

### Korzyści płynące z chmury:

- **Dostęp z każdego miejsca:** Pracujesz na telefonie, laptopie czy komputerze w warsztacie.
- **Bezpieczeństwo i backup:** Awaria twardego dysku w komputerze nie niszczy Twoich plików.
- **Brak opłat na start:** Płacisz mały abonament lub korzystasz z darmowych limitów.

---

## 2. Uprawnienia i udostępnianie plików w chmurze

Kluczowym elementem pracy w chmurze jest bezpieczne udostępnianie dokumentacji klientom i współpracownikom.

| Poziom uprawnień | Co może zrobić odbiorca? | Zastosowanie |
| --- | --- | --- |
| **Przeglądający (Viewer)** | Może tylko czytać i pobrać plik | Wysyłanie gotowej oferty / cennika dla klienta |
| **Komentujący (Commenter)** | Może dopisywać uwagi w chmurkach | Przegląd projektu z inwestorem |
| **Edytor (Editor)** | Może zmieniać treść, kasować i dopisywać | Wspólna praca zespołu nad umową |

```
PLIK W CHMURZE  -->  UDOSTĘPNIJ  -->  1. Wybierz adres e-mail
                                     2. Wybierz uprawnienie (Edytor / Podgląd)
                                     3. Wyślij powiadomienie
```

!!! info "Nigdy nie udostępniaj pliku jako 'Każdy mający link może edytować'!"

    Udostępnienie dokumentu z uprawnieniem edycji dla każdego, kto ma link, sprawia, że przypadkowa osoba z sieci może usunąć Twoje dane lub wkleić nieodpowiednie treści!

---

## 3. Współedycja dokumentów w czasie rzeczywistym

Aplikacje chmurowe (np. Google Docs, MS Word Online) pozwalają na jednoczesną pracę kilku osób na jednym pliku.

```
Użytkownik A (Warsztat) ---\
                            +---> DOKUMENT W CHMURZE (Widoczne kursory i zmiany w realu)
Użytkownik B (Biuro)    ---/
```

- **Sugerowanie zmian:** Pozwala nanosić poprawki, które właściciel pliku musi zaakceptować.
- **Historia wersji:** Umożliwia przywrócenie stanu dokumentu sprzed godziny, dnia lub tygodnia.

!!! tip "Ochrona konta chmurowego (2FA)"

    W chmurze przechowujesz całe życie swojej firmy. Obowiązkowo włącz **Uwierzytelnianie dwuskładnikowe (2FA)** — logowanie będzie wymagało potwierdzenia w telefonie.

---

## 4. Instrukcja krok po kroku: Praca w chmurze Google Drive / OneDrive

1. **Krok 1:** Zaloguj się na konto Google lub Microsoft i przejdź do usługi *Google Drive* / *OneDrive*.
2. **Krok 2:** Utwórz nowy folder firmowy: *Projekty_2026* (*Nowy -> Folder*).
3. **Krok 3:** Przeciągnij plik z dysku komputera do okna przeglądarki, aby go przesłać.
4. **Krok 4:** Kliknij prawym przyciskiem myszy na wgrany plik i wybierz *Udostępnij (Share)*.
5. **Krok 5:** Wpisz adres e-mail współpracownika i ustaw uprawnienie na *Edytor*.
6. **Krok 6:** Stwórz nowy dokument tekstowy w chmurze (*Nowy -> Dokumenty Google*).
7. **Krok 7:** Wpisz treść protokołu odbioru usługi i wklej zdjęcie.
8. **Krok 8:** Otwórz *Historię wersji (File -> Version history)* i zobacz zapisane automatycznie wersje.
9. **Krok 9:** Pobierz gotowy plik na komputer w formacie `.docx` lub `.pdf`.
10. **Krok 10:** Zabezpiecz dostęp do konta chmurowego silnym hasłem.

!!! warning "Uważaj na synchronizację stacjonarną!"

    Jeśli zainstalujesz aplikację synchronizującą chmurę z folderem na komputerze, skasowanie pliku w folderze na dysku `C:` spowoduje usunięcie go również z chmury!

---

## Podsumowanie

Własna chmura obliczeniowa zapewnia dostęp do dokumentów firmowych z każdego miejsca na świecie, eliminuje ryzyko utraty danych przy awarii komputera i umożliwia wygodną współpracę w zespole. Świadome zarządzanie uprawnieniami udostępniania i zabezpieczenie konta 2FA to fundament bezpiecznej e-pracy.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Zaloguj się na darmowe konto chmurowe, utwórz folder, wgraj do niego 2 pliki i zmień ich nazwy.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Utwórz w chmurze plik tekstowy i wygeneruj link publiczny do podglądu z ograniczonym uprawnieniem (tylko do odczytu).
3. **Ćwiczenie 3 (Branżowe):** Przeprowadź z kolegą z ławki współedycję w czasie rzeczywistym dokumentu kosztorysu w chmurze. Użyj komentarzy i sugerowania zmian.
4. **Ćwiczenie 4 (Zaawansowane):** Przygotuj kompletną strukturę folderów dla małego warsztatu na dysku chmurowym (Oferty, Projekty, Faktury, BHP), określ poziomy dostępu dla właściciela i pracowników oraz skonfiguruj weryfikację dwuetapową (2FA).

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Czym jest SaaS (Software as a Service) w chmurze obliczeniowej?",
    "opcje": [
      "Modelem, w którym użytkownik korzysta z gotowego oprogramowania przez przeglądarkę WWW bez instalacji",
      "Kablem sieciowym łączącym dwa komputery",
      "Płytą główną do serwera",
      "Systemem chłodzenia wodnego"
    ],
    "poprawna": 0,
    "wyjasnienie": "SaaS (Oprogramowanie jako usługa) udostępnia gotowe aplikacje (np. Google Docs, Canva) bezpośrednio w przeglądarce."
  },
  {
    "pytanie": "Które uprawnienie należy nadadać klientowi, któremu wysyłamy cennik w chmurze, aby niczego nie skasował?",
    "opcje": [
      "Wyłącznie podgląd / Przeglądający (Viewer)",
      "Edytor (Editor)",
      "Administrator serwera",
      "Właściciel konta"
    ],
    "poprawna": 0,
    "wyjasnienie": "Uprawnienie Przeglądający pozwala klientowi przeczytać i pobrać plik bez możliwości wprowadzania zmian."
  },
  {
    "pytanie": "Jaka jest główna zaleta funkcji Historii Wersji w dokumentach chmurowych?",
    "opcje": [
      "Możliwość podglądu i przywrócenia dowolnego wcześniejszego stanu dokumentu w przypadku błędu",
      "Szybsze drukowanie papieru",
      "Zwiększenie rozdzielczości ekranu",
      "Automatyczne płacenie podatków"
    ],
    "poprawna": 0,
    "wyjasnienie": "Historia wersji zapisuje każdy krok pracy, co pozwala cofnąć skasowanie tekstu lub powrócić do wersji sprzed kilku dni."
  },
  {
    "pytanie": "Dlaczego zaleca się włączenie dwuskładnikowego uwierzytelniania (2FA) na koncie chmurowym?",
    "opcje": [
      "Wymaga potwierdzenia logowania kodem z telefonu, chroniąc dane firmowe nawet po przejęciu hasła przez oszusta",
      "Zwiększa prędkość internetu dwukrotnie",
      "Zmniejsza rozmiar plików PDF",
      "Pozwala na pracę bez prądu"
    ],
    "poprawna": 0,
    "wyjasnienie": "2FA (dwuetapowa weryfikacja) drastycznie podnosi bezpieczeństwo konta, wymagając drugiego składnika (telefonu) przy logowaniu."
  },
  {
    "pytanie": "Które z poniższych rozwiązań jest przykładem bezpłatnego lub płatnego Dysku w Chmurze?",
    "opcje": [
      "Google Drive / Microsoft OneDrive / Nextcloud",
      "Kalkulator Windows",
      "Notatnik systemowy",
      "Płyta CD-ROM"
    ],
    "poprawna": 0,
    "wyjasnienie": "Google Drive, OneDrive oraz Nextcloud to popularne platformy składowania i synchronizacji plików w chmurze."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na usługach Cloud Computing dla Szkół Branżowych.*
