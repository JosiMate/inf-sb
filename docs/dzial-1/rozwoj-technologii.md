# 8, 16, 32, 64, czyli jak rozwój technologii wpływa na rozwój społeczeństw

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 3**

Te cztery liczby nie są przypadkowe. To **potęgi dwójki** — i to one rządzą tym,
ile kolorów ma zdjęcie, ile pamięci widzi komputer i dlaczego stary program nie
chce się uruchomić na nowym sprzęcie. Ta lekcja jest o dwóch rzeczach naraz:
**skąd się biorą te liczby** i **co zmieniło się w życiu ludzi**, kiedy urządzenia
liczące stały się tanie i powszechne.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. wyjaśnić, czym jest bit i bajt, i powiedzieć, skąd biorą się liczby 8, 16, 32, 64
    2. uzasadnić, dlaczego układy komputera projektuje się w kodzie dwójkowym, a nie dziesiętnym
    3. odczytać liczbę binarną z wag pozycji i zamienić ją na dziesiętną — na kartce i w kalkulatorze
    4. powiedzieć, co w praktyce znaczy „system 64-bitowy" i czym różni się od 32-bitowego
    5. podać przykłady wpływu postępu technologicznego na zastosowanie komputerów
    6. omówić wpływ rozwoju technologii informacyjnych na rozwój społeczeństw, w tym zalety i koszty zdalnego nauczania
    7. wskazać, czym jest wykluczenie cyfrowe, i podać liczby, które je opisują

## 1. Skąd się biorą 8, 16, 32 i 64

Komputer ma do dyspozycji jedną informację elementarną: **bit** — coś, co może być
w jednym z **dwóch** stanów. Zero albo jeden. Prąd płynie albo nie płynie.

Jeden bit to mało. Dlatego bity łączy się w grupy. Grupa **ośmiu bitów** to
**bajt** — i to jest podstawowa porcja, którą operują komputery od kilkudziesięciu lat.

Liczba różnych układów, jakie można zapisać na *n* bitach, to **2ⁿ**:

| Ile bitów | Ile różnych wartości | Gdzie to spotkasz |
| :---: | ---: | --- |
| 1 | 2 | tak / nie, włączone / wyłączone |
| 4 | 16 | jedna cyfra szesnastkowa, np. w kodzie koloru `#FF8800` |
| **8** (1 bajt) | 256 | jeden znak w starszych kodowaniach, jedna składowa koloru |
| **16** | 65 536 | znaki Unicode w podstawowym zakresie, dźwięk w jakości CD |
| **32** | 4 294 967 296 | adresy pamięci w starszych systemach, adres IPv4 |
| **64** | ok. 18 trylionów (1,8 · 10¹⁹) | adresy pamięci w dzisiejszych systemach |

!!! example "Skąd 16,7 miliona kolorów"

    Zdjęcie zapisane w trybie RGB przechowuje trzy składowe: czerwoną, zieloną
    i niebieską. Każda ma **1 bajt**, czyli 256 poziomów.

    256 × 256 × 256 = **16 777 216** kolorów.

    Dlatego mówi się o „kolorze 24-bitowym" — 3 bajty po 8 bitów. Kiedy widzisz
    zapis `#FF8800`, każda para znaków to jedna składowa zapisana szesnastkowo:
    `FF` = 255, `88` = 136, `00` = 0.

## 2. Dlaczego komputer liczy dwójkowo

Pytanie jest sensowne: ludzie liczą w systemie dziesiętnym, więc czemu maszyna nie?

Bo układ elektroniczny musi **odróżnić** stany od siebie — niezawodnie, miliardy
razy na sekundę, przy zakłóceniach i wahaniach napięcia.

- **Dwa stany** rozróżnia się łatwo: poniżej pewnego napięcia to zero, powyżej —
  jeden. Między nimi jest szeroki margines, w którym może się dziać bałagan,
  i nadal wiadomo, co jest czym.
- **Dziesięć stanów** wymagałoby podziału tego samego zakresu napięć na dziesięć
  przedziałów. Każde zakłócenie mogłoby przesunąć wartość do sąsiedniego przedziału
  i zamienić 7 na 8. Układ byłby droższy, wolniejszy i zawodny.

