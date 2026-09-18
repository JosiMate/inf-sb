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
NL = chr(10)
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
        3: ("dzial-1/rozwoj-technologii.md", "Rozwój technologii a społeczeństwo"),
        4: ("dzial-1/wiedza-w-sieci.md", "Wiedza w sieci"),
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

    Na tej stronie są **treści do nauki** i **materiały do pobrania**. Oceny,
    terminy i odsyłanie wykonanych prac — w **Dzienniku VULCAN**, który pozostaje
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
"""




# ─────────────────────────────────────────────── strony działów
try:
    ZADANIA6 = json.load(open(HERE / "zadania6.json", encoding="utf-8"))
except FileNotFoundError:
    ZADANIA6 = {}


def zadania_celujace_md(naglowek, link_wymagania):
    """Sekcja „Zadania na ocenę celującą” dla działu.

    Treść zadań trzyma narzedzia/zadania6.json — kluczem jest nagłówek działu
    („Dział I. …”), wartością lista zadań. Dział bez wpisu nie dostaje sekcji.
    """
    zad = ZADANIA6.get(naglowek)
    if not zad:
        return ""
    ile = len(zad)
    slowo = "zadanie" if ile == 1 else ("zadania" if ile < 5 else "zadań")
    czesci = [f'??? example "{naglowek} — {ile} {slowo} do wyboru"', ""]
    for i, z in enumerate(zad):
        linie = [f"**{z['ozn']}. {z['tytul']}**", ""]
        if z.get("wymaga"):
            linie += [f"*Do wykonania {z['wymaga']}.*", ""]
        for akapit in z["opis"]:
            linie += [akapit, ""]
        linie += [f"**Oddajesz:** {z['oddajesz']}", ""]
        czesci.append(NL.join("    " + l if l else "" for l in linie))
        if i < ile - 1:
            czesci.append("    ---" + NL)
    return (
        NL + "## Zadania na ocenę celującą" + NL + NL
        + "Zadania na szóstkę są **działowe, nie tematyczne** — obejmują materiał całego" + NL
        + "działu i wymagają czegoś więcej niż powtórzenia ćwiczenia z lekcji. Wybierasz" + NL
        + "**jedno** z listy poniżej." + NL + NL
        + "Pracę oddajesz w Dzienniku VULCAN, w zadaniu **„Zadanie na ocenę celującą:" + NL
        + "Dział …”** założonym do tego działu, w ciągu **dwóch tygodni od zakończenia" + NL
        + "działu**. Plik nazwij `nr<numer w dzienniku>-<litera zadania>`, a w treści" + NL
        + "zadania dopisz 3–5 zdań o tym, co zrobiłeś i co z tego wyszło." + NL + NL
        + "Cała lista jest widoczna **od początku działu**, żebyś miał czas wybrać" + NL
        + "i popracować. Przy każdym zadaniu jest napisane, po którym temacie da się" + NL
        + f"je wykonać. Pełne zasady opisuje strona [wymagań edukacyjnych]({link_wymagania})." + NL + NL
        + NL.join(czesci) + NL)


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

    # zadania na ocenę celującą — treść z narzedzia/zadania6.json
    sekcja6 = zadania_celujace_md(f"Dział {d['nr']}. {d['tytul']}",
                                  "../dzial-1/wymagania-i-bhp.md")

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
{sekcja6}
## Karta pracy

Kartę prowadzisz **przez cały dział**, dopisując po każdej lekcji, co zrobiłeś.
Jest tu, pod spisem tematów — rozwiń ją, kiedy masz coś do wpisania.

<div class="kp-podsumowanie" data-karta="dzial-{numer}"></div>

<span id="karta" class="kp-kotwica"></span>

??? karta "Rozwiń kartę pracy działu {d['nr']}"

    Odpowiedzi zapisują się same w Twojej przeglądarce. To nie jest sprawdzian,
    tylko Twoje portfolio: każda lekcja kończy się czymś gotowym — plikiem,
    dokumentem, modelem, programem — a karta zbiera te efekty razem ze zrzutami
    ekranu. Na koniec działu pobierasz gotowy dokument Worda i oddajesz go przez
    **Zadania domowe w dzienniku VULCAN**.

    !!! warning "Chcesz dokończyć w domu — zapisz postęp do pliku"

        Odpowiedzi zostają w **tej przeglądarce, na tym komputerze**. Zanim
        wyjdziesz z pracowni, kliknij pod kartą **Zapisz do pliku**. Dostaniesz
        plik `postep_inf-sb-dzial-{numer}.json` — przenieś go pendrive'em,
        OneDrive'em albo mailem do siebie, a w domu kliknij **Wczytaj z pliku**.
        Ten sam plik działa w obie strony. Wszystkie działy naraz zapiszesz
        jednym plikiem na stronie [Karty pracy](../karty/index.md).

    <div class="karta-pracy" data-karta="dzial-{numer}"></div>

[:material-folder-multiple-outline: Wszystkie karty pracy](../karty/index.md){{ .md-button }}
{sekcja_pracy_klasowej(d)}"""


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
        "tytul": "Zgłoszenie zadania na ocenę celującą",
        "poziom": "wymagania wykraczające · ocena 6",
        "polecenie": "Wypełnij, jeśli wykonujesz zadanie dodatkowe. <strong>Samą "
                     "pracę oddajesz osobno</strong> — w Dzienniku VULCAN, w zadaniu "
                     "„Zadanie na ocenę celującą” założonym do tego działu, w ciągu "
                     "dwóch tygodni od zakończenia działu. W karcie zostaje "
                     "zgłoszenie i wnioski.",
        "pola": [
            {"typ": "tekst", "id": "cel_temat", "wiersze": 2,
             "pytanie": "Które zadanie z działu wybrałeś? Podaj literę i tytuł"},
            {"typ": "tekst", "id": "cel_opis", "wiersze": 6,
             "pytanie": "Co zrobiłeś i co z tego wyszło? Kilka zdań: na czym polegało "
                        "zadanie, jak je wykonałeś i jaki jest wynik albo wniosek.",
             "podpowiedz": "Zadanie polegało na … . Zrobiłem … . Wyszło mi, że …"},
            {"typ": "tabela", "wiersze": [
                ["cel_plik", "Nazwa pliku oddanego w VULCAN-ie", "nr<numer w dzienniku>-<litera zadania>"],
                ["cel_data", "Data wysłania", ""],
            ]},
        ],
    })

    zadania.append({
        "nr": nr + 3,
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


# ─────────────────────────────────────────────── praca klasowa działu
# Karta portfolio (wyżej) zbiera efekty pracy przez cały dział. Praca klasowa
# jest czymś innym: uczeń pisze ją na lekcji, przy komputerze, i oddaje na
# koniec godziny. Układ zadań idzie za wymaganiami — zadania są ustawione od
# koniecznych do dopełniających, więc ocena wynika z tego, dokąd uczeń doszedł
# samodzielnie. Zadania na ocenę celującą są poza tą kartą, w osobnej zakładce
# działu i oddawane osobno w VULCAN-ie.


def praca_klasowa_dzial_1(d):
    """Dział I: prawo autorskie i licencje, wizerunek, system dwójkowy,
    wyszukiwanie i wiarygodność źródeł. Wszystkie zadania są do wykonania przy
    komputerze — sprawdzamy umiejętność, nie pamięć do definicji."""
    return {
        "id": "inf-sb-pk-dzial-1",
        "tytul": f"Praca klasowa — dział {d['nr']}. {d['tytul']}",
        "przedmiot": "PCEiKZ Szczucin · informatyka · klasa 1W, branżowa szkoła I stopnia",
        "klasa": "1W",
        "sufiks": "INF-SB-PK-DZIAL-1",
        "zadania": [
            {
                "nr": 1,
                "tytul": "Co wolno, a co jest przestępstwem",
                "poziom": "wymagania konieczne · ocena 2",
                "polecenie": "Oceń każdą sytuację. Nie zgadujesz — przy każdej "
                             "odpowiedzi piszesz jedno zdanie uzasadnienia.",
                "pola": [
                    {"typ": "tabela", "wiersze": [
                        ["z1_a", "Wrzucam na swój profil film, który nagrałem sam",
                         "wolno / nie wolno"],
                        ["z1_b", "Udostępniam znajomym serial pobrany z torrenta",
                         "wolno / nie wolno"],
                        ["z1_c", "Używam w prezentacji zdjęcia z sieci bez podania autora",
                         "wolno / nie wolno"],
                        ["z1_d", "Wgrywam do szkolnej gazetki utwór na licencji CC BY, "
                                "podając autora i licencję", "wolno / nie wolno"],
                    ]},
                    {"typ": "tekst", "id": "z1_uzasadnienie", "wiersze": 4,
                     "pytanie": "Uzasadnij po jednym zdaniu do każdego wiersza. "
                                "Przy sytuacjach, których nie wolno — napisz, czym to grozi.",
                     "podpowiedz": "a) …  b) …  c) …  d) …"},
                    {"typ": "tekst", "id": "z1_rodo", "wiersze": 3,
                     "pytanie": "Po co wprowadzono przepisy oparte na RODO? "
                                "Odpowiedz własnymi słowami, jednym–dwoma zdaniami."},
                ],
            },
            {
                "nr": 2,
                "tytul": "System dwójkowy w kalkulatorze",
                "poziom": "wymagania podstawowe · ocena 3",
                "polecenie": "Otwórz <strong>Kalkulator</strong> i przełącz go w tryb "
                             "<strong>Programisty</strong> (<code>Alt + 3</code>). "
                             "Przelicz liczby z tabeli i wpisz wynik w systemie dwójkowym.",
                "pola": [
                    {"typ": "tabela", "wiersze": [
                        ["z2_8", "8 (DEC) w systemie dwójkowym", ""],
                        ["z2_12", "12 (DEC) w systemie dwójkowym", ""],
                        ["z2_64", "64 (DEC) w systemie dwójkowym", ""],
                        ["z2_100", "100 (DEC) w systemie dwójkowym", ""],
                        ["z2_255", "255 (DEC) w systemie dwójkowym", ""],
                    ]},
                    {"typ": "zrzut", "id": "z2_zrzut",
                     "opis": "kalkulator w trybie Programisty z jednym z przeliczeń"},
                    {"typ": "tekst", "id": "z2_wagi", "wiersze": 3,
                     "pytanie": "Wypisz wagi ośmiu pozycji bajtu, od lewej do prawej, "
                                "i pokaż na liczbie 100, które z nich się sumują."},
                    {"typ": "tekst", "id": "z2_bajt", "wiersze": 3,
                     "pytanie": "Ile różnych wartości zapiszesz na jednym bajcie i "
                                "dlaczego akurat tyle? Podaj też najmniejszą i największą."},
                ],
            },
            {
                "nr": 3,
                "tytul": "Znajdź obiekt, którego wolno użyć",
                "poziom": "wymagania podstawowe · ocena 3",
                "polecenie": "Znajdź w sieci <strong>grafikę na licencji Creative "
                             "Commons</strong>, której mógłbyś legalnie użyć w szkolnej "
                             "prezentacji. Skorzystaj z serwisu, który pozwala filtrować "
                             "po licencji — na przykład <code>openverse.org</code> albo "
                             "<code>commons.wikimedia.org</code>.",
                "pola": [
                    {"typ": "tabela", "wiersze": [
                        ["z3_serwis", "Serwis, w którym szukałeś", ""],
                        ["z3_adres", "Adres znalezionego obiektu", ""],
                        ["z3_autor", "Autor", ""],
                        ["z3_licencja", "Oznaczenie licencji", "np. CC BY 4.0"],
                    ]},
                    {"typ": "zrzut", "id": "z3_zrzut",
                     "opis": "strona obiektu z widocznym oznaczeniem licencji"},
                    {"typ": "tekst", "id": "z3_warunki", "wiersze": 4,
                     "pytanie": "Czego wymaga od Ciebie ta konkretna licencja? "
                                "Wypisz warunki i napisz, jak je spełnisz w prezentacji."},
                    {"typ": "tekst", "id": "z3_utwor", "wiersze": 3,
                     "pytanie": "Czym w świetle prawa jest utwór? Podaj jeden przykład "
                                "czegoś, co utworem jest, i jeden — co nie jest."},
                ],
            },
            {
                "nr": 4,
                "tytul": "Wyszukiwanie zaawansowane",
                "poziom": "wymagania rozszerzające · ocena 4",
                "polecenie": "Wykonaj trzy wyszukiwania z użyciem operatorów. Za każdym "
                             "razem przepisz <strong>całe zapytanie</strong> i zanotuj, co "
                             "operator zmienił w wynikach.",
                "pola": [
                    {"typ": "tabela", "wiersze": [
                        ["z4_site", "Zapytanie ograniczone do jednej domeny (operator site:)", ""],
                        ["z4_typ", "Zapytanie szukające pliku PDF (operator filetype:)", ""],
                        ["z4_fraza", "Zapytanie z frazą w cudzysłowie", ""],
                    ]},
                    {"typ": "zrzut", "id": "z4_zrzut",
                     "opis": "wyniki jednego z tych wyszukiwań, z widocznym paskiem zapytania"},
                    {"typ": "tekst", "id": "z4_roznica", "wiersze": 4,
                     "pytanie": "Co dał każdy z operatorów? Napisz po jednym zdaniu, "
                                "porównując wynik z tym samym zapytaniem bez operatora."},
                    {"typ": "tekst", "id": "z4_domyslna", "wiersze": 3,
                     "pytanie": "Gdzie w przeglądarce, z której korzystasz, zmienia się "
                                "domyślną wyszukiwarkę? Opisz drogę przez menu."},
                ],
            },
            {
                "nr": 5,
                "tytul": "Cytat, plagiat i cudzy wizerunek",
                "poziom": "wymagania rozszerzające · ocena 4",
                "polecenie": "Dwie sytuacje z życia szkoły. Rozstrzygnij każdą "
                             "i powołaj się na to, co wiesz z działu.",
                "pola": [
                    {"typ": "tekst", "id": "z5_cytat", "wiersze": 5,
                     "pytanie": "Kolega wkleił do swojej pracy trzy akapity z serwisu "
                                "internetowego i dopisał na końcu adres strony. Czy to jest "
                                "cytat, czy plagiat? Odpowiedz i wyjaśnij, czym te dwie "
                                "rzeczy się różnią."},
                    {"typ": "tekst", "id": "z5_wizerunek", "wiersze": 5,
                     "pytanie": "Na wycieczce ktoś zrobił Ci zdjęcie i wrzucił je na "
                                "publiczny profil klasy, nie pytając Cię o zgodę. Jakie masz "
                                "prawa i co konkretnie możesz zrobić? Wypisz kolejne kroki."},
                    {"typ": "tekst", "id": "z5_zasady", "wiersze": 4,
                     "pytanie": "Podaj trzy zasady, których sam przestrzegasz, publikując "
                                "zdjęcia z innymi osobami.",
                     "podpowiedz": "1.  2.  3."},
                ],
            },
            {
                "nr": 6,
                "tytul": "Sprawdź, komu wierzysz",
                "poziom": "wymagania dopełniające · ocena 5",
                "polecenie": "Wybierz <strong>jedno twierdzenie</strong> z sieci dotyczące "
                             "techniki albo zdrowia i sprawdź je w dwóch niezależnych "
                             "źródłach. Jednym z nich ma być wyszukiwarka specjalistyczna — "
                             "na przykład <code>europeana.eu</code> albo katalog biblioteczny.",
                "pola": [
                    {"typ": "tekst", "id": "z6_twierdzenie", "wiersze": 2,
                     "pytanie": "Sprawdzane twierdzenie"},
                    {"typ": "tabela", "wiersze": [
                        ["z6_a_adres", "Źródło 1 — adres", ""],
                        ["z6_a_kto", "Źródło 1 — kto za nim stoi", ""],
                        ["z6_b_adres", "Źródło 2 — adres (wyszukiwarka specjalistyczna)", ""],
                        ["z6_b_kto", "Źródło 2 — kto za nim stoi", ""],
                    ]},
                    {"typ": "wybor", "id": "z6_werdykt",
                     "pytanie": "Po sprawdzeniu twierdzenie uznaję za",
                     "opcje": ["prawdziwe", "fałszywe", "częściowo prawdziwe",
                               "nie da się rozstrzygnąć"]},
                    {"typ": "tekst", "id": "z6_kryteria", "wiersze": 5,
                     "pytanie": "Po czym poznałeś, które źródło jest wiarygodniejsze? "
                                "Wymień konkretne przesłanki — autor, data, powołanie się "
                                "na badania, cel strony — a nie samo wrażenie."},
                    {"typ": "tekst", "id": "z6_tozsamosc", "wiersze": 4,
                     "pytanie": "Czym może skutkować kradzież tożsamości? Podaj dwa "
                                "konkretne skutki dla okradzionej osoby."},
                ],
            },
        ],
    }


# Dział dostaje pracę klasową dopiero wtedy, gdy ma napisane materiały.
PRACE_KLASOWE = {
    "I": praca_klasowa_dzial_1,
}


def sekcja_pracy_klasowej(d):
    """Blok pracy klasowej na stronie działu. Pusty napis, gdy działu jeszcze
    nie ma w PRACE_KLASOWE — wtedy strona wygląda dokładnie jak dotąd."""
    if d["nr"] not in PRACE_KLASOWE:
        return ""
    numer = NUMER[d["nr"]]
    return f"""
## Praca klasowa — dział {d['nr']}

Tę kartę wypełniasz **na lekcji, przy komputerze**, i oddajesz na koniec
godziny. Zadania są ustawione od najłatwiejszych do najtrudniejszych, zgodnie
z wymaganiami wyżej: zaczynasz od pierwszego i idziesz po kolei.

!!! info "Skąd bierze się ocena"

    Zadania odpowiadają kolejnym poziomom wymagań — pierwsze koniecznym, ostatnie
    dopełniającym. Ocena wynika z tego, **dokąd doszedłeś samodzielnie**, a nie
    z liczby zapisanych zdań. Nie ma sensu przeskakiwać do końca: wymagania są
    kumulatywne, więc zadanie na 5 liczy się dopiero wtedy, gdy wcześniejsze są zrobione.

    Zadania na ocenę celującą są poza tą pracą — masz je w zakładce działu
    i oddajesz osobno w dzienniku VULCAN.

!!! warning "Wolno korzystać z komputera — nie wolno z cudzej pracy"

    Wyszukiwarka, kalkulator i strony z materiałami są na tej pracy potrzebne
    i możesz z nich korzystać. Rozwiązanie ma być Twoje: przy sprawdzaniu mogę
    poprosić, żebyś pokazał na komputerze, jak doszedłeś do wyniku. Zasady
    samodzielności opisuje strona
    [wymagań edukacyjnych](../dzial-1/wymagania-i-bhp.md).

!!! tip "Zanim oddasz"

    Kliknij pod kartą **Pobierz dokument** i oddaj plik tak, jak powiem na
    lekcji. Odpowiedzi zostają też w tej przeglądarce — jeśli lekcja się urwie,
    użyj **Zapisz do pliku**, żeby nic nie przepadło.

<span id="karta-praca-klasowa" class="kp-kotwica"></span>

<div class="kp-podsumowanie" data-karta="dzial-{numer}-praca-klasowa"></div>

???+ karta "Rozwiń kartę pracy klasowej"

    <div class="karta-pracy" data-karta="dzial-{numer}-praca-klasowa"></div>
"""


# ─────────────────────────────────────────────── zbiorcza strona kart
def strona_kart():
    """Spis wszystkich kart ze stanem wypełnienia — „ćwiczeniówka" serwisu.

    Stan liczy karty.js z tego, co leży w przeglądarce; tutaj podajemy tylko,
    które karty istnieją i gdzie ich szukać. Prace klasowe wchodzą na tę samą
    listę, bo uczeń szuka „swojej pracy", a nie kategorii karty.
    """
    pozycje = []
    for d in DZIALY:
        numer = NUMER[d["nr"]]
        pozycje.append({
            "plik": f"dzial-{numer}",
            "tytul": f"Dział {d['nr']}. {d['tytul']}",
            "url": f"../dzial-{numer}/#karta",
        })
        if d["nr"] in PRACE_KLASOWE:
            pozycje.append({
                "plik": f"dzial-{numer}-praca-klasowa",
                "tytul": f"Dział {d['nr']} — praca klasowa",
                "url": f"../dzial-{numer}/#karta-praca-klasowa",
            })
    dane = json.dumps(pozycje, ensure_ascii=False, indent=2)

    return f"""---
hide:
  - navigation
---

# Karty pracy

**Informatyka · klasa 1W · branżowa szkoła I stopnia**

Tu w jednym miejscu widzisz **całą swoją pracę z tego przedmiotu**: ile masz
wypełnione w każdym dziale i kiedy ostatnio przy tym siedziałeś. Kartę
otwierasz, klikając nazwę działu.

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
`moje-karty-pracy.json` ze wszystkimi działami naraz — przenosisz go
pendrive'em, OneDrive'em albo mailem do siebie i na drugim komputerze klikasz
**Wczytaj karty z pliku**. Plik z pojedynczego działu też tu zadziała.

!!! warning "Zrób to przed końcem lekcji"

    Wyczyszczenie danych przeglądarki kasuje odpowiedzi bezpowrotnie. Jeżeli
    pracujesz na komputerze w pracowni, zapisuj plik **po każdych zajęciach** —
    to trwa jedno kliknięcie.

!!! info "Oddawanie prac"

    Gotową kartę pobierasz jako dokument Worda (przycisk pod kartą) i oddajesz
    przez **Zadania domowe w dzienniku VULCAN**. Ta strona nie jest kanałem
    oddawania prac — służy tylko Tobie do pracy.
"""


# ─────────────────────────────────────────────── nawigacja (awesome-nav)
# Nawigację składa wtyczka awesome-nav z plików .nav.yml leżących w katalogach
# docs/. Generator pisze je wszystkie, więc mkdocs.yml zostaje nietknięty —
# wcześniej trzeba było pilnować znaczników w cudzym pliku konfiguracyjnym.
WSTEP_KORZEN = (
    "# Plik generowany przez narzedzia/genstrony_sb.py — nie edytuj ręcznie.\n"
    "# Kolejność i nazwy w lewej kolumnie — wtyczka awesome-nav.\n"
    "# Katalog dopisany bez wpisu niżej trafi na koniec listy (append_unmatched),\n"
    "# więc nowa strona nigdy nie zniknie ze strony w sposób niezauważony.\n"
)
WSTEP_KATALOG = (
    "# Plik generowany przez narzedzia/genstrony_sb.py — nie edytuj ręcznie.\n"
    "# Kolejność i nazwy tematów w tym dziale — wtyczka awesome-nav.\n"
    "# Plik dopisany bez wpisu niżej trafi na koniec listy (append_unmatched)\n"
    "# i dostanie tytuł z nagłówka pierwszego poziomu.\n"
)


def yaml_klucz(tekst):
    """Klucz YAML w cudzysłowie — tytuł działu może zawierać dwukropek,
    który bez cytowania rozbiłby wpis na klucz i wartość."""
    return '"' + tekst.replace('"', '\\"') + '"'


def nawigacja_korzenia():
    linie = [WSTEP_KORZEN, "append_unmatched: true", "nav:", '  - "Start": index.md']
    for d in DZIALY:
        linie.append(f"  - dzial-{NUMER[d['nr']]}")
    linie.append('  - "Karty pracy": karty/index.md')
    return "\n".join(linie) + "\n"


def nawigacja_dzialu(d):
    gotowe = GOTOWE.get(d["nr"], {})
    naglowek = "Dział " + d["nr"] + ". " + d["tytul"]
    linie = [WSTEP_KATALOG, "title: " + yaml_klucz(naglowek),
             "append_unmatched: true", "nav:", '  - "Przegląd działu": index.md']
    for t in d["tematy"]:
        if t["lp"] in gotowe:
            wpis = gotowe[t["lp"]]
            linie.append("  - " + yaml_klucz(etykieta(wpis, t["tytul"]))
                         + ": " + sciezka(wpis).split("/", 1)[1])
    return "\n".join(linie) + "\n"


def zapisz_nawigacje():
    """Pisze .nav.yml w docs/ i w każdym katalogu działu. mkdocs.yml zostaje
    nietknięty — od wdrożenia awesome-nav nie ma w nim już klucza nav."""
    zapisz(".nav.yml", nawigacja_korzenia())
    for d in DZIALY:
        zapisz(f"dzial-{NUMER[d['nr']]}/.nav.yml", nawigacja_dzialu(d))


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
    zapisz_json(f"assets/karty/dzial-{numer}.json", karta_dzialu(d))
    if d["nr"] in PRACE_KLASOWE:
        zapisz_json(f"assets/karty/dzial-{numer}-praca-klasowa.json",
                    PRACE_KLASOWE[d["nr"]](d))
zapisz("karty/index.md", strona_kart())
zapisz_nawigacje()

print(f"\nGotowe: {SUMA} godzin, {len(DZIALY)} działów, {LICZBA_TEMATOW} tematów.")
