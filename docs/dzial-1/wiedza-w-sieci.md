# Wiedza w sieci, czyli Internet mądrych ludzi

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 4**

Wyszukiwarka zwraca miliony wyników w pół sekundy — i to jest jej najmniejsza
zaleta. Problem zaczyna się dalej: **który z tych wyników jest prawdziwy**
i **co wolno z nim zrobić**. Ta lekcja jest o trzech umiejętnościach, które
przydają się w warsztacie tak samo jak w szkole: szybko trafić do konkretu,
sprawdzić, czy można temu wierzyć, i użyć znalezionego materiału legalnie.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. dobrać słowa i operatory wyszukiwania tak, żeby trafić do konkretu zamiast przeglądać setki wyników
    2. poprawić własne zapytanie, kiedy pierwsze nie zadziałało
    3. ocenić wiarygodność strony według pięciu kryteriów i wskazać, na którym dana strona wypada źle
    4. rozpoznać typowe chwyty dezinformacji i sprawdzić zdjęcie wyszukiwaniem wstecznym
    5. wymienić sześć licencji Creative Commons i powiedzieć, co przy każdej wolno zrobić
    6. wskazać różnicę między cytatem a plagiatem
    7. znaleźć i wykorzystać wyszukiwarkę branżową związaną ze swoim zawodem

## 1. Mądre wyszukiwanie — operatory

Wpisanie samego hasła zwraca miliony przypadkowych trafień. Operatory pozwalają
powiedzieć wyszukiwarce, czego **nie** chcesz — a to zwykle skraca listę bardziej
niż dokładanie kolejnych słów.

| Operator | Przykład | Co robi |
| :--- | :--- | :--- |
| `" "` | `"montaż płyt gipsowo-kartonowych"` | szuka dokładnie tej frazy, w tej kolejności |
| `-` | `silnik elektryczny -sklep -cena` | wyrzuca strony zawierające dane słowo |
| `site:` | `norma site:gov.pl` | przeszukuje tylko tę witrynę albo domenę |
| `filetype:` | `instrukcja obsługi filetype:pdf` | zwraca wyłącznie pliki danego typu |
| `OR` | `"spawanie TIG" OR "spawanie MIG"` | szuka jednego **albo** drugiego |
| `*` | `jak wymienić * w pralce` | gwiazdka zastępuje dowolne słowo |
| `intitle:` | `intitle:cennik usługi hydrauliczne` | słowo musi być w tytule strony |

!!! warning "Trzy rzeczy, na których łatwo się przejechać"

    - **`OR` pisze się wielkimi literami.** Małe `or` wyszukiwarka potraktuje jak
      zwykłe słowo. Polskie „lub" i „i" **nie są** operatorami — nie działają.
      Zamiennikiem `OR` jest pionowa kreska `|` — działa tak samo.
    - **`OR` łączy sąsiednie słowa, nie całe zapytania.** `spawanie TIG OR MIG`
      znaczy „spawanie, a potem TIG albo MIG" — czyli nie to, o co Ci chodziło.
      Dlatego całe warianty bierze się w cudzysłów albo w nawias.
    - **Operatory to nie jest gwarancja.** Wyszukiwarki zmieniają zasady bez
      zapowiedzi, a część operatorów nigdy nie była oficjalnie opisana. Jeżeli
      wynik wygląda dziwnie, sprawdź zapytanie na prostszej wersji.

### Kiedy pierwsze zapytanie nie zadziałało

To jest umiejętność sama w sobie — i częściej potrzebna niż znajomość operatorów.

- **Za dużo wyników** → dodaj cudzysłów, dorzuć `site:` albo `filetype:`
- **Wyniki ze sklepów zamiast wiedzy** → `-sklep -cena -promocja -allegro`
- **Same stare strony** → w wyszukiwarce **Narzędzia → dowolny czas → ostatni rok**
- **Wyniki po polsku są słabe** → zadaj pytanie po angielsku. W technice
  dokumentacja producenta prawie zawsze jest anglojęzyczna i prawie zawsze jest
  lepsza od tłumaczeń