!!! tip "To nie jest tylko teoria"

    Ta sama zasada działa poza komputerem. Sygnał telewizji cyfrowej albo płyta
    Blu-ray też kodują dwa stany — dlatego obraz albo jest idealny, albo rozsypuje
    się w kwadraty. Sygnał analogowy pogarszał się stopniowo: najpierw śnieg,
    potem szum. Cyfrowy albo działa, albo nie, i to jest cena za odporność.

## 3. Jak odczytać liczbę binarną

Każda pozycja w zapisie dwójkowym ma swoją **wagę** — kolejną potęgę dwójki,
licząc od prawej strony:

| Pozycja | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Waga | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| Przykład | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |

Dodajesz wagi tych pozycji, na których stoi jedynka:

`128 + 32 + 16 + 4 = 180`

Czyli `10110100` to dziesiętnie **180**.

W drugą stronę — z dziesiętnego na dwójkowy — idziesz od największej wagi
i pytasz „czy się mieści":

!!! example "Zamień 200 na dwójkowo"

    | Waga | Mieści się w reszcie? | Bit | Reszta |
    | ---: | --- | :---: | ---: |
    | 128 | tak (200 − 128) | 1 | 72 |
    | 64 | tak (72 − 64) | 1 | 8 |
    | 32 | nie | 0 | 8 |
    | 16 | nie | 0 | 8 |
    | 8 | tak (8 − 8) | 1 | 0 |
    | 4 | nie | 0 | 0 |
    | 2 | nie | 0 | 0 |
    | 1 | nie | 0 | 0 |

    Wynik: `11001000`. Sprawdzenie: 128 + 64 + 8 = 200. ✔

### Kalkulator w trybie Programisty

Nie musisz liczyć wszystkiego ręcznie — ale musisz **umieć sprawdzić**, czy
kalkulator pokazuje to, czego się spodziewasz.

1. Otwórz **Kalkulator** (Windows: ++win+r++, wpisz `calc`).
2. Menu (trzy kreski) → **Programista**.
3. Po lewej zobaczysz cztery wiersze: **HEX**, **DEC**, **OCT**, **BIN**.
4. Kliknij **DEC**, wpisz `180` — w wierszu BIN pojawi się `1011 0100`.
5. Kliknij **BIN**, wpisz `11001000` — w DEC pojawi się `200`.

Kalkulator grupuje bity po cztery, żeby dało się je czytać. Cztery bity to
dokładnie jedna cyfra szesnastkowa — dlatego HEX tak dobrze pasuje do informatyki.

## 4. Co naprawdę znaczy „64-bitowy"

To najczęściej **szerokość adresu pamięci**: ile różnych komórek pamięci procesor
potrafi wskazać.

- System **32-bitowy** ma 2³² adresów, czyli około 4,29 miliarda. Jeśli jeden adres
  wskazuje jeden bajt, maksimum pamięci to **4 GB** — i ani bajta więcej, choćbyś
  włożył do komputera 32 GB. To nie jest ograniczenie producenta ani licencji.
  To arytmetyka.
- System **64-bitowy** ma 2⁶⁴ adresów. To liczba tak duża, że przez najbliższe
  dziesięciolecia nikt o nią nie zahaczy.

!!! warning "Dlatego stary program czasem nie chce działać"

    Program 32-bitowy uruchomisz w systemie 64-bitowym (system ma tryb zgodności).
    Odwrotnie — nie. I dlatego przy pobieraniu sterownika albo programu widzisz
    wybór **x86** (32-bitowy) i **x64** (64-bitowy): to nie są dwie wersje
    „lepsza i gorsza", tylko dwa różne formaty.

Ta sama arytmetyka stoi za adresami internetowymi. **IPv4** ma 32 bity, czyli
około 4,3 miliarda adresów — i one się skończyły. Dlatego powstał **IPv6**,
w którym adres ma 128 bitów.

## 5. Od 2300 tranzystorów do miliardów

Pierwszy komercyjny mikroprocesor, **Intel 4004**, trafił na rynek w listopadzie
1971 roku. Miał **2300 tranzystorów**, przetwarzał dane po **4 bity** naraz,
taktowany był do **740 kHz** i powstawał w procesie **10 mikrometrów**.

Dzisiejszy procesor telefonu ma **dziesiątki miliardów** tranzystorów, przetwarza
dane po 64 bity, pracuje z częstotliwością tysiące razy wyższą, a ścieżki w nim
mierzy się w **nanometrach** — tysiąc razy mniejszych niż mikrometr.

