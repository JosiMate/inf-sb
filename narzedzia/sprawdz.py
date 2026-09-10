#!/usr/bin/env python3
"""Kontrola: czy w wygenerowanych plikach jest dokładnie to, co w dokumentach.

Sprawdza trzy rzeczy, które łatwo zepsuć niezauważenie przy przebudowie:
  1. wszystkie 30 tematów rozkładu trafiło na stronę startową i do .docx,
  2. każdy punkt wymagań z planu wynikowego jest na stronie wymagań,
  3. suma godzin się zgadza i żaden temat nie zgubił numeru.

Uruchamiać po każdej zmianie budujdane.py, genstrony_sb.py albo gen1w.js.
"""
import json
import pathlib
import re
import subprocess
import sys
import zipfile

HERE = pathlib.Path(__file__).parent
DOCS = HERE.parent / "docs"

dzialy = json.load(open(HERE / "daneSB.json", encoding="utf-8"))
rozklad = json.load(open(HERE / "rozklad.json", encoding="utf-8"))
plan = json.load(open(HERE / "plan.json", encoding="utf-8"))

bledy = []


def sprawdz(warunek, opis):
    print(("  ✔ " if warunek else "  ✘ ") + opis)
    if not warunek:
        bledy.append(opis)


def tekst_docx(sciezka):
    """Goły tekst z document.xml — wystarczy do sprawdzenia, czy fraza jest."""
    with zipfile.ZipFile(sciezka) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = re.sub(r"</w:p>", "\n", xml)
    return re.sub(r"<[^>]+>", "", xml)


print("Dane scalone:")
sprawdz(sum(d["godziny"] for d in dzialy) == 30, "suma godzin = 30")
tematy = [t for d in dzialy for t in d["tematy"]]
sprawdz(len(tematy) == 30, "tematów = 30")
sprawdz([t["lp"] for t in tematy] == list(range(1, 31)),
        "numery tematów to 1…30 bez luk i powtórzeń")
sprawdz(len({t["slug"] for t in tematy}) == 30, "30 różnych adresów (slugów)")
sprawdz(len(rozklad) == 30 and sum(int(r["godz"]) for r in rozklad) == 30,
        "rozkład źródłowy: 30 pozycji po 1 godzinie")

print("\nStrona startowa (docs/index.md):")
index = (DOCS / "index.md").read_text(encoding="utf-8")
brak = [t["tytul"] for t in tematy if t["tytul"] not in index]
sprawdz(not brak, f"wszystkie tytuły tematów są na stronie{'' if not brak else ': brakuje ' + str(brak)}")
sprawdz(all(f'Dział {d["nr"]}. {d["tytul"]}' in index for d in dzialy),
        "wszystkie nazwy działów są na stronie")

print("\nStrona wymagań (docs/dzial-1/wymagania-i-bhp.md):")
wym = (DOCS / "dzial-1" / "wymagania-i-bhp.md").read_text(encoding="utf-8")
punkty = [p for d in plan for t in d["tematy"] for lst in t["oceny"].values() for p in lst]
brak = [p for p in punkty if p not in wym]
sprawdz(not brak, f"każdy punkt planu wynikowego jest na stronie "
                  f"({len(punkty)} punktów){'' if not brak else '; brakuje ' + str(brak[:3])}")
sprawdz("§ 30 ust. 5" in wym and "§ 35" in wym and "§ 28 ust. 2" in wym,
        "zapisy statutu (§ 28 ust. 2, § 30 ust. 5, § 35) są przywołane")
sprawdz("art. 44b ust. 10" in wym,
        "poprawa oceny oznaczona jako ustalenie przedmiotowe (art. 44b ust. 10)")

print("\nDokument .docx:")
docx = DOCS / "pliki" / "wymagania-edukacyjne-informatyka-1w.docx"
if docx.exists():
    tresc = tekst_docx(docx)
    brak = [t["tytul"] for t in tematy if t["tytul"] not in tresc]
    sprawdz(not brak, f"wszystkie tematy są w dokumencie{'' if not brak else ': brakuje ' + str(brak)}")
    brakp = [p for p in punkty if p not in tresc]
    sprawdz(not brakp, f"wszystkie punkty wymagań są w dokumencie"
                       f"{'' if not brakp else '; brakuje ' + str(brakp[:3])}")
    sprawdz("łącznie 30 godzin" in tresc, "nagłówek podaje 30 godzin")
else:
    sprawdz(False, f"brak pliku {docx}")

print("\nBudowanie strony (mkdocs build --strict):")
wynik = subprocess.run(["mkdocs", "build", "--strict"], cwd=HERE.parent,
                       capture_output=True, text=True)
sprawdz(wynik.returncode == 0, "mkdocs build --strict kończy się bez błędu")

print()
if bledy:
    print(f"NIEZGODNOŚCI: {len(bledy)}")
    sys.exit(1)
print("Wszystko się zgadza.")
