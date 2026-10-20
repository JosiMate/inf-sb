# Zadanie dla Julesa — poprawki po PR #3 („bring all lesson topics up to AGENTS.md standard”)

Skopiuj wszystko poniżej linii i wklej do Julesa
(repozytorium `JosiMate/inf-sb`, gałąź `main`).

---

Przeczytaj `AGENTS.md` i postępuj według niego — szczególnie według sekcji 5
„Standard tematu” (kolejność elementów, układ rozgrzewki, kryteria sukcesu)
i sekcji 6 „Widżety i składnia”.

## Kontekst

W PR #3 dostosowałeś 29 tematów w `docs/dzial-1` … `docs/dzial-5` do
standardu. Strona się buduje, ale sprawdzenie wyrenderowanego HTML-a pokazało
błędy, a części zmian zapowiedzianych w opisie PR nie ma. Popraw je w **dwóch
osobnych commitach**: najpierw etap A (techniczny), potem etap B (treść).
Wszystko w jednym PR.

Pliki pomocnicze i skrypty sprawdzające trzymaj w `/tmp/` — **nic poza
`docs/` nie może się zmienić**, z wyjątkiem usunięcia plików z punktu A5.

## Etap A — poprawki techniczne (wszystkie 29 tematów)

**A1. Kryteria sukcesu nie są listą.** We wszystkich 29 tematach po wierszu
„Po tej lekcji:” brakuje pustego wiersza, więc Markdown skleja punkty w jeden
akapit („Po tej lekcji: 1. … 2. … 3. …”). Przez to skrypt
`docs/assets/js/samoocena.js` (strona „Mój postęp”) nie znajduje punktów
kryteriów — szuka `ol > li` w ramce „Kryteria sukcesu”. Dodaj pusty wiersz
między „Po tej lekcji:” a punktem 1. Każdy punkt zakończ kropką.

**A2. Rozgrzewka stoi pod kryteriami.** Standard (AGENTS.md, sekcja 5) każe:
tytuł → „O tym temacie” → **rozgrzewka** → **kryteria sukcesu** → treść.
Przenieś cały blok `??? rozgrzewka …` (razem z zagnieżdżonymi odpowiedziami)
nad ramkę `!!! success "Kryteria sukcesu"` we wszystkich 29 tematach.

**A3. Ramka „O tym temacie” urywa się w trzech tematach działu I:**
`kim-jestem.md`, `rozwoj-technologii.md`, `wiedza-w-sieci.md`. Wciąłeś
4 spacjami tylko pierwszy wiersz akapitu wprowadzającego — reszta akapitu
wypada pod ramkę. Wetnij cały akapit. Usuń też zbędne puste wiersze, które
zostały pod ramką „O tym temacie” w innych tematach (2–3 puste wiersze
z rzędu).

**A4. Bezokoliczniki w kryteriach.** Skrypt ze słownikiem czasowników
zostawił 34 punkty w 19 plikach w bezokoliczniku albo z pomieszanymi formami,
np. „Wstawiać i edytuję nagłówki…”, „Zakładać konto i skorzystam…”,
„Uzasadnić, dlaczego…”. Każdy punkt ma być w pierwszej osobie czasu
przyszłego, **wszystkie czasowniki w punkcie**: „Wstawię i zmodyfikuję…”,
„Założę konto i skorzystam…”, „Uzasadnię…”. Popraw ręcznie, czytając zdanie —
nie skryptem. Sens punktu ma zostać ten sam.

**A5. Usuń z korzenia repozytorium swoje skrypty robocze:**
`fix_grammar_criteria.py`, `fix_predictions.py`, `fix_warmup_indent.py`.

**Sprawdzenie etapu A** — skrypt w `/tmp/`, nie w repozytorium. Po
`mkdocs build --strict` dla każdego z 29 tematów w `site/…/index.html`:

- ramka z tytułem „Kryteria sukcesu” zawiera `<ol>` z 4–7 elementami `<li>`;
- `<details class="rozgrzewka">` stoi w kodzie **przed** ramką „Kryteria
  sukcesu”, ma w środku `<ol>` z trzema pytaniami i zagnieżdżone
  `<details class="success">` z odpowiedziami;
- w ramce `admonition abstract` jest cały akapit wprowadzający, a zaraz za
  ramką nie stoi `<p>` z dalszym ciągiem zdania;
- żaden punkt kryteriów nie zawiera czasownika zakończonego na `-ć`
  (sprawdź wyrażeniem regularnym `\b\w+ć\b` i przejrzyj trafienia ręcznie).

Wynik sprawdzenia (tabela: plik, ok/błąd) wklej do opisu PR.

## Etap B — treść (rozgrzewki, „Przewiduj”, podpowiedzi)

**B1. Rozgrzewki — ułóż od nowa we wszystkich 29 tematach.** Obecne mają dwa
błędy:

1. Zwykle wszystkie trzy pytania dotyczą poprzedniej lekcji. Ma być: pytanie 1
   — poprzedni temat, pytanie 2 — temat sprzed kilku tygodni (3–6 tematów
   wstecz), pytanie 3 — dawniejszy (wcześniejszy dział). Kolejność tematów
   odczytasz z plików `.nav.yml` w kolejnych działach.
