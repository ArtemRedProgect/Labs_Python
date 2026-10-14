from collections import Counter
text = input('Введите текст:' )

clearWords = []
for word in text.split():
    cleanWord = word.strip("—.,!?()«» ").lower()
    if cleanWord:
        clearWords.append(cleanWord)

print("Количество слов: ", len(clearWords))

counts = Counter(clearWords)
print(counts)
print("Самые часто попадющееся слово: ", counts.most_common(1))

max_word = max(clearWords, key = len)
min_word = min(clearWords, key = len)
print(f"Слово с самой большой длиной: ({max_word}). Его длина: {len(max_word)}")
print(f"Слово с самой маленькой длиной: ({min_word}). Его длина: {len(min_word)}")