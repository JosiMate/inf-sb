#!/usr/bin/env python3
"""Generuje serwis inf-sb (informatyka, klasa 1W, branżowa szkoła I stopnia):
   • stronę startową z kafelkami działów i spisem tematów,
   • stronę wymagań edukacyjnych z bhp i zasadami oceniania.

Źródłem jest daneSB.json — scalony przez budujdane.py rozkład materiału
i plan wynikowy. Opisy działów na kafelkach siedzą w daneSB.json (pole
„opis"), bo powstają razem z podziałem na działy.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
import wzo_md  # noqa: E402

ROOT = HERE.parent / "docs"
DZIALY = json.load(open(HERE / "daneSB.json", encoding="utf-8"))

# Materiały gotowe: numer działu -> {numer tematu: "ścieżka/pliku.md"}.
# Strona „Wymagania edukacyjne i bhp" jest treścią pierwszej lekcji, którą
# realizujemy w ramach tematu 1, więc podpięta jest właśnie pod niego.
GOTOWE = {
    "I": {
        1: ("dzial-1/wymagania-i-bhp.md", "Wymagania edukacyjne i bhp"),
        2: ("dzial-1/kim-jestem.md", "Wizerunek w sieci"),
    },
}


def sciezka(wpis):
    """Z wpisu GOTOWE wyciąga samą ścieżkę."""
    return wpis[0] if isinstance(wpis, (tuple, list)) else wpis


def etykieta(wpis, zapas):
    """Z wpisu GOTOWE wyciąga krótką etykietę do lewej nawigacji."""
    return wpis[1] if isinstance(wpis, (tuple, list)) and len(wpis) > 1 else zapas

# ─────────────────────────────────────────────── kontrola spójności
for nr, mapa in GOTOWE.items():
    numery = {t["lp"] for d in DZIALY if d["nr"] == nr for t in d["tematy"]}
    obce = set(mapa) - numery
    if obce:
        sys.exit(f"BŁĄD: w dziale {nr} nie ma tematów o numerach: {sorted(obce)}")

SUMA = sum(d["godziny"] for d in DZIALY)
LICZBA_TEMATOW = sum(len(d["tematy"]) for d in DZIALY)
if SUMA != 30:
    sys.exit(f"BŁĄD: suma godzin = {SUMA}, powinno być 30")
if LICZBA_TEMATOW != 30:
    sys.exit(f"BŁĄD: tematów = {LICZBA_TEMATOW}, powinno być 30")


# Numer działu w adresie: I → 1, II → 2 … Rzymskie zostają na ekranie,
# w ścieżkach wygodniejsze są arabskie.
NUMER = {d["nr"]: i + 1 for i, d in enumerate(DZIALY)}


def godz(n):
    """Polska odmiana: 1 godzina, 2–4 godziny, 5+ godzin."""
    n = int(n)
    if n == 1:
        return "1 godzina"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return f"{n} godziny"
    return f"{n} godzin"


def tematy_sl(n):
    if n == 1:
        return "1 temat"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return f"{n} tematy"
    return f"{n} tematów"


# ─────────────────────────────────────────────── strona startowa
def strona_startowa():
    kafelki, tabele = [], []
    for d in DZIALY:
        gotowe = GOTOWE.get(d["nr"], {})
        numer = NUMER[d["nr"]]
        # Kafelek prowadzi do STRONY DZIAŁU, nie do pierwszego tematu — inaczej
        # kliknięcie „Otwórz dział" wrzucało od razu w treść jednej lekcji.
        # Cel podajemy jako plik (…/index.md), a nie katalog (…/): MkDocs
        # sprawdza wtedy odsyłacz i sam zamienia go na adres katalogowy.
        stan = f"[Otwórz dział](dzial-{numer}/index.md)" + "{ .md-button }"
        kafelki.append(
            f"-   :{d['ikona']}:{{ .lg .middle }} **Dział {d['nr']}. {d['tytul']}**\n\n"
            f"    ---\n\n"
            f"    {d['opis']}\n\n"
            f"    *{godz(d['godziny'])} · {tematy_sl(len(d['tematy']))}"
            f"{'' if gotowe else ' · materiały w przygotowaniu'}*\n\n"
            f"    {stan}"
        )

        wiersze = []
        for t in d["tematy"]:
            plik = sciezka(gotowe[t["lp"]]) if t["lp"] in gotowe else None
            nazwa = f"**[{t['tytul']}]({plik})**" if plik else t["tytul"]
            mat = (':material-check-circle:{ title="Materiał gotowy" } gotowe'
                   if plik else "*w przygotowaniu*")
            wiersze.append(f"| {t['lp']}. {nazwa} | {t['godziny']} | {mat} |")
        tabele.append(
            f"### Dział {d['nr']}. {d['tytul']}\n\n"
            f"*{godz(d['godziny'])}*\n\n{d['opis']}\n\n"
            "| Temat | Godz. | Materiały |\n| --- | :---: | --- |\n"
            + "\n".join(wiersze) + "\n"
        )

    return f"""---
