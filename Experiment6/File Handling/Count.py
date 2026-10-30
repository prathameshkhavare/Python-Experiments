f = open("paragraph.txt", "w")

data = input("Enter a paragraph: ")
f.write(data)
f.close()

f = open("paragraph.txt", "r")
content = f.read()
f.close()

print("\nFile Contents:")
print(content)

print("Lines:", len(content.splitlines()))
print("Words:", len(content.split()))
print("Characters:", len(content))