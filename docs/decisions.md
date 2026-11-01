# Decisions

## 1. Fairy tales as training data
- **Options:** a single novel, fairy tales, modern text
- **Chose:** Grimm + Andersen fairy tales
- **Why:** public domain, consistent storytelling style, small enough for a laptop

## 2. Separate raw and clean data folders
- **Why:** cleaning can always be rerun on untouched originals (reproducibility)

## 3. Python 3.14 instead of the newest 3.15
- **Why:** 3.15 was released weeks ago; AI libraries like PyTorch often take
  time to support new versions

## 4. Keep story titles
- **Options:** keep titles, or strip them for pure story text
- **Chose:** keep
- **Why:** titles mark where each story begins, so the model can learn story
  structure — and might generate its own titles

## 5. Normalize curly quotes to straight quotes
- **Options:** keep original quotes, or convert “ ” ‘ ’ to " and '
- **Chose:** normalize
- **Why:** the model treats ' and ’ as unrelated characters and would learn
  the same thing twice; fewer characters = less for a small model to learn