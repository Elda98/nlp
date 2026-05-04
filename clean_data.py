from datasets import load_dataset
import re
import os


SAVE_FILE = "cleaned.txt"
TARGET = 200000   
BATCH_PRINT = 10000


def clean_text(text):
    text = re.sub(r"http\S+", "", text)  
    text = re.sub(r"<.*?>", "", text)    
    text = re.sub(r"[\u064B-\u065F\u0617-\u061A\u06D6-\u06ED]", "", text)  
    text = re.sub(r"\s+", " ", text).strip()  
    return text


ds = load_dataset(
    "lightonai/ArabicWeb24",
    split="train",
    streaming=True
)


count = 0

with open(SAVE_FILE, "a", encoding="utf-8") as f:
    for sample in ds:

        text = sample.get("text", "")
        text = clean_text(text)

        if len(text) < 30:
            continue

        f.write(text + "\n")
        count += 1

        if count % BATCH_PRINT == 0:
            print(f" Cleaned: {count}")

        if count >= TARGET:
            break

print(" Done cleaning:", count)