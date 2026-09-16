# Warunki, pętle, funkcje, czyli podstawy języków programowania

**Informatyka · klasa 1W · branżowa szkoła I stopnia · 1 godzina · rozdział 5**

Wyobraź sobie, że program komputerowy to bardzo dokładna instrukcja dla kogoś, kto nie ma własnej intuicji i rozumie tylko polecenia typu „zrób to” albo „jeśli stanie się X, zrób Y”. Jeśli pominiesz jeden krok albo pomylisz kolejność, komputer nie „domyśli się”, o co Ci chodziło — po prostu zrobi dokładnie to, co napisałeś, nawet jeśli skończy się to błędem. Ta lekcja jest o tym, jak pisać takie instrukcje, żeby komputer nas rozumiał.

!!! success "Cele lekcji"

    Po tej lekcji potrafisz:

    1. zdefiniować pojęcia: kod programu, interpreter, kompilator i debugger
    2. wymienić kolejne etapy powstawania programu komputerowego
    3. założyć konto w serwisie Scratch i odnaleźć się w jego interfejsie
    4. wyjaśnić, czym są zmienne i jak tworzyć je w Scratch
    5. używać instrukcji wejścia i wyjścia danych
    6. odróżnić pętlę od instrukcji warunkowej i zastosować je w programie
    7. korzystać z operatorów logicznych i matematycznych do budowania warunków

## 1. Od pomysłu do działającego programu

Zanim programista usiądzie do klawiatury, musi przejść przez proces, który chroni go przed pisaniem kodu „na oślep”.

### Etapy powstawania programu
1. **Analiza problemu** — dokładnie określamy, co program ma robić (co jest wejściem, a co wynikiem).
2. **Opracowanie algorytmu** — tworzymy plan działania (np. schemat blokowy lub listę kroków), zanim napiszemy kod.
3. **Kodowanie** — zapisujemy algorytm w konkretnym języku programowania.
4. **Testowanie i poprawianie (debugowanie)** — uruchamiamy program z różnymi danymi, szukamy błędów i je naprawiamy.
5. **Dokumentacja** — opisujemy, jak działa program, żeby inni (lub my sami za miesiąc) wiedzieli, jak go używać.

### Język maszynowy a języki wysokiego poziomu
Komputer rozumie tylko prąd (włączony/wyłączony), czyli zera i jedynki (**język maszynowy**). Ludzie piszą w językach bardziej zrozumiałych (np. Python, C++, Java), które nazywamy **językami wysokiego poziomu**. Żeby komputer mógł je wykonać, potrzebny jest „tłumacz”.

| Pojęcie | Co to jest? | Jak działa? | Przykład |
| --- | --- | --- | --- |
| **Kod programu** | Tekst napisany w języku programowania | Zbiór instrukcji, które komputer ma wykonać | Plik `.py` w Pythonie |
| **Kompilator** | Tłumacz „całościowy” | Tłumaczy cały kod na język maszynowy raz, tworząc plik wykonywalny (np. `.exe`) | C++, Rust |
| **Interpreter** | Tłumacz „na bieżąco” | Czyta kod linijka po linijce i od razu go wykonuje | Python, JavaScript, Scratch |
| **Debugger** | Narzędzie do szukania błędów | Pozwala zatrzymać program w dowolnym miejscu i sprawdzić, co dzieje się w zmiennych | Narzędzia wbudowane w IDE |

!!! tip "Dlaczego debugger jest ważny?"
    Szukanie błędów (tzw. **debugowanie**) to 80% pracy programisty. Debugger pozwala nam „wejść do głowy” komputera i zobaczyć, dlaczego zmienna, która powinna mieć wartość 10, nagle stała się liczbą -1.

## 2. Scratch — Twoje pierwsze środowisko

**Scratch** to język programowania wizualnego. Zamiast wpisywać komendy z klawiatury (gdzie jeden brakujący średnik może zepsuć cały program), układasz **bloki** jak klocki LEGO. To idealny sposób, żeby nauczyć się *logiki* programowania bez walki z błędami w pisowni.

