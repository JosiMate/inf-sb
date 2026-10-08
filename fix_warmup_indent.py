import glob, re

files = sorted(glob.glob("docs/dzial-*/*.md"))

for filepath in files:
    if filepath.endswith("index.md") or "wymagania-i-bhp" in filepath:
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match ??? rozgrzewka block up to the next heading or admonition outside
    def indent_warmup(match):
        block = match.group(0)
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            if line.startswith("??? rozgrzewka"):
                new_lines.append(line)
            elif line.strip() == "":
                new_lines.append("")
            else:
                # Ensure 4-space indent for everything inside rozgrzewka
                if not line.startswith("    "):
                    new_lines.append("    " + line)
                else:
                    new_lines.append(line)
        return "\n".join(new_lines)

    content = re.sub(r'\?\?\? rozgrzewka "Na rozgrzewkę — 3 minuty, bez zaglądania".*?(?=\n##|\n!!! success "Kryteria|\Z)', indent_warmup, content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Warmup indentation fixed.")
