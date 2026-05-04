import os
import json

INPUT_FOLDER = "chunks"
OUTPUT_FILE = "data/dataset.jsonl"

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:

    for file in os.listdir(INPUT_FOLDER):
        if file.endswith(".txt"):
            path = os.path.join(INPUT_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    text = line.strip()

                    if not text:
                        continue

                    obj = {"text": text}
                    out.write(json.dumps(obj, ensure_ascii=False) + "\n")

print(" dataset.jsonl created!")
