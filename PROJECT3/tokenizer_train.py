from tokenizers import Tokenizer, models, trainers, pre_tokenizers
import json

tokenizer = Tokenizer(models.BPE())

tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

trainer = trainers.BpeTrainer(
    vocab_size=90000,
    special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"]
)

files = ["data/dataset_dedup.jsonl"]

def read_data():
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                yield data["text"]

tokenizer.train_from_iterator(read_data(), trainer)

tokenizer.save("tokenizer.json")

print(" Tokenizer trained!")
