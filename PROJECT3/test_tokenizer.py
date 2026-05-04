
from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("tokenizer.json")

text = "أنا أحب الذكاء الاصطناعي"

output = tokenizer.encode(text)

print("Tokens IDs:", output.ids)
print("Tokens:", output.tokens)

decoded = tokenizer.decode(output.ids)
print("Decoded:", decoded)
