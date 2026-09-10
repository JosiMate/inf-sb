#!/usr/bin/env python3
"""Łączy rozkład materiału 1W z planem wynikowym w jeden zestaw danych.

Wejście:
    rozklad.json  – 30 tematów (lp, temat, godz) wyciągniętych z Informatyka_1W.docx
    plan.json     – 5 działów, w każdym tematy z wymaganiami na 5 poziomów ocen

Wyjście:
    daneSB.json   – wspólne źródło dla generatora .docx i generatora stron
    daneSB.js     – ten sam zestaw jako moduł CommonJS (dla gen1w.js)

Tytuły tematów bierzemy z rozkładu (to dokument nauczyciela), poza jednym
przypadkiem: w temacie 25 rozkład ma literówkę („informatyka oszczędzają
czas"), więc wchodzi poprawna wersja z planu wynikowego. Temat 10 jest w obu
dokumentach nazwany inaczej i tu wygrywa rozkład.
"""
import json
import re
import unicodedata

ROZDZIAL = re.compile(r"\s*Rozdzia[łl]\s*(\d+)\s*$")

POPRAWKI = {
    25: "Firma w sieci, czyli jak informatyka oszczędza czas",
}

RZYMSKIE = ["I", "II", "III", "IV", "V"]

# Skrót do nazw plików/katalogów na stronie — po jednym na dział.
SLUGI_DZIALOW = [
    "prawo-i-bezpieczenstwo",
    "programowanie",
    "aplikacje",
    "peryferia",
    "siec",
]

# Krótkie hasło na kafelek działu i ikona Material.
# Nazwa ikony w postaci shortcode'u pymdownx.emoji — człony rozdziela MYŚLNIK
# („material-scale-balance"), nie ukośnik. Ze ukośnikiem shortcode nie zostaje
# rozpoznany i na stronie widać goły napis „:material/scale-balance:".
OPISY_DZIALOW = [
    ("Prawo autorskie, wizerunek w sieci, rozwój technologii i wiarygodność źródeł.",
     "material-scale-balance"),
    ("Instrukcje warunkowe, pętle i funkcje. Algorytmy NWD/NWW, ułamki, systemy liczbowe i szyfry.",
     "material-code-braces"),
    ("Modelowanie 3D, grafika rastrowa, dokumenty techniczne, arkusz kalkulacyjny i prezentacje.",
     "material-application-brackets"),
    ("Urządzenia peryferyjne, ich parametry i maszyny sterowane komputerowo.",
     "material-printer-3d"),
    ("Działanie Internetu, chmura, praca zespołowa, komunikacja, e-learning i szukanie pracy.",
     "material-lan-connect"),
]


def bez_ogonkow(s: str) -> str:
    # „ł" i „Ł" to osobne znaki Unicode, nie „l" ze znakiem łączącym — NFKD ich
    # nie rozłoży, więc trzeba je podmienić ręcznie, zanim zdejmiemy resztę
    # ogonków. Bez tego „pomysłów" dawało slug „pomys-ow".
    s = s.lower().replace("ł", "l")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def slug(tytul: str) -> str:
    """Adres tematu — pierwszy człon tytułu, przed słowem „czyli"."""
    glowa = re.split(r",\s*czyli\b", tytul)[0]
    s = bez_ogonkow(glowa)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:40].rstrip("-")


def main() -> None:
    rozklad = json.load(open("rozklad.json", encoding="utf-8"))
    plan = json.load(open("plan.json", encoding="utf-8"))

    plaski = [(d["tytul"], t) for d in plan for t in d["tematy"]]
    assert len(rozklad) == len(plaski) == 30, (len(rozklad), len(plaski))

    dzialy = []
    i = 0
    uzyte_slugi = set()
    for nr, d in enumerate(plan):
        tematy = []
        oceny = {k: [] for k in ("dop", "dst", "db", "bdb", "cel")}
        for t in d["tematy"]:
            lp = int(rozklad[i]["lp"])
            assert lp == i + 1, (lp, i)
            tytul = POPRAWKI.get(lp, rozklad[i]["temat"])
            m = ROZDZIAL.search(t["temat"])
            rozdzial = m.group(1) if m else str(lp)
            s = slug(tytul)
            assert s not in uzyte_slugi, s
            uzyte_slugi.add(s)
            tematy.append({
                "lp": lp,
                "tytul": tytul,
                "godziny": int(rozklad[i]["godz"]),
                "rozdzial": rozdzial,
                "slug": s,
                "oceny": t["oceny"],
            })
            for k in oceny:
                for punkt in t["oceny"][k]:
                    if punkt not in oceny[k]:
                        oceny[k].append(punkt)
            i += 1

        opis, ikona = OPISY_DZIALOW[nr]
        dzialy.append({
            "nr": RZYMSKIE[nr],
            "tytul": re.sub(r"^[IVX]+\.\s*", "", d["tytul"]),
            "slug": SLUGI_DZIALOW[nr],
            "opis": opis,
            "ikona": ikona,
            "godziny": sum(t["godziny"] for t in tematy),
            "tematy": tematy,
            "oceny": oceny,
        })

    razem = sum(d["godziny"] for d in dzialy)
    assert razem == 30, razem

    json.dump(dzialy, open("daneSB.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    with open("daneSB.js", "w", encoding="utf-8") as f:
        f.write("// Wymagania edukacyjne – informatyka, klasa 1W (branżowa szkoła I stopnia)\n")
        f.write("// Plik generowany przez budujdane.py z rozkladu materialu i planu wynikowego.\n")
        f.write("// Nie edytuj recznie – zmiany wprowadzaj w dokumentach zrodlowych.\n\n")
        f.write("module.exports.dzialy = ")
        f.write(json.dumps(dzialy, ensure_ascii=False, indent=2))
        f.write(";\n")

    print(f"działów: {len(dzialy)}, tematów: {sum(len(d['tematy']) for d in dzialy)}, godzin: {razem}")
    for d in dzialy:
        n = {k: len(v) for k, v in d["oceny"].items()}
        print(f"  {d['nr']:>3}. {d['godziny']:>2} h, {len(d['tematy']):>2} tematów, punkty {n}")


if __name__ == "__main__":
    main()
