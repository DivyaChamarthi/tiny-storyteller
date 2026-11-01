import urllib.request
from pathlib import Path

BOOKS = {
    "grimm": 2591,     # Grimms' Fairy Tales
    "andersen": 1597,  # Andersen's Fairy Tales
}

raw_dir = Path(__file__).parent.parent / "data" / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

for name, book_id in BOOKS.items():
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    out = raw_dir / f"{name}.txt"
    print(f"Downloading {name} from {url}")
    urllib.request.urlretrieve(url, out)
    print(f"  saved {out.stat().st_size:,} bytes")