hide:
  - navigation
---

# Informatyka — klasa 1W

**Branżowa szkoła I stopnia · 1 godzina tygodniowo · {godz(SUMA)} w całym cyklu**

Ten przedmiot jest o tym, **jak komputer pomaga w Twoim zawodzie**. Nie chodzi
o teorię informatyki dla niej samej, tylko o umiejętności, które przydają się
w pracy: przygotować ofertę i wizytówkę, policzyć koszty w arkuszu, poprawić
zdjęcie do reklamy, dobrać drukarkę albo skaner, zrobić model 3D, sprawdzić
umowę pod kątem praw autorskich i nie dać się nabrać w sieci.

!!! info "Co gdzie jest"

    Na tej stronie są **treści do nauki** i **materiały do pobrania**. Twoja
    własna praca — to, co wpisujesz po lekcjach — zbiera się w
    [kartach pracy](karty/index.md), po jednej na dział. Oceny, terminy
    i odsyłanie wykonanych prac — w **Dzienniku VULCAN**, który pozostaje
    kanałem obowiązującym.

## Plan pracy

Informatyka w branżowej szkole I stopnia jest **tylko w klasie pierwszej**, po
jednej godzinie tygodniowo — razem {godz(SUMA)}. Każdy temat to jedna lekcja,
więc materiał jest ułożony tak, żeby każde zajęcia kończyły się czymś gotowym:
plikiem, dokumentem, działającym programem.

Materiał dzieli się na **{len(DZIALY)} działów** i idzie od zasad, przez
programowanie i aplikacje, po sprzęt i sieć: co wolno, a czego nie wolno robić
w sieci → jak myśli komputer → czym się pracuje na co dzień → jakie urządzenia
podłączyć → co daje Internet w firmie.

Przy jednej godzinie tygodniowo **podstawą oceny jest praca na lekcji**.
Kto systematycznie kończy ćwiczenia, ma komplet ocen bez pisania dodatkowych prac.

<div class="grid cards wybor-modulu" markdown>

{chr(10).join(chr(10) + k for k in kafelki)}

</div>

## Spis tematów

Możesz odhaczać przerobione tematy — zaznaczenia zostają w Twojej przeglądarce
i nie mają nic wspólnego z ocenami.

<div class="spis-tematow" data-postep="inf-sb-1w" markdown>

{chr(10).join(tabele)}

</div>

## Po co mi to w zawodzie