### Prawo Moore'a

W 1965 roku Gordon Moore zauważył, że liczba tranzystorów w układzie scalonym
podwaja się mniej więcej co dwa lata. To nie było prawo przyrody — to była
obserwacja, która przez pół wieku okazywała się trafna i którą branża sama
uczyniła celem.

**Co się z nim dzieje teraz.** Tempo zwolniło i zmienił się jego koszt:

- Produkcja seryjna w procesie **2 nm** ruszyła u TSMC pod koniec **grudnia 2025 r.**,
  w architekturze Gate-All-Around. Samsung uruchomił własny proces 2 nm w tym samym
  miesiącu.
- Jeden **wafel** w procesie 2 nm kosztuje około **30 000 dolarów** — o 50–66 procent
  więcej niż w procesie 3 nm. Cała produkcja TSMC na 2026 rok została wykupiona
  z góry przez dwie firmy.
- Zysk wydajności bywa skromny: Samsung deklaruje przy swoim procesie 2 nm około
  **5 procent** wzrostu wydajności i **8 procent** poprawy efektywności energetycznej.

!!! quote "Dlaczego procesory przestały przyspieszać, a zaczęły się mnożyć"

    Około 2005 roku dalsze podnoszenie częstotliwości przestało się opłacać —
    układy grzały się szybciej, niż dało się je chłodzić. Zamiast jednego szybszego
    rdzenia producenci zaczęli umieszczać w procesorze **kilka rdzeni**. Stąd
    „czterordzeniowy", „ośmiordzeniowy" — i stąd wzięła się potrzeba programów,
    które potrafią pracować równolegle.

## 6. Trzy fale, czyli jak technologia przestawia społeczeństwo

Nowa technologia nie zmienia tylko sprzętu. Zmienia to, **gdzie ludzie pracują,
czego się uczą i jak się porozumiewają**. Alvin Toffler opisał to jako trzy fale:

| Fala | Co ją uruchomiło | Gdzie pracowała większość | Co było najcenniejsze |
| --- | --- | --- | --- |
| rolnicza | uprawa roli | na roli | ziemia |
| przemysłowa | maszyna parowa, elektryczność | w fabryce | kapitał i maszyny |
| informacyjna | komputer i sieć | w usługach, przy przetwarzaniu informacji | **informacja i umiejętności** |

Każda fala budziła te same obawy — że maszyny odbiorą pracę. Za każdym razem
część zawodów faktycznie znikała, a w ich miejsce pojawiały się inne, których
wcześniej nikt nie umiałby nazwać. Zmiana jest realna; katastrofa się nie
wydarzyła. Ale koszt ponoszą ci, którzy nie zdążyli się przekwalifikować —
i to jest sedno sprawy, a nie ogólny bilans.

## 7. Polska w liczbach

Tak wygląda trzecia fala u nas. Dane **GUS za 2025 rok**:

| Co mierzono | Wynik |
| --- | ---: |
| gospodarstwa domowe z dostępem do internetu | **96,2 %** |
| osoby 16–74 lata, które kupiły coś przez internet w ciągu roku | **69,7 %** |
| osoby 16–74 lata korzystające z e-administracji | **61,1 %** |
| — w tym w miastach | 66,6 % |
| — w tym na wsi | 53,0 % |
| przedsiębiorstwa wykorzystujące sztuczną inteligencję | **8,7 %** |

Dwie rzeczy warto z tej tabeli wyczytać. Po pierwsze: **dostęp jest prawie
powszechny** — różnica między miastem a wsią wynosi już tylko jeden punkt
procentowy (97 % wobec 96 % gospodarstw). Po drugie: **korzystanie już nie**.
W e-administracji różnica miasto–wieś to ponad 13 punktów. Sam kabel nie
załatwia sprawy.

## 8. Zdalne nauczanie — co dało i co kosztowało

Najbardziej masowy eksperyment społeczny z technologią, jaki przeszło polskie
szkolnictwo. Warto ocenić go uczciwie, z obu stron.

**Co zyskaliśmy**

- lekcja może się odbyć niezależnie od odległości — dla ucznia z małej
  miejscowości albo chorującego to realna różnica
