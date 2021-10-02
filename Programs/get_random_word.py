import random

with open("/usr/share/dict/words", "r") as f:
    words = f.read()

words = words.split()
print(random.choice(words))