2. Część pytań dotyczy rzeczy, których **nie ma** w żadnym wcześniejszym
   temacie — pojęcie występuje tylko w samej rozgrzewce. Przykłady: przelew
   Elixir, wzorzec slajdów (Slide Master), IMAP, kanał alfa, twarda spacja,
   SUMA.JEŻELI, MOOC, kopia 3-2-1, narzędzie stempel.

Zasady:

- **Każde pytanie musi dotyczyć treści, która stoi na stronie wskazanego
  tematu.** Odpowiedź ma się dać znaleźć w tym pliku. W opisie PR przy każdym
  pytaniu podaj plik i sekcję, z której pochodzi (np. `wiedza-w-sieci.md, §2`).
- Pytania krótkie, z jednoznaczną odpowiedzią (liczba, nazwa, jedno zdanie).
  Dobre pytanie przygotowuje dzisiejszy temat — odpowiedź może kończyć się
  zdaniem „Dziś do tego wrócimy”.
- Dla pierwszych tematów roku, gdy nie ma jeszcze tematu „sprzed kilku
  tygodni” ani „dawniejszego”: pytanie 2 ze strony „Wymagania edukacyjne
  i bhp”, pytanie 3 z wiedzy ze szkoły podstawowej — wtedy pytanie ma być
  bardzo podstawowe (np. „Ile bitów ma bajt?”), bez faktów, których nie da się
  sprawdzić w repozytorium.
- Nagłówki pytań bez zmian: **Z poprzedniej lekcji.**, **Sprzed kilku
  tygodni.**, **Z dawniejszych tematów.**

**B2. „Przewiduj, potem sprawdź wynik” — dodaj w każdym temacie 1–2 ramki.**
W PR #3 nie dodałeś ani jednej (skrypt `fix_predictions.py` niczego nie
zmieniał). Składnia — AGENTS.md, sekcja 6. Wybieraj miejsca, gdzie strona
już podaje wynik albo odpowiedź:

- dział II (NWD i NWW, ułamki, systemy liczbowe, szyfrowanie, Python) —
  obliczenie, zamiana liczby, szyfrogram albo wynik krótkiego programu;
  **wynik policz programem** (Python 3) i przepisz z uruchomienia;
- arkusz (dział III) — wynik formuły w polskiej wersji, separator `;`;
  sprawdź w LibreOffice Calc, jeśli jest w środowisku, a jeśli nie — wypisz
  ten wynik w części „Do sprawdzenia” opisu PR;
- tematy bez obliczeń — pytanie z sytuacji z życia, odpowiedź schowana
  w `??? success "Przewiduj, potem sprawdź wynik"`.

Wynik, który teraz stoi na widoku zaraz po przykładzie, **przenieś** do
zwiniętej ramki — nie dubluj go.

**B3. Trzy podpowiedzi pod trudniejszymi ćwiczeniami.** W działach III–V
ćwiczenia są zwykłą listą numerowaną („1. **Ćwiczenie 1 (Podstawowe):** …”).
Podpowiedzi muszą stać pod ćwiczeniem, więc:

- zamień listę na ramki `!!! note "Ćwiczenie N. Krótki tytuł"` — **ta sama
  numeracja i ta sama treść polecenia**, poziom („Podstawowe”,
  „Zaawansowane”…) zostaw w treści ramki;
- pod najtrudniejszym ćwiczeniem w temacie (zwykle ostatnim, „Zaawansowane”
  albo „Branżowe”) dodaj trzy podpowiedzi `??? tip "Podpowiedź 1"`, 2, 3
  wcięte razem z ćwiczeniem: kierunek → konkretne narzędzie lub polecenie
  menu → prawie gotowe rozwiązanie;
- w działach I i II, gdzie ćwiczenia mają już postać ramek albo ich nie ma,
  dodaj podpowiedzi tylko pod istniejącymi ćwiczeniami.

Nazwy poleceń menu i narzędzi podawaj tylko te, które są na stronie tematu
albo w dokumentacji programu, którego temat dotyczy. Jeśli nie masz pewności
co do nazwy w polskiej wersji programu, opisz czynność słowami i wypisz to
miejsce w „Do sprawdzenia”.

## Czego nie zmieniać

- reszty treści tematów, numeracji ćwiczeń, quizów;
- plików kart pracy (`docs/assets/karty/*.json`) i `id` ich pól;
- tekstów wierszy w spisach tematów (`docs/dzial-N/index.md`, `docs/index.md`);
- `docs/assets/js/`, `mkdocs.yml`, `narzedzia/`.

## Zanim otworzysz PR

1. `mkdocs build --strict` — bez ostrzeżeń.
2. Sprawdzenie z etapu A dla wszystkich 29 tematów — same „ok”.
3. Każda tablica quizu nadal jest poprawnym JSON-em.
4. `git status`: zmienione tylko pliki w `docs/dzial-*/` i usunięte trzy
   skrypty `fix_*.py`; żadnych nowych plików poza `docs/`.
5. Opis PR po polsku:
   - co zrobiłeś w etapie A i B;
   - tabela sprawdzenia z etapu A;
   - przy każdej rozgrzewce — źródła pytań (plik i sekcja);
   - „Do sprawdzenia” — wyniki formuł i nazwy poleceń menu, których nie
     sprawdziłeś w programie;
   - lista kontrolna standardu z AGENTS.md (sekcja 8), odhaczona.