| Dział | Co z tego zostaje na później |
| --- | --- |
| I. Prawo i bezpieczeństwo | Wiesz, czego nie wolno wrzucić do sieci ani skopiować do własnej oferty — i jak nie stracić dobrego wizerunku zawodowego. |
| II. Programowanie i algorytmy | Rozumiesz, według jakiego schematu działa maszyna sterowana komputerem, i umiesz rozpisać czynność krok po kroku. |
| III. Aplikacje | Robisz sam dokumentację, ofertę, ulotkę, kosztorys i prezentację, zamiast zlecać to komuś. |
| IV. Peryferia | Umiesz dobrać i podłączyć drukarkę, skaner czy ploter i wiesz, co znaczą parametry w ofercie sprzedawcy. |
| V. Sieć | Pracujesz w chmurze, dogadujesz się z zespołem zdalnie, podnosisz kwalifikacje i szukasz pracy przez Internet. |
"""


# ─────────────────────────────────────────────── strona wymagań
POZIOMY = [
    ("dop", "Ocena dopuszczająca (2)", "wymagania konieczne"),
    ("dst", "Ocena dostateczna (3)", "wymagania podstawowe"),
    ("db", "Ocena dobra (4)", "wymagania rozszerzające"),
    ("bdb", "Ocena bardzo dobra (5)", "wymagania dopełniające"),
    ("cel", "Ocena celująca (6)", "wymagania wykraczające"),
]

BHP = """!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. stosować zasady bhp obowiązujące w pracowni i wiedzieć, jak zachować się przy awarii lub ewakuacji
    2. wskazać, co na tym przedmiocie podlega ocenie i według jakich wymagań
    3. zaliczyć zaległość po nieobecności i skorzystać z prawa do poprawy oceny w obowiązującym terminie
    4. opisać tryb ubiegania się o roczną ocenę klasyfikacyjną wyższą niż przewidywana
    5. wskazać, gdzie szukać materiałów do przedmiotu i gdzie oddaje się wykonane prace

## Bezpieczeństwo i higiena pracy w pracowni

Pracownia komputerowa to stanowisko pracy pod napięciem. Część zasad poniżej
chroni Ciebie, część chroni sprzęt i pracę kolegów.

**Zanim zaczniesz**

- do pracowni wchodzisz za zgodą nauczyciela i zajmujesz wyznaczone stanowisko
- okrycia wierzchnie i plecaki zostawiasz tak, by nie blokowały przejść
- przed włączeniem komputera obejrzyj stanowisko: uszkodzony przewód, poluzowane
  gniazdo, ślady zalania czy zapach spalenizny **zgłoś od razu** i nie włączaj sprzętu

**W trakcie pracy**

- nie jesz i nie pijesz przy stanowisku — zalana klawiatura to koniec zajęć
- nie rozkręcasz obudowy, nie odłączasz przewodów i nie przenosisz sprzętu
- pracujesz **na swoim koncie i na swoich plikach**; nie logujesz się na cudze
  i nie zmieniasz ustawień systemu bez polecenia nauczyciela
- nie instalujesz własnego oprogramowania i nie uruchamiasz plików pobranych
  z nieznanych źródeł
- monitor ustaw tak, by górna krawędź ekranu była mniej więcej na wysokości oczu,
  a odległość od ekranu wynosiła co najmniej 50 cm; siedź prosto, ze stopami na podłodze
- po każdych 45 minutach patrzenia w ekran oderwij na chwilę wzrok i spójrz w dal —
  to nie jest dobra rada, tylko zasada higieny pracy przy monitorze

**Gdy coś pójdzie nie tak**

- iskrzenie, dym, zapach spalenizny lub porażenie: **nie dotykaj urządzenia**,
  odsuń się i natychmiast powiadom nauczyciela
- awaryjne wyłączenie zasilania pracowni obsługuje wyłącznie nauczyciel
- zawieszony komputer zgłaszasz nauczycielowi — nie resetujesz sprzętu sam
- w razie ewakuacji zostawiasz sprzęt i wychodzisz wyznaczoną drogą, spokojnie,
  w kolejności wskazanej przez nauczyciela

**Na koniec zajęć**

- zapisujesz swoją pracę w miejscu wskazanym przez nauczyciela
- zamykasz programy i **wylogowujesz się**
- porządkujesz stanowisko: klawiatura, mysz, krzesło na miejscu

!!! danger "Ta wiedza podlega ocenie"

    Znajomość i stosowanie zasad bhp to jedno z wymagań na ocenę dopuszczającą.
    Rażące ich łamanie oznacza odsunięcie od pracy przy komputerze na daną lekcję.

## Zasady oceniania

### Wymagania są kumulatywne

Żeby dostać daną ocenę, trzeba spełniać **wszystkie** wymagania na oceny niższe.
Nie da się dostać czwórki, pomijając to, co jest wpisane przy trójce — nawet jeśli
zrobiło się coś trudniejszego.

