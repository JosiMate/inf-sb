/* Wspólny blok „ocenianie” dla wszystkich dokumentów wymagań edukacyjnych.
 *
 * Źródło: Statut PCEiKZ w Szczucinie, rozdział 15 (Wewnątrzszkolne Zasady Oceniania)
 *   § 26 ust. 1  – informacja o wymaganiach do 25 września, wraz z warunkami i trybem
 *                  uzyskania oceny wyższej niż przewidywana,
 *   § 28 ust. 2  – plusy i minusy przy ocenach bieżących (poza cel i ndst),
 *   § 30 ust. 2  – jeden sprawdzian godzinny dziennie, nie więcej niż trzy tygodniowo,
 *   § 30 ust. 3  – prace oddane i ocena uzasadniona w ciągu dwóch tygodni,
 *   § 30 ust. 5  – zaliczenie zapowiedzianej formy pisemnej po nieobecności: do 2 tygodni
 *                  od dnia powrotu do szkoły,
 *   § 35 ust. 2–13 – tryb odwołania od przewidywanej oceny rocznej,
 *   § 36         – dostosowanie wymagań przy specyficznych trudnościach w uczeniu się,
 *   § 37 ust. 2–3 – zwolnienie z informatyki decyzją dyrektora, wpis „zwolniony”,
 *   § 37 ust. 6  – laureaci i finaliści olimpiad przedmiotowych.
 *
 * Statut nie reguluje poprawiania ocen bieżących — te zasady są ustaleniem
 * przedmiotowym nauczyciela (art. 44b ust. 10 ustawy o systemie oświaty).
 */

/* opcje:
 *   formaD   – dopełniacz formy podlegającej poprawie, np. "sprawdzianu działowego"
 *   formaM   – mianownik tej samej formy, np. "sprawdzian działowy"
 *   formaB   – biernik, np. "sprawdzian działowy" / "pracę kontrolną"
 *   formaZ   – zaimek dla formy: "go" albo "ją"
 *   praktyczne – true, jeżeli przedmiot ma zadania praktyczne przy komputerze
 *   olimpiada  – nazwa olimpiady w dopełniaczu (domyślnie "olimpiady przedmiotowej")
 *   zwolnienie – true dla informatyki (§ 37 ust. 2–3 wymienia ją wprost)
 *   extraZaleglosci / extraDostosowania – dodatkowe punkty przedmiotowe
 */