- **Nie wiesz, jak nazwać rzecz** → opisz ją i dodaj słowo `nazwa` albo poszukaj
  w katalogu części zamiast w wyszukiwarce ogólnej

## 2. Czy można temu wierzyć — pięć pytań

Zanim wykorzystasz informację w nauce albo w pracy, zadaj pięć pytań. W literaturze
anglojęzycznej ten zestaw nosi skrót **CRAAP** — od pierwszych liter angielskich nazw.

| Kryterium | Pytanie, które zadajesz | Zły znak |
| :--- | :--- | :--- |
| **Aktualność** | Kiedy to opublikowano albo zaktualizowano? | brak daty, martwe odsyłacze |
| **Istotność** | Czy to odpowiada na **moje** pytanie i na moim poziomie? | tekst o czymś obok tematu |
| **Autorstwo** | Kto to napisał? Kto za tym stoi? | brak autora, brak kontaktu, brak informacji „o nas" |
| **Dokładność** | Skąd wzięte są dane? Czy podano źródła? | okrągłe liczby bez źródła, błędy językowe |
| **Cel** | Po co powstała ta strona? | sprzedaż, reklama, granie na emocjach |

!!! tip "Najszybszy test z tych pięciu"

    Zacznij od **celu**. Strona, która chce Ci coś sprzedać, nie napisze, że
    produkt konkurencji jest lepszy — nawet jeśli jest. To nie znaczy, że kłamie;
    znaczy, że pokazuje wycinek. Do porównania sprzętu szukaj testu z pomiarami,
    nie opisu w sklepie.

!!! example "Dwie strony o tym samym"

    Szukasz, czy do danego kleju można dodać wodę. Znajdujesz:

    - wpis na forum sprzed ośmiu lat, autor „Marek84", bez zdjęć
    - **kartę techniczną producenta** w PDF, z datą wydania i numerem wersji

    Karta techniczna wygrywa na czterech kryteriach z pięciu. Forum bywa cenne —
    ale jako sygnał, czego szukać w karcie, nie jako źródło.

## 3. Dezinformacja — jak to działa i jak to sprawdzić

**Fake news** to nie jest po prostu pomyłka. To informacja **celowo** nieprawdziwa
albo przekręcona, przygotowana tak, żeby ludzie chcieli ją podać dalej.

Typowe chwyty, po których je poznasz:

- **Nagłówek obiecuje więcej niż treść** — „Naukowcy ostrzegają…", a w tekście
  jedno badanie na 30 osobach
- **Prawdziwe zdjęcie, fałszywy podpis** — najczęstsza forma; zdjęcie jest
  autentyczne, tylko z innego miejsca albo sprzed lat
- **Brak konkretu** — „eksperci twierdzą", ale żadnego nazwiska ani instytucji
- **Emocja zamiast argumentu** — tekst ma Cię rozzłościć albo przestraszyć,
  bo wtedy podaje się go dalej bez czytania
- **Podrobiony adres** — domena łudząco podobna do prawdziwej redakcji

### Jak sprawdzić zdjęcie

To najprostsza i najskuteczniejsza rzecz, jakiej można się tu nauczyć:
**wyszukiwanie wsteczne obrazem**.

1. Kliknij zdjęcie prawym przyciskiem → **Szukaj obrazu w Google** (albo
   otwórz Grafikę Google i wgraj plik ikoną aparatu).
2. Wyszukiwarka pokaże, gdzie jeszcze to zdjęcie się pojawiło — **i kiedy
   najwcześniej**.
3. Jeżeli zdjęcie „z wczorajszego pożaru" istnieje w sieci od 2019 roku,
   sprawa jest zamknięta.

