import json

INPUT = "data/dataset.jsonl"
OUTPUT = "data/dataset_dedup.jsonl"

seen = set()
kept = 0
removed = 0

with open(INPUT, "r", encoding="utf-8") as f_in, \
     open(OUTPUT, "w", encoding="utf-8") as f_out:

    for line in f_in:
        obj = json.loads(line)
        text = obj["text"].strip()

        if text in seen:
            removed += 1
            continue

        seen.add(text)
        f_out.write(json.dumps({"text": text}, ensure_ascii=False) + "\n")
        kept += 1

        if kept % 10000 == 0:
            print(f" kept: {kept}")

print("\n Done")
print("Kept:", kept)
print("Removed duplicates:", removed)
