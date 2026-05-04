import os

folder = "chunks"

if not os.path.exists(folder):
    print(" chunks folder not found")
    exit()

files = [f for f in os.listdir(folder) if f.endswith(".txt")]

if not files:
    print(" no chunk files found")
    exit()

total_lines = 0

for file in files:
    path = os.path.join(folder, file)

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f"{file} -> {len(lines)} lines")
        total_lines += len(lines)

print("\n TOTAL LINES:", total_lines)