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
    "I": {1: "dzial-1/wymagania-i-bhp.md"},
}

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
        pierwszy = next((gotowe[t["lp"]] for t in d["tematy"] if t["lp"] in gotowe), None)
        stan = (f"[Otwórz dział]({pierwszy})" + "{ .md-button }") if pierwszy \
            else "*materiały w przygotowaniu*"
        kafelki.append(
            f"-   :{d['ikona']}:{{ .lg .middle }} **Dział {d['nr']}. {d['tytul']}**\n\n"
            f"    ---\n\n"
            f"    {d['opis']}\n\n"
            f"    *{godz(d['godziny'])} · {tematy_sl(len(d['tematy']))}*\n\n"
            f"    {stan}"
        )

        wiersze = []
        for t in d["tematy"]:
            plik = gotowe.get(t["lp"])
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


# ─────────────────────────────────────────────── zapis
def zapisz(sciezka, tresc):
    p = ROOT / sciezka
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(tresc, encoding="utf-8")
    print(f"  {sciezka}  ({len(tresc.splitlines())} linii)")


zapisz("index.md", strona_startowa())
zapisz("dzial-1/wymagania-i-bhp.md", strona_wymagan())
print(f"\nGotowe: {SUMA} godzin, {len(DZIALY)} działów, {LICZBA_TEMATOW} tematów.")