!!! abstract "Gdzie sprawdzić, czy coś już zweryfikowano"

    Zanim sam zaczniesz szukać, zajrzyj do serwisów, które robią to zawodowo.
    W Polsce działają m.in. **Demagog**, **Konkret24** i **AFP Sprawdzam**.
    Wpisujesz hasło z nagłówka — bardzo często sprawa jest już opisana.

!!! warning "Deepfake — dlaczego to jest trudniejsze"

    Materiały wygenerowane przez sztuczną inteligencję nie mają „oryginału",
    więc wyszukiwanie wsteczne nic nie znajdzie. Tu pomaga co innego: sprawdź,
    czy **poważne redakcje** podają tę samą informację. Sensacja, którą ma
    wyłącznie jedno nieznane konto, prawie zawsze jest nieprawdziwa — i to
    działa niezależnie od tego, jak dobrze wygląda nagranie.

## 4. Licencje Creative Commons

Pobranie grafiki z wyszukiwarki i wstawienie jej do własnego projektu, ulotki
czy strony to **naruszenie prawa autorskiego** — nawet jeśli podasz autora.
Zgoda musi istnieć wcześniej. Licencje **Creative Commons** to gotowa zgoda,
którą autor daje z góry wszystkim.

Licencja składa się z klocków. Klocki to warunki:

| Oznaczenie | Nazwa | Co oznacza dla Ciebie |
| :---: | :--- | :--- |
| **BY** | Uznanie autorstwa | musisz podać autora, tytuł i licencję |
| **SA** | Na tych samych warunkach | swoją przeróbkę udostępniasz na tej samej licencji |
| **NC** | Użycie niekomercyjne | nie wolno używać zarobkowo |
| **ND** | Bez utworów zależnych | nie wolno przerabiać ani wycinać fragmentów |

Z tych klocków powstaje **sześć** licencji — warunek **BY** jest w każdej:

| Licencja | Wolno przerabiać? | Wolno zarabiać? |
| :--- | :---: | :---: |
| **CC BY** | tak | tak |
| **CC BY-SA** | tak, na tej samej licencji | tak |
| **CC BY-NC** | tak | **nie** |
| **CC BY-NC-SA** | tak, na tej samej licencji | **nie** |
| **CC BY-ND** | **nie** | tak |
| **CC BY-NC-ND** | **nie** | **nie** |

Aktualna wersja licencji to **4.0** — dlatego przy materiale zobaczysz zapis
w rodzaju `CC BY-SA 4.0`. Osobno funkcjonuje **CC0**, czyli zrzeczenie się praw:
z takim materiałem możesz zrobić wszystko, bez podawania autora.

!!! warning "Nie każde „darmowe" to Creative Commons"

    Serwisy takie jak **Unsplash** czy **Pexels** mają **własne licencje**, nie CC.
    Zwykle pozwalają na użycie komercyjne i **nie wymagają** podania autora —
    ale zabraniają innych rzeczy, na przykład budowania z tych zdjęć konkurencyjnego
    serwisu. Jeżeli w zadaniu masz podać oznaczenie licencji CC, zdjęcie
    z Unsplasha się do tego **nie nadaje** — bo takiego oznaczenia nie ma.

    Pewne źródła materiałów na licencjach CC: **Wikimedia Commons**, **Openverse**,
    **Flickr** z filtrem licencji, a także Grafika Google → **Narzędzia → Prawa użytkowania**.

### Jak poprawnie oznaczyć wykorzystany materiał

Najprostszy wzór, który spełnia warunek BY — **cztery elementy**:

> Zdjęcie: *Warsztat samochodowy* (autor: Jan Kowalski), źródło: Wikimedia Commons,
> licencja: CC BY-SA 4.0

Tytuł, autor, skąd wzięte, na jakiej licencji. Bez któregokolwiek z tych czterech
elementów warunek BY nie jest spełniony.

### Cytat a plagiat

To dwie różne rzeczy i różnica jest ostra:

- **Cytat** to przytoczenie **fragmentu** cudzej pracy **z podaniem autora
  i źródła**, uzasadnione wyjaśnianiem, analizą albo nauczaniem. Prawo autorskie
  na to pozwala i nie trzeba pytać o zgodę.
