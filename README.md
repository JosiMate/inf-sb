# inf-sb — informatyka, klasa 1W

Materiały do informatyki w branżowej szkole I stopnia (PCEiKZ Szczucin).
Strona: <https://josimate.github.io/inf-sb/>

## Co jest w repozytorium

| Katalog | Zawartość |
| --- | --- |
| `docs/` | treść strony (Markdown, style, pliki do pobrania) |
| `narzedzia/` | generatory i dokumenty źródłowe — patrz niżej |
| `.github/workflows/deploy.yml` | publikacja na GitHub Pages przy każdym pushu na `main` |

## Jak to się generuje

Strony i dokument wymagań **nie są pisane ręcznie** — powstają z dwóch
dokumentów nauczyciela leżących w `narzedzia/`:

* `rozklad_1W.docx` — rozkład materiału (30 tematów po 1 godzinie),
* `plan_wynikowy.docx` — wymagania na pięć poziomów ocen.

Kolejność uruchamiania:

```bash
cd narzedzia
python3 budujdane.py       # scala oba dokumenty → daneSB.json + daneSB.js
node    gen1w.js           # → dokument .docx z wymaganiami
python3 genstrony_sb.py    # → docs/index.md i docs/dzial-1/wymagania-i-bhp.md
python3 sprawdz.py         # kontrola zgodności + mkdocs build --strict
```

`gen1w.js` potrzebuje pakietu `docx` (npm), reszta tylko Pythona.
Blok o ocenianiu (`wzo.js` dla .docx, `wzo_md.py` dla stron) jest wspólny
z pozostałymi przedmiotami — zapisy statutu brzmią wszędzie tak samo.

## Podgląd lokalny

```bash
pip install -r requirements.txt
mkdocs serve
```

## Publikacja

Push na `main` uruchamia workflow. Warunek: w **Settings → Pages**
źródłem musi być **GitHub Actions** (nie gałąź).
