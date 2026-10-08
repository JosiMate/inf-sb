import glob, re

files = sorted(glob.glob("docs/dzial-*/*.md"))

verb_map = {
    "wskazać": "wskażę",
    "powiedzieć": "powiem",
    "wyjaśnić": "wyjaśnię",
    "opisać": "opiszę",
    "wymienić": "wymienię",
    "wykonać": "wykonam",
    "stosować": "zastosuję",
    "użyć": "użyję",
    "zrobić": "zrobię",
    "sprawdzić": "sprawdzę",
    "dobrać": "dobiorę",
    "sklasyfikować": "sklasyfikuję",
    "porównać": "porównam",
    "zidentyfikować": "zidentyfikuję",
    "odróżnić": "odróżnię",
    "rozróżniać": "rozróżnię",
    "znaleźć": "znajdę",
    "przeanalizować": "przeanalizuję",
    "korygować": "skoryguję",
    "usunąć": "usunę",
    "kadrować": "skadruję",
    "uruchomić": "uruchomię",
    "importować": "zaimportuję",
    "eksportować": "wyeksportuję",
    "utworzyć": "utworzę",
    "zamienić": "zamienię",
    "połączyć": "połączę",
    "modyfikować": "zmodyfikuję",
    "podzielić": "podzielę",
    "dostosować": "dostosuję",
    "nakładać": "nałożę",
    "przeszukiwać": "przeszukam",
    "wczytywać": "wczytam",
    "przygotować": "przygotuję",
    "określić": "określę",
    "zabezpieczyć": "zabezpieczę",
    "zgłosić": "zgłosić",
    "napisać": "napiszę",
    "rozpisać": "rozpiszę",
    "przeliczyć": "przeliczę",
    "szyfrować": "zaszyfruję",
    "odszyfrować": "odszyfruję",
    "skonfigurować": "skonfiguruję",
    "przeprowadzić": "przeprowadzę",
    "charakteryzować": "scharakteryzuję",
    "oceniać": "ocenię",
    "ocenić": "ocenię",
    "oszacować": "oszacuję",
    "wyliczyć": "wyliczę",
    "wyszukać": "wyszukam",
    "pobrać": "pobiorę",
    "zainstalować": "zainstaluję",
    "uruchamiać": "uruchomię",
    "wymieniać": "wymienię",
    "pakować": "spakuję",
    "wysyłać": "wyślę",
    "synchronizować": "zsynchronizuję",
    "tworzyć": "utworzę",
    "edytować": "edytuję",
    "zorganizować": "zorganizuję",
    "zaplanować": "zaplanuję",
    "zarządzać": "zarządzę",
    "opracować": "opracuję",
    "wybierać": "wybiorę",
    "czyścić": "oczyszczę",
    "konwertować": "skonwertuję",
    "obliczać": "obliczę",
    "przeliczać": "przeliczę",
    "skorygować": "skoryguję",
    "regulować": "skoryguję",
    "układać": "ułożę",
    "pisać": "napiszę",
    "identyfikować": "zidentyfikuję",
    "odróżniać": "odróżnię",
    "cyfryzować": "scyfryzuję",
    "przygotowywać": "przygotuję",
    "interpretować": "zinterpretuję",
    "analizować": "przeanalizuję",
    "przydzielać": "przydzielę",
    "zsynchronizować": "zsynchronizuję",
    "pobierać": "pobiorę",
    "korzystać": "skorzystam",
    "weryfikować": "zweryfikuję",
    "dbać": "zadbam",
    "umieszczać": "umieszczę",
    "budować": "zbuduję",
    "diagnozować": "sdiagnozuję",
    "nawiązywać": "nawiążę",
    "przesyłać": "prześlę",
    "chronić": "ochronię",
    "organizować": "zorganizuję",
    "podpisywać": "podpiszę",
    "prowadzić": "przeprowadzę",
    "wyjaśniać": "wyjaśnię",
    "edytować": "edytuję",
    "udostępniać": "udostępnię",
    "przenosić": "przeniosę",
    "dostosowywać": "dostosuję",
    "wyciągać": "wyciągnę",
    "skalować": "skaluję",
    "obracać": "obrócę",
    "wycinać": "wyetnę",
    "dodawać": "dodam",
    "prostować": "sprostuję",
    "usuwać": "usunę",
    "instalować": "zainstaluję",
    "konfigurować": "skonfiguruję"
}

for filepath in files:
    if filepath.endswith("index.md") or "wymagania-i-bhp" in filepath:
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    def fix_criteria_block(match):
        block = match.group(0)
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            m = re.match(r'^(\s*\d+\.\s*)(.*)$', line)
            if m and not line.strip().startswith("Po tej lekcji"):
                prefix = m.group(1)
                text = m.group(2)

                # Replace any remaining infinitives in text with first person form
                words = text.split(" ")
                new_words = []
                for idx, w in enumerate(words):
                    clean_w = w.strip(".,;:()").lower()
                    if clean_w in verb_map:
                        replacement = verb_map[clean_w]
                        if idx == 0:
                            replacement = replacement.capitalize()
                        # preserve punctuation
                        prefix_punc = w[:len(w)-len(w.lstrip(".,;:()"))]
                        suffix_punc = w[len(w.rstrip(".,;:()")):]
                        new_words.append(prefix_punc + replacement + suffix_punc)
                    else:
                        new_words.append(w)
                new_line = prefix + " ".join(new_words)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        return "\n".join(new_lines)

    content = re.sub(r'!!! success "Kryteria sukcesu".*?(?=\n\n\S|\n\n\?\?\?|\n\n##)', fix_criteria_block, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Grammar in criteria fixed.")
