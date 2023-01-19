# Name: Sresha Ventrapragada
# UT EID: svv346
# sort the words list by length and pring the last 5 words
words = []
sorted_words = []

with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

words.sort(key=len, reverse=True)
sorted_words = words[:5]

for word in sorted_words:
    print(word)

