import sys

words = {}
for n, word in enumerate(sys.stdin.read().split()):
    word = word.replace('.', '')
    if word.istitle() and words.get(word) is None:
        words[word] = n
print(*[f"{words.get(word)} - {word}" for word in sorted(words.keys())], sep='\n')
