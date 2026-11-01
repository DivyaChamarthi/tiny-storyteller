# Tiny Storyteller

A small language model I'm building and training from scratch on
public-domain fairy tales, to understand how LLMs work under the hood.

## How to run

Requires Python 3.14.

```
python scripts/download.py   # downloads the raw books into data/raw/
python scripts/clean.py      # writes cleaned text to data/clean/
```

The data isn't committed to this repo — these two scripts rebuild it from Project Gutenberg.