book1 = input("Enter text of Book 1: ").lower()
book2 = input("Enter text of Book 2: ").lower()

words1 = set(book1.split())
words2 = set(book2.split())

print("Unique words in Book 1:", words1)
print("Unique words in Book 2:", words2)

print("Common words:", words1 & words2)
print("Words unique to Book 1:", words1 - words2)
print("Words unique to Book 2:", words2 - words1)

all_words = words1 | words2
print("Total unique words across both books:", len(all_words))