| Ocena | Poziom | Co to znaczy w praktyce |
| --- | --- | --- |
| dopuszczająca (2) | konieczne | Wykonujesz ćwiczenie krok po kroku według instrukcji, z pomocą nauczyciela. |
| dostateczna (3) | podstawowe | Samodzielnie robisz zadania omawiane na lekcji i wiesz, do czego służą narzędzia, których używasz. |
| dobra (4) | rozszerzające | Stosujesz poznane narzędzia do nowego zadania i umiesz uzasadnić, czemu wybrałeś takie rozwiązanie. |
| bardzo dobra (5) | dopełniające | Wykonujesz zadania złożone, sam znajdujesz błędy i poprawiasz je; efekt nadaje się do pokazania na zewnątrz. |
| celująca (6) | wykraczające | Wychodzisz poza program: własne projekty, zadania trudniejsze niż na lekcji, konkursy. |

!!! warning "Ocena niedostateczna"

    Jedynkę otrzymuje uczeń, który nie spełnia wymagań na ocenę dopuszczającą:
    nie opanował wiadomości i umiejętności pozwalających kontynuować naukę
    przedmiotu i nie wykonuje zadań o elementarnym stopniu trudności nawet
    z pomocą nauczyciela.

!!! note "Jedna godzina tygodniowo — liczy się każda lekcja"

    Przy jednej godzinie w tygodniu nie ma jak nadrobić miesiąca zaległości.
    Dlatego podstawową formą oceny jest **ćwiczenie wykonane na lekcji**, a nie
    sprawdziany. Praca wykonana niesamodzielnie nie podlega ocenie — możesz
    zostać poproszony o objaśnienie tego, co zrobiłeś.

### Co podlega ocenie

- **ćwiczenia i zadania praktyczne przy komputerze** — podstawowa forma oceniania
- **prace kontrolne podsumowujące dział**, zapowiadane z co najmniej tygodniowym
  wyprzedzeniem
- **kartkówki** z bieżącego materiału (do trzech ostatnich lekcji)
- **projekty**: dokument, arkusz, model 3D, materiał reklamowy lub prezentacja —
  oceniane za efekt końcowy, samodzielność i zgodność z poleceniem
- **odpowiedzi ustne, aktywność na lekcji i praca domowa**
- **osiągnięcia w konkursach** informatycznych i zawodowych

"""


def strona_wymagan():
    bloki = []
    for d in DZIALY:
        czesci = []
        for klucz, naglowek, opis in POZIOMY:
            punkty = d["oceny"].get(klucz, [])
            if not punkty:
                continue
            lista = "\n".join(f"    - {x}" for x in punkty)
            czesci.append(f"    **{naglowek}** — *{opis}*\n\n{lista}\n")
        bloki.append(
            f'??? abstract "Dział {d["nr"]}. {d["tytul"]} — {godz(d["godziny"])}"\n\n'
            + "\n".join(czesci)
        )

    ocenianie = wzo_md.blok(
        forma="praca kontrolna podsumowująca dział",
        forma_b="pracę kontrolną",
        praktyczne=True,
        zwolnienie=True,
        olimpiada="olimpiad i konkursów przedmiotowych",
        extra_zaleglosci=(
            "- ćwiczenie niedokończone na lekcji oddajesz **do końca następnego\n"
            "  tygodnia** — do tego czasu ocena pozostaje niewystawiona",
        ),
    )

    return f"""# Wymagania edukacyjne i bhp

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina tygodniowo**

Ta strona odpowiada na dwa pytania: **jak bezpiecznie pracować w pracowni**
i **za co dostaje się poszczególne oceny**. Warto tu wracać przed każdą pracą
kontrolną — wymagania niżej to lista, według której powstają zadania.

{BHP}{ocenianie}
## Wymagania na poszczególne oceny

Rozwiń dział, żeby zobaczyć, co trzeba umieć na każdą ocenę. Wymagania są
kumulatywne — na ocenę wyższą trzeba spełniać także wszystkie niższe.

{chr(10).join(bloki)}

## Do pobrania

[:material-file-word: Wymagania edukacyjne (.docx)](../pliki/wymagania-edukacyjne-informatyka-1w.docx){{ .md-button download="wymagania-edukacyjne-informatyka-1w.docx" }}
[:material-file-word: Rozkład materiału (.docx)](../pliki/rozklad-materialu-informatyka-1w.docx){{ .md-button download="rozklad-materialu-informatyka-1w.docx" }}