- nagrany materiał da się obejrzeć drugi raz, we własnym tempie
- kursy, wykłady i dokumentacja, dawniej dostępne tylko na uczelni, są na wyciągnięcie ręki
- nauczyciel i uczeń nauczyli się narzędzi, które są dziś standardem w pracy biurowej

**Co to kosztowało**

- uczeń bez własnego komputera albo bez łącza po prostu wypadał z lekcji
- spadła sprawność w tym, czego nie da się przećwiczyć przez ekran — a w szkole
  zawodowej to większość przedmiotu
- mniej kontaktu z rówieśnikami odbiło się na samopoczuciu i motywacji
- łatwiej było udawać obecność niż faktycznie uczestniczyć

!!! note "Wniosek, który się z tego bierze"

    Technologia dokłada możliwości, ale niczego nie zastępuje za darmo. Zdalnie
    da się przekazać wiedzę; **umiejętności praktycznych** — montażu, pomiaru,
    obsługi maszyny — już nie. Dlatego zdalne nauczanie przyjęło się jako
    uzupełnienie, a nie jako zamiennik.

## 9. Druga strona: wykluczenie cyfrowe

**Wykluczenie cyfrowe** to sytuacja, w której ktoś nie może skorzystać
z rozwiązania dostępnego dla reszty — bo nie ma sprzętu, łącza albo umiejętności.
Im więcej spraw załatwia się wyłącznie przez internet, tym dotkliwsze są jego skutki.

Skala w Polsce:

- **8 %** Polaków **nigdy** nie korzystało z internetu (w 2021 roku było to 11 %)
- **50 %** ma co najmniej podstawowe umiejętności cyfrowe (w 2021 roku — 43 %)
- w grupie **25–34 lata** podstawowe umiejętności cyfrowe ma **75,7 %** osób,
  w grupie **65–74 lata** — **12,3 %**

Ta ostatnia para liczb jest najważniejsza w całej lekcji. Różnica sześciokrotna
oznacza, że e-recepta, e-urząd i bankowość internetowa dla jednej grupy są
ułatwieniem, a dla drugiej — barierą. Dlatego przepisy wciąż wymagają, żeby
sprawę dało się załatwić także przy okienku.

## 10. Najnowsza fala: sztuczna inteligencja

Zmiana, która dzieje się teraz i której skutków nikt jeszcze nie zna. Liczby
z badania z **2026 roku**:

- **85,7 %** Polaków miało kontakt z generatywną AI
- **40,3 %** korzysta z niej regularnie w życiu prywatnym — rok wcześniej **23,3 %**
- najczęstsze zastosowania: wyszukiwanie i streszczanie informacji (50,1 %),
  nauka i rozwój (36,2 %), pomoc techniczna (33,8 %)

Obawy, które przy tym zgłaszają:

| Czego się obawiają | Odsetek | Zmiana rok do roku |
| --- | ---: | --- |
| dezinformacji i deepfake'ów | 41,0 % | — |
| naruszenia prywatności | 37,9 % | — |
| spadku własnego krytycznego myślenia | 30,9 % | wzrost z 25,3 % |
| utraty pracy | 24,5 % | spadek z 29,3 % |

!!! warning "Przeczytaj tę tabelę jeszcze raz"

    Dwie ostatnie linijki idą w **przeciwnych** kierunkach. Strach przed utratą
    pracy maleje — ludzie zobaczyli, że AI raczej zmienia sposób pracy, niż ją
    zabiera. Ale obawa o **własne** myślenie rośnie. To jest trzecia fala
    w pigułce: narzędzie, które zdejmuje z Ciebie wysiłek, zdejmuje razem z nim
    część wprawy.

## Ćwiczenia

!!! question "Ćwiczenie 1. Rachunek na kartce, sprawdzenie w kalkulatorze"

    Zamień na system dwójkowy, licząc **ręcznie** metodą wag: **37**, **100**, **255**.
    Potem sprawdź każdy wynik w Kalkulatorze w trybie Programisty.

    W karcie pracy zapisz trzy wyniki i odpowiedz: **co jest szczególnego w liczbie 255**?

??? success "Rozwiązanie 1"

    - 37 = `100101` (32 + 4 + 1)
    - 100 = `1100100` (64 + 32 + 4)
    - 255 = `11111111`

    255 to największa liczba, jaką da się zapisać na jednym bajcie — wszystkie
    osiem bitów ustawionych na 1. Następna wartość, 256, wymaga już dziewiątego bitu.
    Dlatego składowa koloru kończy się na 255, a nie na 256 czy 300.

