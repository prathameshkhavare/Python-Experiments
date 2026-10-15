s = input("Enter a string: ")
ch = input("Enter character to count: ")
count = 0

for x in s:
    if x == ch:
        count = count + 1

print("Frequency =", count)