# Nie wszystko jest takie oczywiste, czyli jak działa Internet

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 24**

!!! abstract "O tym temacie"

    Świadome i bezpieczne korzystanie z sieci w pracy zawodowej wymaga zrozumienia podstawowych mechanizmów rządzących globalną siecią Internet. W ramach tej lekcji (1h) w Dziale V serwisu `inf-sb` dla Szkoły Branżowej nauczysz się jak działają protokoły sieciowe (TCP/IP), adresy IP (IPv4 vs IPv6), system nazw domenowych (DNS), protokół DHCP oraz jak diagnozować i śledzić połączenia za pomocą poleceń systemowych (`ping`, `tracert`) i programów diagnostycznych.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić pojęcie i rolę protokołów sieciowych (TCP/IP) w przesyłaniu danych
    2. odróżniać adresy IP prywatne od publicznych oraz wersję IPv4 od IPv6
    3. wyjaśnić rolę i działanie serwerów nazw domenowych (DNS - Domain Name System)
    4. opisać działanie i zadania protokołu automatycznej konfiguracji DHCP
    5. stosować polecenie `ping` w Wierszu poleceń do sprawdzania łączności z serwerem
    6. używać polecenia `tracert` / `traceroute` do śledzenia trasy pakietów w sieci
    7. wyjaśnić pojęcie domeny internetowej, jej struktury (TLD, subdomeny) oraz podmiotów je przydzielających (IANA/NASK)
    8. interpretować parametry opóźnień sieciowych (ping / latency w milisekundach)
    9. rozpoznawać funkcję rutera i przełącznika (switcha) w sieci firmowej
    10. diagnozować podstawowe usterki braku dostępu do sieci na stanowisku pracy

## 1. Jak dane podróżują po sieci: Protokół TCP/IP i adresy IP

Internet to globalna sieć połączonych ze sobą komputerów i ruterów. Aby maszyny mogły się porozumieć, stosują wspólny język — **protokół TCP/IP**.

```
+-----------------------------------------------------------------------+
|  MODELE TRANSDUKCJI DANYCH (TCP/IP)                                    |
|  [Aplikacja]  --> HTTPS, DNS, SSH, FTP                               |
|  [Transport]  --> TCP (gwarancja dostarczenia) / UDP (szybkość)       |
|  [Internet]   --> IP (Adresowanie pakietów IPv4 / IPv6)                |
|  [Dostęp]     --> Ethernet, Wi-Fi, Światłowód                         |
+-----------------------------------------------------------------------+
```

### Podstawowe adresy w sieci:

- **Adres IP (np. `192.168.1.15` lub `212.77.98.9`):** Unikalny identyfikator urządzenia w sieci.
- **IPv4 vs IPv6:** IPv4 składa się z 4 bajtów (pula adresów wyczerpała się), IPv6 stosuje zapis szesnastkowy o dużej pojemności.
- **Protokół DHCP:** Automatycznie przydziela adres IP, maskę i bramę komputerom wbijającym się do sieci.

---

## 2. Rola systemu domen DNS i traseologia

Ludzie wolą używać nazw słownych (np. `www.pceikz.pl`), ale komputery łączą się wyłącznie po adresach cyfrowych IP (`195.150.9.37`).

| Usługa / Pojęcie | Rola w sieci |
| --- | --- |
| **DNS (Domain Name System)** | „Książka telefoniczna Internetu” — zamienia nazwę `pceikz.pl` na adres IP |
| **Domena główna (TLD)** | Końcówka adresu (np. `.pl`, `.com`, `.gov.pl`, `.eu`) |
| **NASK / IANA** | Instytucje odpowiedzialne za rejestrację i ład w domenach |

```
UŻYTKOWNIK (www.google.com)  -->  SERWER DNS  -->  ZWRACA IP (142.250.186.46)  -->  POŁĄCZENIE Z SERWEREM
```

!!! info "Co robimy, gdy strona nie działa?"

    Często awaria „braku internetu” to tylko awaria serwera DNS. Jeśli wpisanie adresu `142.250.186.46` otwiera stronę Google, a wpisanie `www.google.com` wyświetla błąd — problem leży po stronie serwera DNS!

---

## 3. Diagnostyka sieciowa: Polecenia ping i tracert

Każdy pracownik i administrator powinien umieścić podstawowe testy sieciowe w swoim warsztacie.

```
Wiersz poleceń (cmd) -> ping google.com    --> Mierzy czas odpowiedzi (ms)
Wiersz poleceń (cmd) -> tracert google.com --> Pokazuje wszystkie węzły (rutery) na trasie
```

### Jak interpretować wyniki?

- **`ping 8.8.8.8`:** Brak odpowiedzi oznacza fizyczny brak połączenia z siecią lub zablokowany ruch ICMP.
- **`tracert wp.pl`:** Wypisuje kolejne serwery (chmury/rutery). Gwiazdki `* * *` oznaczają zapory sieciowe lub zgubiony pakiet.

!!! tip "Czas odpowiedzi (RTT / Ping)"

    Ping poniżej `20 ms` oznacza idealne łącze światłowodowe. Ping powyżej `200 ms` oznacza duże opóźnienia, utrudniające pracę z aplikacjami w chmurze i wideokonferencje.

---

## 4. Instrukcja krok po kroku: Diagnostyka połączenia internetowego w Wierszu poleceń

