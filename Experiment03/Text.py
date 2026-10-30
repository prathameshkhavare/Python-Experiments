text = input("Enter a paragraph: ").lower()

words = text.split()
frequency = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Total number of words:", len(words))
print("Word frequency:", frequency)

top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("Top 3 most frequent words:")
for word, count in top_words[:3]:
    print(word, ":", count)

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Total number of vowels:", count)