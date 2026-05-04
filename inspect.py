import json

with open("data/dataset_filtered.jsonl", "r", encoding="utf-8") as f:
    for _ in range(10):
        print(json.loads(f.readline())["text"])
        print("-" * 80)