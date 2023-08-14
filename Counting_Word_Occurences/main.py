

freq = {}
text = input()
for piece in text.lower().split():
    # only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())
    # only consider if word has at least one character
    if word:
        freq[word] = 1 + freq.get(word, 0)
max_word = ''
max_count = 0
for (w, c) in freq.items():  # (key, value) tuple representing (word, count)
    if c > max_count:
        max_word = w
        max_count = c
print('The most frequent word is:', max_word)
print('The maximum occurence:', max_count)