- **Plagiat** to podanie cudzej pracy jako własnej — niezależnie od długości.
  Skopiowany akapit bez źródła jest plagiatem tak samo jak skopiowana cała praca.

Uwaga na pułapkę: **przepisanie cudzego tekstu własnymi słowami też jest plagiatem**,
jeżeli nie podasz, skąd wziąłeś myśl. Zmiana szyku zdania niczego nie załatwia.

## 5. Wyszukiwarki branżowe

Wyszukiwarka ogólna przeszukuje to, co jest w otwartym internecie. Duża część
wiedzy zawodowej tam nie leży — siedzi w bazach, do których trzeba wejść osobno.

| Czego szukasz | Gdzie szukać |
| :--- | :--- |
| normy i przepisy techniczne | katalog **PKN**, Dziennik Ustaw (`isap.sejm.gov.pl`) |
| części, symbole, zamienniki | katalogi producentów i hurtowni branżowych |
| dane techniczne materiału | **karta techniczna** i **karta charakterystyki** na stronie producenta |
| opisy rozwiązań i patenty | baza **Urzędu Patentowego RP**, **Espacenet** |
| artykuły naukowe i techniczne | **Google Scholar**, biblioteki cyfrowe |
| dokumentacja podzespołów elektronicznych | wyszukiwarki **datasheetów** |

!!! tip "Dlaczego to działa lepiej"

    W bazie branżowej wpisujesz **symbol albo numer katalogowy**, a nie opis
    słowny — i dostajesz jeden właściwy wynik zamiast tysiąca przybliżonych.
    To jest różnica między „jaka śruba do tego pasuje" a wpisaniem oznaczenia
    z rysunku.

## Ćwiczenia

!!! question "Ćwiczenie 1. Precyzyjne wyszukiwanie"

    Znajdź **plik PDF** z oficjalną statystyką dotyczącą rynku pracy albo edukacji
    w Polsce. Użyj operatorów `filetype:pdf` oraz `site:gov.pl`.

    Potem **zepsuj** własne zapytanie: usuń oba operatory i policz, na którym
    miejscu wyników pojawia się ten sam dokument (albo czy pojawia się w ogóle).

    **Zapisujesz:** użytą frazę wyszukiwania, odsyłacz do pliku oraz odpowiedź,
    ile dały operatory.

??? success "Wskazówka do rozwiązania 1"

    Działające zapytania to na przykład:
    `bezrobocie filetype:pdf site:stat.gov.pl` albo
    `"absolwenci szkół zawodowych" filetype:pdf site:gov.pl`.

    Bez operatorów na górze wyników wychodzą zwykle artykuły prasowe omawiające
    dane, a nie same dane. To jest sedno ćwiczenia: **operatory prowadzą do
    źródła, nie do komentarza o źródle**.

!!! question "Ćwiczenie 2. Dwa źródła o tym samym"

    Wybierz jedną nowinkę techniczną z ostatnich tygodni. Znajdź **dwa** teksty
    na jej temat: jeden w serwisie informacyjnym, drugi u **producenta albo
    w dokumentacji**.

    Porównaj je według pięciu kryteriów z punktu 2. Wskaż co najmniej jedną rzecz,
    którą jedno źródło podaje, a drugie pomija — i napisz, dlaczego tak jest.

    **Zapisujesz:** oba odsyłacze, tabelkę porównania i jedno zdanie wniosku.

??? success "Wskazówka do rozwiązania 2"

    Najczęstsza różnica: serwis informacyjny podaje **efekt** („dwa razy
    szybszy"), producent podaje **warunki pomiaru** (przy jakim obciążeniu,
    w jakiej konfiguracji, wobec czego). Pominięcie warunków nie jest kłamstwem,
    ale czyni liczbę bezużyteczną — i to jest wniosek, o który tu chodzi.

