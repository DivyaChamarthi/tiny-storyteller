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