!!! question "Ćwiczenie 2. Ile to zajmie miejsca"

    Zdjęcie ma 1920 × 1080 pikseli i zapisane jest w kolorze 24-bitowym, bez
    kompresji. Policz, ile bajtów zajmuje, i podaj wynik w megabajtach.

    Potem odpowiedz: dlaczego plik JPG z tego samego zdjęcia waży kilkaset razy mniej?

??? success "Rozwiązanie 2"

    1920 × 1080 = 2 073 600 pikseli.
    Każdy piksel to 3 bajty, czyli 2 073 600 × 3 = **6 220 800 bajtów** ≈ **5,9 MB**.

    JPG stosuje **kompresję stratną**: usuwa szczegóły, których oko i tak nie
    zauważy, i zapisuje obszary o podobnym kolorze skrótowo. Płaci się za to
    jakością — po kilku zapisach tego samego pliku widać charakterystyczne
    kwadraty wokół krawędzi.

!!! question "Ćwiczenie 3. Kogo dotyczy wykluczenie"

    Wybierz **jedną** sprawę, którą dziś załatwia się głównie przez internet:
    e-recepta, wniosek o dowód osobisty, zakup biletu kolejowego, rejestracja
    do lekarza albo rozliczenie PIT.

    Opisz krok po kroku, **co musi mieć i umieć** osoba, żeby to zrobić samodzielnie.
    Potem wskaż, w którym kroku odpadnie ktoś z wynikiem z grupy 65–74 lata
    z tabeli wyżej — i zaproponuj jedno rozwiązanie, które ten krok ułatwia.

??? success "Wskazówka do rozwiązania 3"

    Typowa lista wymagań okazuje się dłuższa, niż się wydaje: urządzenie, łącze,
    aktywny adres e-mail, numer telefonu odbierający kody, profil zaufany albo
    bankowość elektroniczna, umiejętność odczytania komunikatu o błędzie,
    a często jeszcze umiejętność zapisania i wysłania pliku PDF.

    Najczęściej odpada krok z **uwierzytelnieniem** — profil zaufany i kody SMS.
    Rozwiązania, które realnie pomagają: możliwość załatwienia sprawy przy okienku,
    pomoc wyznaczonej osoby w urzędzie, uproszczony interfejs, szkolenia dla seniorów.