!!! question "Ćwiczenie 3. Grafika, którą wolno wykorzystać"

    Znajdź w **Wikimedia Commons** albo w **Openverse** zdjęcie lub ilustrację
    związaną z zawodem, którego się uczysz. Materiał musi być na licencji
    **Creative Commons** — ma mieć widoczne oznaczenie w rodzaju `CC BY-SA 4.0`.

    **Zapisujesz:** odsyłacz do materiału i gotową notę o źródle, zbudowaną
    z czterech elementów ze wzoru w punkcie 4. Dopisz też, **czy wolno Ci to
    zdjęcie przerobić** i skąd to wiesz.

??? success "Wskazówka do rozwiązania 3"

    O tym, czy wolno przerabiać, decyduje obecność członu **ND**. Jeżeli
    w oznaczeniu go nie ma — wolno. Jeżeli jest `ND`, zdjęcie możesz
    rozpowszechniać tylko w oryginalnej postaci; przycięcie albo nałożenie
    napisu jest już utworem zależnym.

    Uwaga: jeżeli trafisz na materiał z Unsplasha albo Pexelsa, oznaczenia
    CC przy nim nie znajdziesz — to inna licencja i do tego ćwiczenia się
    nie nadaje.

!!! note "Co oddajesz"

    Wyniki wszystkich trzech ćwiczeń wpisujesz do **karty pracy działu I**,
    w zadaniu przypisanym do tego tematu. Do ćwiczenia 3 dołącz zrzut ekranu
    strony z widocznym oznaczeniem licencji.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Chcesz znaleźć dokładnie frazę „montaż płyt gipsowo-kartonowych”. Jak zapiszesz zapytanie?",
    "opcje": [
      "montaż płyt gipsowo-kartonowych",
      "\"montaż płyt gipsowo-kartonowych\"",
      "montaż+płyt+gipsowo-kartonowych",
      "intitle:montaż płyt"
    ],
    "poprawna": 1,
    "wyjasnienie": "Cudzysłów wymusza dokładną frazę w podanej kolejności. Bez niego wyszukiwarka potraktuje to jak zestaw osobnych słów i pokaże też strony, na których stoją one w różnych miejscach tekstu."
  },
  {
    "pytanie": "Które zapytanie poprawnie szuka stron o spawaniu metodą TIG ALBO MIG?",
    "opcje": [
      "spawanie TIG lub MIG",
      "spawanie TIG or MIG",
      "\"spawanie TIG\" OR \"spawanie MIG\"",
      "spawanie TIG i MIG"
    ],
    "poprawna": 2,
    "wyjasnienie": "OR musi być wielkimi literami i powinien łączyć całe warianty, nie pojedyncze wyrazy. Polskie „lub” i „i” nie są operatorami — wyszukiwarka potraktuje je jak zwykłe słowa."
  },
  {
    "pytanie": "Co robi operator site:?",
    "opcje": [
      "pokazuje mapę witryny",
      "ogranicza wyniki do wskazanej witryny lub domeny",
      "wyklucza wskazaną witrynę z wyników",
      "sprawdza, czy witryna jest bezpieczna"
    ],
    "poprawna": 1,
    "wyjasnienie": "site:gov.pl zawęża wyniki do stron w tej domenie. Żeby witrynę wykluczyć, trzeba dopisać przed nim minus: -site:przyklad.pl."
  },
  {
    "pytanie": "Widzisz zdjęcie podpisane „wczorajsza powódź w naszym regionie”. Od czego zaczynasz sprawdzanie?",
    "opcje": [
      "od zapytania znajomych, czy też to widzieli",
      "od wyszukiwania wstecznego obrazem — sprawdzasz, gdzie i kiedy zdjęcie pojawiło się wcześniej",
      "od policzenia komentarzy pod wpisem",
      "od sprawdzenia, czy zdjęcie jest ostre"
    ],
    "poprawna": 1,
    "wyjasnienie": "Najczęstsza forma dezinformacji to prawdziwe zdjęcie z fałszywym podpisem. Wyszukiwanie wsteczne pokazuje najwcześniejsze wystąpienie — jeżeli zdjęcie krąży od kilku lat, sprawa jest rozstrzygnięta."
  },
  {
    "pytanie": "Ile jest licencji Creative Commons zbudowanych z warunków BY, SA, NC i ND?",
    "opcje": ["cztery", "sześć", "osiem", "dwanaście"],
    "poprawna": 1,
    "wyjasnienie": "Sześć: BY, BY-SA, BY-NC, BY-NC-SA, BY-ND, BY-NC-ND. Warunek BY występuje w każdej. Osobno funkcjonuje CC0 — zrzeczenie się praw, które licencją w tym sensie nie jest."
  },
  {
    "pytanie": "Znalazłeś ilustrację na licencji CC BY-ND 4.0. Chcesz ją przyciąć i dodać napis. Wolno?",
    "opcje": [
      "Tak, pod warunkiem podania autora",
      "Tak, bo licencja jest w wersji 4.0",
      "Nie — człon ND zabrania tworzenia utworów zależnych, a przycięcie i napis to właśnie przeróbka",
      "Tak, jeżeli nie zarabiasz na efekcie"
    ],
    "poprawna": 2,
    "wyjasnienie": "ND (Bez utworów zależnych) pozwala rozpowszechniać materiał wyłącznie w oryginalnej postaci. Podanie autora spełnia warunek BY, ale nie znosi ND. Brak zarobku dotyczyłby członu NC, którego w tej licencji nie ma."
  },
  {
    "pytanie": "Zdjęcie pobrane z Unsplasha:",
    "opcje": [
      "jest zawsze na licencji CC BY 4.0",
      "podlega własnej licencji Unsplash, która nie wymaga podania autora, ale nie jest licencją Creative Commons",
      "jest w domenie publicznej i nie ma żadnych ograniczeń",
      "wymaga wykupienia licencji przed użyciem komercyjnym"
    ],
    "poprawna": 1,
    "wyjasnienie": "Unsplash ma własną licencję. Pozwala na użycie komercyjne i nie wymaga oznaczenia autora, ale zabrania na przykład budowania z tych zdjęć konkurencyjnego serwisu. Oznaczenia „CC” przy takim zdjęciu nie znajdziesz."
  },
  {
    "pytanie": "Przepisałeś akapit z cudzego artykułu własnymi słowami i nie podałeś źródła. To:",
    "opcje": [
      "dozwolony cytat, bo tekst jest Twój",
      "plagiat — zmiana sformułowań nie zmienia tego, że myśl jest cudza",
      "dozwolone, jeżeli akapit ma mniej niż pięć zdań",
      "dozwolone w pracy szkolnej, zabronione tylko w publikacjach"
    ],
    "poprawna": 1,
    "wyjasnienie": "Cytat wymaga podania autora i źródła — bez tego jest plagiatem, niezależnie od długości i od tego, czy przepisałeś dosłownie, czy przeredagowałeś. Cudza jest tu myśl, nie tylko szyk zdania."
  }
]
</script>
</div>

---

!!! info "Skąd wzięte są informacje w tej lekcji"

    - Licencje Creative Commons, ich warunki i aktualna wersja 4.0: Creative Commons Polska, *Poznaj licencje Creative Commons*
    - Warunki korzystania ze zdjęć Unsplash: oficjalna licencja serwisu (unsplash.com/license)
    - Zestaw pięciu kryteriów oceny źródła jest znany w literaturze anglojęzycznej jako test CRAAP
    - Polskie serwisy factcheckingowe: Demagog, Konkret24, AFP Sprawdzam

*Stan sprawdzony 14 września 2026 r. Operatory wyszukiwania i warunki licencji
serwisów ze zdjęciami zmieniają się bez zapowiedzi — przy pracy, która ma pójść
dalej niż zeszyt, sprawdź licencję na stronie, z której pobierasz materiał, a nie
w notatkach z lekcji.*
