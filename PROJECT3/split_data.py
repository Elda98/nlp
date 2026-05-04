import os

INPUT_FILE = "arabic_1M.txt"

OUTPUT_DIR = "chunks"

NUM_CHUNKS = 3

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

chunk_size = len(lines) // NUM_CHUNKS

for i in range(NUM_CHUNKS):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < NUM_CHUNKS - 1 else len(lines)

    output_path = f"{OUTPUT_DIR}/batch_{i}.txt"

    with open(output_path, "w", encoding="utf-8") as out:
        out.writelines(lines[start:end])

    print(f"Created: {output_path}")