### Pierwsze kroki
1. Wejdź na stronę [scratch.mit.edu](https://scratch.mit.edu).
2. Załóż konto (pozwoli Ci to zapisywać projekty i dzielić się nimi z innymi).
3. Kliknij **Twórz**, aby otworzyć edytor.

### Interfejs w pigułce
- **Scena** — miejsce, gdzie dzieje się akcja. Tu widzisz swojego duszka (spritę).
- **Paleta bloków** — menu z wszystkimi dostępnymi rozkazami, podzielonymi na kategorie (Ruch, Wygląd, Dźwięk, Zdarzenia itd.).
- **Obszar skryptów** — miejsce, w którym przeciągasz i łączysz bloki, budując swój program.

## 3. Zmienne i dane

W programie często musimy coś zapamiętać: wynik mnożenia, imię gracza albo liczbę zebranych punktów. Do tego służą **zmienne**.

**Zmienna** to taki „nazwany pojemnik” w pamięci komputera, do którego możemy włożyć jakąś wartość, a potem ją wyciągnąć lub zmienić.

### Zmienne w Scratch
Aby stworzyć zmienną, przejdź do kategorii **Zmienne** i kliknij **Stwórz zmienną**. Nadaj jej nazwę (np. `wynik` lub `liczba_punktow`).
- **Ustawienie wartości**: blok `ustaw [zmienna] na [wartość]`.
- **Zmiana wartości**: blok `zmień [zmienna] o [wartość]` (np. o 1, żeby dodać punkt).

### Komunikacja z użytkownikiem
Program, który tylko liczy w pamięci, jest bezużyteczny. Musi umieć rozmawiać z człowiekiem:

- **Wyjście danych** — przekazywanie informacji z programu do użytkownika.
  - W Scratch: blok `powiedz [tekst] przez [2] sekundy`.
- **Wejście danych** — pobieranie informacji od użytkownika.
  - W Scratch: blok `zapytaj [tekst] i czekaj`. Wpisana odpowiedź zostaje automatycznie zapisana w specjalnym bloku `odpowiedź`.

!!! example "Prosty program: Powitanie"
    Złóż bloki w tej kolejności:
    1. `Kiedy kliknięto zieloną flagę`
    2. `zapytaj [Jak masz na imię?] i czekaj`
    3. `powiedz (połącz [Cześć ] i (odpowiedź)) przez [2] sekundy`

## 4. Sterowanie programem: Warunki, Pętle, Operatory

To jest „serce” programowania. Dzięki tym konstrukcjom program przestaje być prostą listą kroków, a zaczyna „myśleć” i reagować na sytuację.

### Instrukcje warunkowe (Decyzje)
Pozwalają programowi wybrać jedną z kilku dróg. Jeśli warunek jest spełniony (prawda), wykonaj instrukcję. Jeśli nie — pomiń ją lub zrób coś innego.

- **Blok `jeżeli <warunek> to`** — wykonuje kod tylko wtedy, gdy warunek jest prawdziwy.
- **Blok `jeżeli <warunek> to ... w przeciwnym razie ...`** — zawsze coś zrobi. Jeśli warunek jest prawdą, robi jedną rzecz; jeśli fałszem — drugą.

### Pętle (Powtarzanie)
Służą do wykonywania tej samej czynności wiele razy, bez konieczności kopiowania tych samych bloków.

- **`powtórz [10] razy`** — wiemy dokładnie, ile razy coś ma się stać.
- **`zawsze`** — pętla nieskończona (np. sprawdzanie, czy gracz nacisnął klawisz strzałki).
- **`powtarzaj aż <warunek>`** — pętla działa tak długo, aż warunek stanie się prawdziwy (np. powtarzaj ruch, aż duszek dotknie krawędzi ekranu).

### Operatory (Sądownictwo)
Aby warunki działały, program musi umieć porównywać wartości. Do tego służą operatory z zielonej kategorii.

| Typ operatora | Przykłady | Zastosowanie |
| --- | --- | --- |
| **Matematyczne** | `+`, `-`, `*`, `/`, `modulo` | Obliczenia, np. `wynik = liczba1 + liczba2` |
| **Porównania** | `=`, `<`, `>` | Sprawdzanie, czy np. `punkty > 100` |
| **Logiczne** | `i`, `lub`, `nie` | Łączenie warunków, np. `(wiek > 12) i (ma_bilet = tak)` |

!!! warning "Pętla vs Warunek — nie pomyl ich!"
    - **Warunek** (`jeżeli`) pyta: „Czy mam to teraz zrobić?”. Jeśli nie — pomija to raz i idzie dalej.
    - **Pętla** (`powtórz`) mówi: „Rób to tak długo, aż powiem stop”. Jeśli warunek nie jest spełniony, wraca na początek i próbuje znowu.

## Sprawdź się

<div class="quiz" markdown="0">
<script type="application/json">
[
  {
    "pytanie": "Które z poniższych narzędzi służy do szukania błędów w kodzie i sprawdzania wartości zmiennych w trakcie działania programu?",
    "opcje": [
      "Kompilator",
      "Interpreter",
      "Debugger",
      "Edytor tekstu"
    ],
    "poprawna": 2,
    "wyjasnienie": "Debugger to narzędzie, które pozwala zatrzymać program w dowolnym momencie i przeanalizować jego stan."
  },
  {
    "pytanie": "Jaka jest główna różnica między kompilatorem a interpreterem?",
    "opcje": [
      "Kompilator tłumaczy kod linijka po linijce, interpreter cały naraz",
      "Kompilator tworzy plik wykonywalny przed uruchomieniem, interpreter tłumaczy kod w czasie rzeczywistym",
      "Interpreter jest szybszy w działaniu niż skompilowany program",
      "Kompilator jest używany tylko w Scratchu"
    ],
    "poprawna": 1,
    "wyjasnienie": "Kompilator przetwarza cały kod przed uruchomieniem (tworząc np. plik .exe), natomiast interpreter tłumaczy i wykonuje instrukcje jedna po drugiej."
  },
  {
    "pytanie": "Co w programowaniu jest 'pojemnikiem' na dane, których wartość może się zmieniać w czasie działania programu?",
    "opcje": [
      "Operatorem",
      "Zmienną",
      "Pętlą",
      "Funkcją"
    ],
    "poprawna": 1,
    "wyjasnienie": "Zmienna to obszar w pamięci komputera, który przechowuje wartość przypisaną pod konkretną nazwą."
  },
  {
    "pytanie": "Chcesz, aby Twój program w Scratchu pytał użytkownika o imię i wyświetlał je na ekranie. Jakich bloków użyjesz?",
    "opcje": [
      "bloczków 'powiedz' i 'powtórz'",
      "bloczków 'zapytaj i czekaj' oraz 'powiedz'",
      "bloczków 'jeżeli' oraz 'zawsze'",
      "tylko bloczków z kategorii 'Ruch'"
    ],
    "poprawna": 1,
    "wyjasnienie": "Blok 'zapytaj' służy do wejścia danych (input), a blok 'powiedz' do ich wyjścia (output)."
  },
  {
    "pytanie": "Która konstrukcja jest odpowiednia, gdy chcesz, aby postać w grze poruszała się do momentu, aż dotknie ściany?",
    "opcje": [
      "Instrukcja 'jeżeli ... to'",
      "Pętla 'powtórz 10 razy'",
      "Pętla 'powtarzaj aż <dotyka ściany>'",
      "Operator logiczny 'lub'"
    ],
    "poprawna": 2,
    "wyjasnienie": "Pętla 'powtarzaj aż' wykonuje instrukcje tak długo, dopóki określony warunek nie stanie się prawdziwy."
  },
  {
    "pytanie": "Kiedy używamy operatora logicznego 'i' (AND)?",
    "opcje": [
      "Gdy chcemy, aby program wykonał czynność, jeśli przynajmniej jeden z dwóch warunków jest prawdziwy",
      "Gdy chcemy, aby program wykonał czynność tylko wtedy, gdy oba warunki są jednocześnie prawdziwe",
      "Gdy chcemy zaprzeczyć istniejącemu warunkowi",
      "Gdy chcemy dodać dwie liczby do siebie"
    ],
    "poprawna": 1,
    "wyjasnienie": "Operator 'i' wymaga, aby wszystkie połączone warunki były prawdziwe, aby cały wynik był prawdą."
  }
]
</script>
</div>

---

*Stan wiedzy: Wrzesień 2026 r. Przykłady oparte na środowisku Scratch 3.0.*