!!! note "Co oddajesz"

    Wyniki wszystkich trzech ćwiczeń wpisujesz do **karty pracy działu I**,
    w zadaniu przypisanym do tego tematu. Do ćwiczenia 1 dołącz zrzut ekranu
    z kalkulatora w trybie Programisty.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Ile różnych wartości można zapisać na jednym bajcie?",
    "opcje": ["8", "64", "256", "1024"],
    "poprawna": 2,
    "wyjasnienie": "Bajt to 8 bitów, a każdy bit ma 2 stany: 2⁸ = 256 różnych układów. Wartości liczbowe to zakres od 0 do 255."
  },
  {
    "pytanie": "Dlaczego układy komputera projektuje się w kodzie dwójkowym?",
    "opcje": [
      "Bo dwójkowy zapis jest krótszy od dziesiętnego",
      "Bo dwa stany napięcia da się odróżnić niezawodnie, nawet przy zakłóceniach",
      "Bo tak jest taniej produkować obudowy",
      "Bo ludzie łatwiej czytają zera i jedynki"
    ],
    "poprawna": 1,
    "wyjasnienie": "Chodzi o niezawodność, nie o wygodę. Przy dwóch stanach między „zero” a „jeden” zostaje szeroki margines napięcia, w którym zakłócenie niczego nie psuje. Zapis dwójkowy jest zresztą DŁUŻSZY od dziesiętnego."
  },
  {
    "pytanie": "Liczba binarna 1011 0100 to dziesiętnie:",
    "opcje": ["164", "172", "180", "196"],
    "poprawna": 2,
    "wyjasnienie": "Jedynki stoją na pozycjach o wagach 128, 32, 16 i 4. Suma: 128 + 32 + 16 + 4 = 180."
  },
  {
    "pytanie": "System 32-bitowy nie obsłuży więcej niż 4 GB pamięci RAM, ponieważ:",
    "opcje": [
      "producenci celowo ograniczyli go licencją",
      "2³² adresów po jednym bajcie daje dokładnie tyle komórek pamięci",
      "starsze płyty główne nie miały więcej gniazd",
      "4 GB to maksimum, jakie mieści się w pamięci podręcznej procesora"
    ],
    "poprawna": 1,
    "wyjasnienie": "To arytmetyka, nie decyzja handlowa. 2³² ≈ 4,29 miliarda adresów; jeżeli jeden adres wskazuje jeden bajt, więcej pamięci procesor po prostu nie potrafi wskazać."
  },
  {
    "pytanie": "Intel 4004 z 1971 roku miał:",
    "opcje": [
      "2300 tranzystorów i przetwarzał dane po 4 bity",
      "23 000 tranzystorów i przetwarzał dane po 8 bitów",
      "2,3 miliona tranzystorów i przetwarzał dane po 16 bitów",
      "2,3 miliarda tranzystorów i przetwarzał dane po 32 bity"
    ],
    "poprawna": 0,
    "wyjasnienie": "2300 tranzystorów, architektura 4-bitowa, taktowanie do 740 kHz, proces 10 mikrometrów. Dzisiejszy procesor telefonu ma dziesiątki miliardów tranzystorów."
  },
  {
    "pytanie": "Prawo Moore'a mówi, że:",
    "opcje": [
      "częstotliwość procesorów rośnie co roku dwukrotnie",
      "liczba tranzystorów w układzie scalonym podwaja się mniej więcej co dwa lata",
      "cena komputera spada o połowę co dwa lata",
      "każdy program z czasem zajmuje dwa razy więcej pamięci"
    ],
    "poprawna": 1,
    "wyjasnienie": "To obserwacja Gordona Moore'a z 1965 roku, nie prawo przyrody. Dotyczy liczby tranzystorów. Częstotliwość przestała rosnąć około 2005 roku — z powodu ciepła — i wtedy producenci przeszli na wiele rdzeni."
  },
  {
    "pytanie": "Według danych GUS za 2025 rok dostęp do internetu w gospodarstwach domowych w Polsce miało:",
    "opcje": ["około 72 %", "około 85 %", "około 96 %", "100 %"],
    "poprawna": 2,
    "wyjasnienie": "96,2 % gospodarstw domowych. Różnica między miastem a wsią to już tylko jeden punkt procentowy — 97 % wobec 96 %."
  },
  {
    "pytanie": "Które zdanie najlepiej opisuje wykluczenie cyfrowe w Polsce?",
    "opcje": [
      "Głównym problemem jest brak łącza internetowego na wsi",
      "Problem praktycznie zniknął, skoro prawie wszyscy mają internet",
      "Dostęp jest już niemal powszechny, ale umiejętności rozkładają się bardzo nierówno — od 75,7 % w grupie 25–34 lata do 12,3 % w grupie 65–74 lata",
      "Dotyczy wyłącznie osób, które nie mają smartfona"
    ],
    "poprawna": 2,
    "wyjasnienie": "Kabel przestał być wąskim gardłem — umiejętności nim są. Dlatego przepisy nadal wymagają, żeby sprawy urzędowe dało się załatwić także osobiście."
  }
]
</script>
</div>

---

!!! info "Skąd wzięte są liczby w tej lekcji"

    - Dostęp do internetu, e-administracja, zakupy online, AI w firmach, umiejętności cyfrowe: GUS, *Społeczeństwo informacyjne w Polsce w 2025 r.* (publikacja z 21 października 2025 r.)
    - Wykluczenie cyfrowe — odsetek osób nigdy niekorzystających z internetu i odsetek z podstawowymi umiejętnościami: dane Ministerstwa Cyfryzacji i GUS przytaczane w 2025 r.
    - Intel 4004: dane techniczne producenta, premiera listopad 1971 r.
    - Produkcja 2 nm: komunikaty TSMC i Samsunga z grudnia 2025 r.
    - Korzystanie z AI przez Polaków: raport branżowy z 2026 r. — **uwaga: nie podaje wielkości próby ani metody badania**, więc traktuj te liczby jako rząd wielkości, nie jako pomiar

*Stan danych sprawdzony 14 września 2026 r. Liczby dotyczące technologii starzeją
się szybciej niż przepisy — przy powoływaniu się na nie sprawdź aktualne wydanie
źródła, a nie notatki z lekcji.*
