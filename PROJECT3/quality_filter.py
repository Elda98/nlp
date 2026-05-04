import json
import re

INPUT = "data/dataset_dedup.jsonl"
OUTPUT = "data/dataset_filtered.jsonl"

kept = 0
removed = 0


def is_good(text):
    if len(text) < 50:
        return False

    if "http" in text or "www" in text:
        return False

    arabic_chars = len(re.findall(r'[\u0600-\u06FF]', text))
    if arabic_chars / max(len(text), 1) < 0.4:
        return False

    symbols = len(re.findall(r'[^\w\s\u0600-\u06FF]', text))
    if symbols / max(len(text), 1) > 0.3:
        return False

    if re.search(r'(.)\1{10,}', text):
        return False

    return True


with open(INPUT, "r", encoding="utf-8") as f_in, \
     open(OUTPUT, "w", encoding="utf-8") as f_out:

    for line in f_in:
        obj = json.loads(line)
        text = obj["text"]

        if is_good(text):
            f_out.write(json.dumps(obj, ensure_ascii=False) + "\n")
            kept += 1
        else:
            removed += 1
   
print(" Filtering Done")
print("Kept:", kept)
print("Removed:", removed)