1. **Krok 1:** Otwórz Wiersz poleceń (*Start -> wpisz `cmd` -> Enter*).
2. **Krok 2:** Sprawdź swój lokalny adres IP i bramę domyślną, wpisując polecenie `ipconfig`.
3. **Krok 3:** Wykonaj test połączenia z ruterem domowym/szkolnym: `ping [adres_bramy]` (np. `ping 192.168.1.1`).
4. **Krok 4:** Wykonaj test połączenia z zewnętrznym serwerem DNS: `ping 8.8.8.8`.
5. **Krok 5:** Sprawdź poprawność działania DNS, wysyłając zapytanie po nazwie: `ping www.gov.pl`.
6. **Krok 6:** Prześledź drogę pakietu do wybranego serwera: wpisz `tracert www.pceikz.pl`.
7. **Krok 7:** Przeanalizuj liczbę przeskoków (skoków / hops) oraz czasy w milisekundach.
8. **Krok 8:** Skopiuj wyniki z okna konsoli do pliku tekstowego raportu.
9. **Krok 9:** Sprawdź właściciela domeny na stronie `whois.nask.pl`.
10. **Krok 10:** Zapisz raport diagnostyczny na potrzeby serwisu.

!!! warning "Uwaga na zapory sieciowe (Firewall)!"

    Niektóre serwery firmowe celowo blokują odpowiedź na polecenie `ping` ze względów bezpieczeństwa. Brak odpowiedzi na ping nie zawsze oznacza, że serwer leży!

---

## Podsumowanie

Internet działa w oparciu o zestaw protokołów TCP/IP, adresację IP, automatyczną konfigurację DHCP oraz system przeliczania nazw DNS. Umiejętność posługiwania się poleceniami diagnostycznymi `ping` i `tracert` pozwala na szybkie zlokalizowanie usterki sieciowej w firmie.

---

## Ćwiczenia

1. **Ćwiczenie 1 (Podstawowe):** Uruchom Wiersz poleceń i odczytaj swój adres IP oraz adres bramy domyślnej za pomocą polecenia `ipconfig`.
2. **Ćwiczenie 2 (Średnio zaawansowane):** Przeprowadź test łączności poleceniem `ping` dla trzech różnych serwisów internetowych i porównaj ich średnie czasy opóźnień (ms).
3. **Ćwiczenie 3 (Branżowe):** Za pomocą polecenia `tracert` prześledź trasę pakietów do serwera hurtowni/portalu branżowego. Policz, przez ile ruterów przechodzi połączenie.
4. **Ćwiczenie 4 (Zaawansowane):** Przygotuj prosty schemat sieci firmowej zawierający ruter, przełącznik (switch), serwer DNS oraz 3 komputery robocze. Przypisz im odpowiednie prywatne adresy IP.

---

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Jaka jest główna rola serwerów DNS (Domain Name System) w necie?",
    "opcje": [
      "Przetłumaczenie zrozumiałej dla człowieka nazwy domeny (np. wp.pl) na adres cyfrowy IP serwera",
      "Automatyczne czyszczenie komputera z kurzu",
      "Drukowanie dokumentów bez papieru",
      "Szyfrowanie połączeń w komunikatorach"
    ],
    "poprawna": 0,
    "wyjasnienie": "DNS pełni rolę cyfrowej książki adresowej, zamieniając nazwy domenowe na numeryczne adresy IP."
  },
  {
    "pytanie": "Do czego służy polecenie systemowe ping uruchamiane w konsoli?",
    "opcje": [
      "Do sprawdzania łączności sieciowej z danym urządzeniem oraz mierzenia czasu odpowiedzi (ms)",
      "Do formatowania dysku twardego",
      "Do pisania wiadomości e-mail",
      "Do instalowania gier"
    ],
    "poprawna": 0,
    "wyjasnienie": "Polecenie ping wysyła pakiety kontrolne (ICMP Echo Request) i mierzy czas oraz obecność odpowiedzi serwera."
  },
  {
    "pytanie": "Który protokół odpowiada za automatyczne przydzielanie adresów IP urządzeniom wbijającym się do sieci?",
    "opcje": [
      "DHCP",
      "FTP",
      "SMTP",
      "POP3"
    ],
    "poprawna": 0,
    "wyjasnienie": "DHCP (Dynamic Host Configuration Protocol) automatycznie nadaje komputerom adres IP, maskę i bramę domyślną."
  },
  {
    "pytanie": "Co robi polecenie tracert (traceroute)?",
    "opcje": [
      "Wyświetla trasę i kolejne rutery (węzły), przez które przechodzą pakiety do serwera docelowego",
      "Kasuje pliki tymczasowe",
      "Zmienia hasło użytkownika",
      "Mierzy zużycie baterii w telefonie"
    ],
    "poprawna": 0,
    "wyjasnienie": "Tracert wypisuje listę wszystkich ruterów po drodze, ułatwiając zlokalizowanie miejsca awarii łącza."
  },
  {
    "pytanie": "Który adres jest przykładem Prywatnego adresu IP stosowanego w sieciach lokalnych (LAN)?",
    "opcje": [
      "192.168.1.50",
      "256.300.1.1",
      "www.google.com",
      "00-11-22-33-44-55"
    ],
    "poprawna": 0,
    "wyjasnienie": "Zakres 192.168.x.x należy do zarezerwowanej puli prywatnych adresów IP używanych wewnątrz sieci domowych i firmowych."
  }
]
</script>
</div>

---

*Stan wiedzy i oprogramowania: wrzesień 2026 r. Przykłady oparte na protokołach TCP/IP i narzędziach konsolowych dla Szkół Branżowych.*