function sekcje(o) {
  const formaD = o.formaD || "sprawdzianu";
  const formaM = o.formaM || "sprawdzian";
  const formaZ = o.formaZ || "go";
  const praktyczne = o.praktyczne !== false;
  const grupy = [];

  grupy.push({
    tytul: "Ocenianie bieżące:",
    punkty: [
      "oceny bieżące ustala się w skali od 1 do 6; przy ocenach bieżących stosuje się znaki „+” i „−”, z wyjątkiem oceny celującej i niedostatecznej (§ 28 ust. 2 statutu);",
      "w ciągu jednego dnia uczeń może mieć tylko jeden godzinny sprawdzian, a w ciągu tygodnia nie więcej niż trzy (§ 30 ust. 2 statutu);",
      "poprawione i ocenione prace pisemne nauczyciel przekazuje uczniom do wglądu podczas lekcji i uzasadnia ocenę w ciągu dwóch tygodni od napisania pracy (§ 30 ust. 3 statutu);",
      "prace pisemne nauczyciel przechowuje do końca roku szkolnego i udostępnia rodzicom do wglądu podczas spotkania w szkole (§ 30 ust. 3–4 statutu)."
    ]
  });

  const zal = [
    `uczeń, który nie zgłosił się na zapowiedzianą pisemną formę kontroli wiadomości, uzupełnia brakującą ocenę w formie i terminie wyznaczonych przez nauczyciela, nie później niż 2 tygodnie od dnia powrotu do szkoły (§ 30 ust. 5 statutu);`
  ];
  if (praktyczne) zal.push("niewykonane zadanie praktyczne uczeń uzupełnia na najbliższych zajęciach albo w terminie konsultacji;");
  (o.extraZaleglosci || []).forEach(t => zal.push(t));
  zal.push("zaliczenie zaległości jest obowiązkiem ucznia i nie jest tym samym co dobrowolna poprawa oceny opisana poniżej.");
  grupy.push({ tytul: "Zaliczanie zaległości (zapis statutu):", punkty: zal });

  grupy.push({
    tytul: "Poprawa oceny — ustalenie przedmiotowe:",
    wstep: "Statut PCEiKZ nie reguluje poprawiania ocen bieżących. Poniższe zasady są ustaleniem nauczyciela przedmiotu, przyjętym na podstawie art. 44b ust. 10 ustawy o systemie oświaty, jednakowym dla wszystkich uczniów w klasie i podanym do wiadomości do 25 września.",
    punkty: [
      `poprawie podlegają oceny z prac obejmujących cały dział (${formaM}); pozostałe oceny bieżące — kartkówki, odpowiedzi, zadania praktyczne, aktywność — nie podlegają poprawie, a wpływ na ocenę okresową ma ich systematyczność;`,
      "poprawa jest dobrowolna i przysługuje jeden raz do każdej oceny;",
      `poprawę pisze się w terminie dwóch tygodni od otrzymania ocenionej pracy, w dniu i formie uzgodnionych z nauczycielem — w miarę możliwości poza lekcją, na konsultacjach;`,
      "poprawa obejmuje ten sam zakres materiału i ma porównywalny stopień trudności jak praca oceniona pierwotnie;",
      "w dzienniku pozostają obie oceny — pierwsza i z poprawy; przy ustalaniu oceny śródrocznej i rocznej brana jest pod uwagę ocena wyższa, więc przystąpienie do poprawy nigdy nie pogarsza sytuacji ucznia;",
      "uczeń, który nie stawi się w uzgodnionym terminie bez usprawiedliwienia, traci prawo do poprawy tej oceny."
    ]
  });

  grupy.push({
    tytul: "Warunki i tryb uzyskania oceny rocznej wyższej niż przewidywana (§ 35 statutu):",
    punkty: [
      "o przewidywanej rocznej ocenie klasyfikacyjnej uczeń i rodzice są informowani na tydzień przed klasyfikacyjnym posiedzeniem rady pedagogicznej — wpisem do dziennika elektronicznego (§ 35 ust. 2–4 statutu);",
      "uczeń ma prawo odwołać się od przewidywanej oceny rocznej najpóźniej na 5 dni przed rocznym klasyfikacyjnym zebraniem rady pedagogicznej, składając na piśmie do Dyrektora PCEiKZ wniosek o sprawdzenie jego wiadomości (§ 35 ust. 7 statutu);",
      "podwyższenie oceny następuje na podstawie sprawdzianu w formie ustnej, pisemnej, praktycznej lub łączonej, obejmującego wymagania niezbędne do uzyskania oceny, o jaką uczeń się ubiega (§ 35 ust. 9 statutu); z tego przedmiotu sprawdzian ma formę praktyczną albo łączoną i obejmuje wymagania z całego roku na wnioskowaną ocenę, wypisane w rozdziale 3 niniejszego dokumentu;",
      "sprawdzian przeprowadza się nie później niż na 3 dni przed rocznym klasyfikacyjnym posiedzeniem rady pedagogicznej (§ 35 ust. 11 statutu);",
      "jeżeli uczeń nie wykaże się spełnieniem wymagań na ocenę, o którą się ubiega, otrzymuje ocenę przewidywaną (§ 35 ust. 10 statutu); z przebiegu sprawdzianu nauczyciel sporządza protokół przekazywany Dyrektorowi (§ 35 ust. 12–13 statutu)."
    ]
  });

  const dost = [
    "przy ocenianiu uwzględnia się zalecenia zawarte w opiniach i orzeczeniach poradni psychologiczno-pedagogicznej; wymagania dostosowuje się do możliwości psychofizycznych ucznia, zachowując wymagania konieczne (§ 36 statutu);"
  ];
  if (o.zwolnienie !== false) {
    dost.push("w uzasadnionych przypadkach uczeń może zostać zwolniony z zajęć na czas określony decyzją Dyrektora PCEiKZ, na podstawie opinii lekarza; jeżeli okres zwolnienia uniemożliwia ustalenie oceny, w dokumentacji wpisuje się „zwolniony” (§ 37 ust. 2–3 statutu);");
  }
  if (praktyczne) dost.push("uczeń, który czasowo nie może pracować przy komputerze, wykonuje zadania w formie zastępczej ustalonej z nauczycielem;");
  (o.extraDostosowania || []).forEach(t => dost.push(t));
  dost.push(`laureaci i finaliści ${o.olimpiada || "olimpiady przedmiotowej"} otrzymują celującą roczną ocenę klasyfikacyjną (§ 37 ust. 6 statutu).`);
  grupy.push({ tytul: "Dostosowania i sytuacje szczególne:", punkty: dost });

  return grupy;
}

const stopka = "Niniejsze wymagania edukacyjne, sposoby sprawdzania osiągnięć oraz warunki i tryb uzyskania oceny wyższej niż przewidywana zostały podane uczniom i rodzicom do wiadomości do 25 września, zgodnie z § 26 ust. 1 statutu PCEiKZ.";

module.exports = { sekcje, stopka };
