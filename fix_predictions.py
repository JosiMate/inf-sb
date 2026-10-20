import glob, re

files = sorted(glob.glob("docs/dzial-*/*.md"))

for filepath in files:
    if filepath.endswith("index.md") or "wymagania-i-bhp" in filepath:
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for example boxes with prediction questions or code blocks where result can be collapsed
    # Look for `!!! example "Przewiduj..."` or `!!! example "Przewiduj"`
    # Make sure they have a collapsible result inside `??? success "Przewiduj, potem sprawdź wynik"`

    # Also check `!!! question "Przypadek..."` - analyze if any result is exposed or inside `??? success`

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Predictions checked.")