Dokument z wymaganiami zawiera to samo co ta strona, plus rozkład godzin na działy
i przypisanie tematów do rozdziałów podręcznika — w formie do wydrukowania
i do dokumentacji.

!!! note "Co oddajesz z tej lekcji"

    Notatkę z tych zajęć wpisujesz do **[zadania 1 w karcie pracy
    działu I](karta.md#zadanie-1)**. Kartę prowadzisz przez cały dział
    i oddajesz na jego koniec.
"""




# ─────────────────────────────────────────────── strony działów
def strona_dzialu(d):
    """Strona działu: po co ten dział, spis tematów, wymagania, karta pracy."""
    gotowe = GOTOWE.get(d["nr"], {})
    numer = NUMER[d["nr"]]

    wiersze = []
    for t in d["tematy"]:
        plik = sciezka(gotowe[t["lp"]]) if t["lp"] in gotowe else None
        # Odsyłacze są względne wobec strony działu, więc odcinamy przedrostek
        # „dzial-N/" — inaczej wychodziłoby dzial-1/dzial-1/temat.
        cel = plik.split("/", 1)[1] if plik else None
        nazwa = f"**[{t['tytul']}]({cel})**" if cel else t["tytul"]
        mat = (':material-check-circle:{ title="Materiał gotowy" } gotowe'
               if cel else "*w przygotowaniu*")
        wiersze.append(f"| {t['lp']}. | {nazwa} | {t['godziny']} | {t['rozdzial']} | {mat} |")

    poziomy = []
    for klucz, naglowek, opis in POZIOMY:
        punkty = d["oceny"].get(klucz, [])
        if punkty:
            lista = "\n".join(f"    - {x}" for x in punkty)
            poziomy.append(f"    **{naglowek}** — *{opis}*\n\n{lista}\n")

    stan = (f"Gotowe materiały: **{len(gotowe)} z {len(d['tematy'])}** tematów."
            if gotowe else
            "Materiały do tego działu powstają w miarę realizacji programu — "
            "na razie znajdziesz tu spis tematów i wymagania.")

    return f"""# Dział {d['nr']}. {d['tytul']}

**{godz(d['godziny'])} · {tematy_sl(len(d['tematy']))} · klasa 1W · branżowa szkoła I stopnia**

{d['opis']}

{stan}

## Tematy działu

Przy jednej godzinie tygodniowo każdy temat to **jedna lekcja**. Kolumna
„Rozdział" odsyła do podręcznika.

| Lp. | Temat | Godz. | Rozdział | Materiały |
| :---: | --- | :---: | :---: | --- |
{chr(10).join(wiersze)}

## Wymagania na oceny w tym dziale

Wymagania są kumulatywne — na ocenę wyższą trzeba spełniać także wszystkie
niższe. Pełna lista dla całego przedmiotu jest na stronie
[wymagań edukacyjnych](../dzial-1/wymagania-i-bhp.md).

??? abstract "Rozwiń wymagania — dział {d['nr']}"

{chr(10).join(poziomy)}

## Karta pracy działu

Kartę prowadzisz **przez cały dział**, dopisując po każdej lekcji, co zrobiłeś.
Otwiera się na osobnej stronie, więc możesz trzymać ją obok treści lekcji.

<div class="kp-podsumowanie" data-karta="dzial-{numer}"></div>

[:material-clipboard-edit-outline: Otwórz kartę pracy działu {d['nr']}](karta.md){{ .md-button .md-button--primary }}
[:material-folder-multiple-outline: Wszystkie karty](../karty/index.md){{ .md-button }}
"""


# ─────────────────────────────────────────────── strona karty działu
def strona_karty(d):
    """Karta pracy na własnej stronie.

    Wcześniej karta wisiała pod spisem tematów na stronie działu i te dwie
    rzeczy sobie przeszkadzały: strona działu jest MENU (wybierz temat),
    a karta jest WARSZTATEM (wpisuj). Za każdym powrotem po następny temat
    uczeń przewijał własną, do połowy wypełnioną pracę. Osobny adres pozwala
    też trzymać kartę w drugiej karcie przeglądarki, obok lekcji, i wysłać
    do niej odsyłacz.
    """
    numer = NUMER[d["nr"]]
    return f"""# Karta pracy — dział {d['nr']}

**{d['tytul']} · klasa 1W**

Wypełniasz ją **przez cały dział**, po jednej lekcji naraz. Odpowiedzi zapisują
się same w Twojej przeglądarce. Na koniec działu pobierasz gotowy dokument Worda
i oddajesz go przez **Zadania domowe w dzienniku VULCAN**.

[:material-arrow-left: Wróć do tematów działu {d['nr']}](index.md){{ .md-button }}

!!! info "To jest Twoje portfolio, nie sprawdzian"

    Na tym przedmiocie każda lekcja kończy się czymś gotowym: plikiem,
    dokumentem, modelem, programem. Karta zbiera te efekty w jednym miejscu —
    razem ze zrzutami ekranu. Pod koniec roku masz komplet tego, co potrafisz
    zrobić przy komputerze, i to jest coś, co pokazuje się pracodawcy.

!!! warning "Chcesz dokończyć w domu — zapisz postęp do pliku"

    Odpowiedzi zostają w **tej przeglądarce, na tym komputerze**. Zanim wyjdziesz
    z pracowni, kliknij pod kartą **Zapisz do pliku**. Dostaniesz jeden plik
    `postep_inf-sb-dzial-{numer}.json` — przenieś go pendrive'em, OneDrive'em
    albo mailem do siebie, a w domu kliknij **Wczytaj z pliku**. Ten sam plik
    działa w obie strony.

    Wszystkie działy naraz zapiszesz jednym plikiem na stronie
    [Karty pracy](../karty/index.md).

<div class="karta-pracy" data-karta="dzial-{numer}"></div>
"""


# ─────────────────────────────────────────────── zbiorcza strona kart
def strona_kart():
    """Spis wszystkich kart ze stanem wypełnienia — „ćwiczeniówka" serwisu."""
    pozycje = [
        {
            "plik": f"dzial-{NUMER[d['nr']]}",
            "tytul": f"Dział {d['nr']}. {d['tytul']}",
            "url": f"../dzial-{NUMER[d['nr']]}/karta/",
        }
        for d in DZIALY
    ]
    dane = json.dumps(pozycje, ensure_ascii=False, indent=2)

    return f"""---
hide:
  - navigation
---

# Karty pracy

**Informatyka · klasa 1W · branżowa szkoła I stopnia**

Tu w jednym miejscu widzisz **całą swoją pracę z tego przedmiotu**: ile masz
wypełnione w każdym dziale i kiedy ostatnio przy tym siedziałeś. Kartę otwierasz,
klikając nazwę działu.

<div class="kp-przeglad">
<script type="application/json">
{dane}
</script>
</div>

## Jak to działa

Odpowiedzi zapisują się **w przeglądarce na tym komputerze** — nic nie jest
wysyłane do szkoły ani nigdzie indziej. To wygodne, ale ma jeden skutek:
w pracowni i w domu to są dwa osobne komplety.

Dlatego jest przycisk **Zapisz wszystkie karty do pliku**. Dostajesz jeden plik
`moje-karty-pracy.json` ze wszystkimi działami naraz — przenosisz go pendrive'em,
OneDrive'em albo mailem do siebie i na drugim komputerze klikasz **Wczytaj karty
z pliku**. Plik z pojedynczego działu też tu zadziała.

!!! warning "Zrób to przed końcem lekcji"

    Wyczyszczenie danych przeglądarki kasuje odpowiedzi bezpowrotnie. Jeżeli
    pracujesz na komputerze w pracowni, zapisuj plik **po każdych zajęciach** —
    to trwa jedno kliknięcie.

!!! info "Oddawanie prac"

    Gotową kartę pobierasz jako dokument Worda (przycisk na stronie karty)
    i oddajesz przez **Zadania domowe w dzienniku VULCAN**. Ta strona nie jest
    kanałem oddawania prac — służy tylko Tobie do pracy.
"""


# ─────────────────────────────────────────────── działowa karta pracy
def karta_dzialu(d):
    """Karta zbierająca efekty pracy z całego działu.

    Inaczej niż w ASSO, gdzie karta jest dziennikiem wdrożenia serwera, tutaj
    liczy się WYTWÓR: dokument, arkusz, model, ulotka, program. Dlatego przy
    każdym temacie pytamy o to, co powstało i w czym, a nie o przebieg
    konfiguracji.
    """
    numer = NUMER[d["nr"]]
    zadania = []

    for i, t in enumerate(d["tematy"], start=1):
        tytul = t["tytul"] if len(t["tytul"]) <= 70 else t["tytul"][:67] + "…"
        zadania.append({
            "nr": i,
            "tytul": tytul,
            "poziom": f"temat {t['lp']} · {godz(t['godziny'])} · rozdział {t['rozdzial']}",
            "polecenie": "Zapisz, co powstało na tej lekcji. Jeżeli nie zdążyłeś "
                         "skończyć, napisz, na czym stanąłeś — to też jest informacja.",
            "pola": [
                {"typ": "tabela", "wiersze": [
                    [f"t{i}_plik", "nazwa pliku albo tytuł pracy", ""],
                    [f"t{i}_program", "program, w którym to zrobiłeś", ""],
                ]},
                {"typ": "tekst", "id": f"t{i}_co", "wiersze": 4,
                 "pytanie": "Co zrobiłeś i czego nowego się przy tym nauczyłeś"},
                {"typ": "zrzut", "id": f"t{i}_zrzut",
                 "opis": "efekt pracy — gotowy dokument, model, arkusz albo działający program"},
            ],
        })

    nr = len(zadania) + 1
    zadania.append({
        "nr": nr,
        "tytul": "Co było trudne",
        "poziom": "wymagania rozszerzające · ocena 4",
        "polecenie": "Napisz o tym, co nie wyszło za pierwszym razem. Nie chodzi "
                     "o przyznanie się do błędu, tylko o to, żebyś umiał nazwać problem "
                     "i powiedzieć, jak go obszedłeś.",
        "pola": [
            {"typ": "tekst", "id": "trudne_co", "wiersze": 3,
             "pytanie": "Co sprawiło kłopot"},
            {"typ": "tekst", "id": "trudne_jak", "wiersze": 3,
             "pytanie": "Jak sobie poradziłeś — sam, z pomocą kolegi, z instrukcji, z sieci"},
        ],
    })

    zadania.append({
        "nr": nr + 1,
        "tytul": "Do czego przyda się to w zawodzie",
        "poziom": "wymagania dopełniające · ocena 5",
        "polecenie": "Ten przedmiot jest o tym, jak komputer pomaga w pracy. "
                     "Pomyśl o zawodzie, którego się uczysz.",
        "pola": [
            {"typ": "tekst", "id": "zawod_zastosowanie", "wiersze": 4,
             "pytanie": "Gdzie w swoim zawodzie użyjesz tego, co było w tym dziale? "
                        "Podaj konkretną sytuację, nie ogólnik."},
        ],
    })

    zadania.append({
        "nr": nr + 2,
        "tytul": "Samoocena",
        "poziom": "podsumowanie działu",
        "polecenie": "Zajrzyj do wymagań na oceny na stronie tego działu i oceń się "
                     "uczciwie. Ta rubryka nie jest oceną — jest podstawą do rozmowy.",
        "pola": [
            {"typ": "wybor", "id": "samoocena_poziom",
             "pytanie": "Wymagania, które według mnie spełniam w tym dziale",
             "opcje": ["konieczne (2)", "podstawowe (3)", "rozszerzające (4)",
                       "dopełniające (5)", "wykraczające (6)"]},
            {"typ": "tekst", "id": "samoocena_uzasadnienie", "wiersze": 4,
             "pytanie": "Uzasadnij: co konkretnie potrafisz zrobić samodzielnie"},
            {"typ": "tekst", "id": "samoocena_braki", "wiersze": 3,
             "pytanie": "Czego jeszcze nie umiesz i co zrobisz, żeby to nadrobić"},
        ],
    })

    return {
        # Nazwa pliku (dzial-N.json) służy do pobrania definicji, a „id" jest
        # kluczem w localStorage. Wszystkie serwisy stoją pod jednym adresem,
        # więc klucz musi nieść nazwę serwisu — inaczej dział I z inf-sb
        # zderzyłby się z działem I z ASSO.
        "id": f"inf-sb-dzial-{numer}",
        "tytul": f"Dział {d['nr']}. {d['tytul']}",
        "przedmiot": "PCEiKZ Szczucin · informatyka · klasa 1W, branżowa szkoła I stopnia",
        "klasa": "1W",
        "sufiks": f"INF-SB-DZIAL-{numer}",
        "zadania": zadania,
    }


# ─────────────────────────────────────────────── nawigacja w mkdocs.yml
# Nawigacja rośnie z każdym dopisanym tematem, więc trzymanie jej ręcznie
# kończyłoby się rozjazdem ze spisem na stronie. Generator przepisuje blok
# między znacznikami — reszty pliku nie dotyka.
POCZATEK = "# ↓↓↓ nawigacja generowana przez narzedzia/genstrony_sb.py"
KONIEC = "# ↑↑↑ koniec bloku generowanego"


def yaml_klucz(tekst):
    """Klucz YAML w cudzysłowie — tytuł działu może zawierać dwukropek,
    który bez cytowania rozbiłby wpis na klucz i wartość."""
    return '"' + tekst.replace('"', '""') + '"'


def blok_nawigacji():
    linie = ["nav:", "  - Start: index.md"]
    for d in DZIALY:
        numer = NUMER[d["nr"]]
        gotowe = GOTOWE.get(d["nr"], {})
        naglowek = "Dział " + d["nr"] + ". " + d["tytul"]
        linie.append("  - " + yaml_klucz(naglowek) + ":")
        linie.append(f"      - Przegląd działu: dzial-{numer}/index.md")
        for t in d["tematy"]:
            if t["lp"] in gotowe:
                wpis = gotowe[t["lp"]]
                linie.append("      - " + yaml_klucz(etykieta(wpis, t["tytul"]))
                             + ": " + sciezka(wpis))
        # Karta na końcu działu, bo sięga się po nią po lekcji, a nie przed.
        linie.append(f"      - Karta pracy: dzial-{numer}/karta.md")
    linie.append("  - Karty pracy: karty/index.md")
    return "\n".join(linie)


def zapisz_nawigacje():
    plik = HERE.parent / "mkdocs.yml"
    tresc = plik.read_text(encoding="utf-8")
    if POCZATEK not in tresc or KONIEC not in tresc:
        sys.exit(f"BŁĄD: w mkdocs.yml brakuje znaczników {POCZATEK!r} / {KONIEC!r}")
    przed, reszta = tresc.split(POCZATEK, 1)
    _stare, po = reszta.split(KONIEC, 1)
    blok = blok_nawigacji()
    plik.write_text(f"{przed}{POCZATEK}\n{blok}\n{KONIEC}{po}", encoding="utf-8")
    print(f"  mkdocs.yml  (nawigacja: {len(blok.splitlines())} linii)")


# ─────────────────────────────────────────────── zapis
def zapisz(sciezka_pliku, tresc):
    p = ROOT / sciezka_pliku
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(tresc, encoding="utf-8")
    print(f"  {sciezka_pliku}  ({len(tresc.splitlines())} linii)")


def zapisz_json(sciezka_pliku, dane):
    p = ROOT / sciezka_pliku
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {sciezka_pliku}  ({len(dane['zadania'])} zadań)")


zapisz("index.md", strona_startowa())
zapisz("dzial-1/wymagania-i-bhp.md", strona_wymagan())
for d in DZIALY:
    numer = NUMER[d["nr"]]
    zapisz(f"dzial-{numer}/index.md", strona_dzialu(d))
    zapisz(f"dzial-{numer}/karta.md", strona_karty(d))
    zapisz_json(f"assets/karty/dzial-{numer}.json", karta_dzialu(d))
zapisz("karty/index.md", strona_kart())
zapisz_nawigacje()

print(f"\nGotowe: {SUMA} godzin, {len(DZIALY)} działów, {LICZBA_TEMATOW} tematów.")
