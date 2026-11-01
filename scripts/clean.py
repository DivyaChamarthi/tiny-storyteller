import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "data" / "raw"
CLEAN_DIR = ROOT / "data" / "clean"

# Book-specific rules: where stories begin, and (optionally) where they end
BOOKS = {                                                   
    "grimm": {"first_story": "THE GOLDEN BIRD", "end_before": "*****"},
    "andersen": {"first_story": "THE EMPEROR'S NEW CLOTHES", "end_before": None},
}

# Curly quotes -> straight quotes (decision #5)
QUOTES = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"})


def find_line(lines, matches, what):
    for i, line in enumerate(lines):
        if matches(line):
            return i
    raise ValueError(f"Could not find {what}")


def clean(name, first_story, end_before):                   
    text = (RAW_DIR / f"{name}.txt").read_text(encoding="utf-8-sig")

    # 1. Normalize quotes first, so the matching below doesn't depend on quote style
    text = text.translate(QUOTES)
    lines = text.splitlines()

    # 2. General rule: keep only what's between Gutenberg's markers
    start = find_line(lines, lambda l: l.startswith("*** START OF"), "START marker")
    end = find_line(lines, lambda l: l.startswith("*** END OF"), "END marker")
    lines = lines[start + 1 : end]

    # 3. Book-specific rule: skip front matter up to the first story title.
    #    Exact match, so the indented contents entries don't count.
    first = find_line(lines, lambda l: l == first_story, f"first story '{first_story}'")
    lines = lines[first:]

    # 4. Book-specific rule: cut any afterword after the last story   
    if end_before:
        last = find_line(lines, lambda l: l == end_before, f"end marker '{end_before}'")
        lines = lines[:last]

    # 5. Remove trailing spaces, and collapse runs of blank lines into one
    text = "\n".join(line.rstrip() for line in lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


CLEAN_DIR.mkdir(parents=True, exist_ok=True)
for name, rules in BOOKS.items():                           
    text = clean(name, rules["first_story"], rules["end_before"])
    out = CLEAN_DIR / f"{name}.txt"
    out.write_text(text, encoding="utf-8")
    print(f"{name}: {len(text):,} characters, {len(text.split()):,} words")
    print("  starts with:", text[:50].replace("\n", " | "))