file = open("sample.txt", "w")
data = input("Enter text: ")
file.write(data)
file.close()

file = open("sample.txt", "r")
text = file.read()
file.close()

lines = len(text.splitlines())
words = len(text.split())
characters = len(text)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)