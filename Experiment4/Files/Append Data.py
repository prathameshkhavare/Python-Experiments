file = open("sample.txt", "a")
data = input("Enter data to append: ")
file.write("\n" + data)
file.close()

file = open("sample.txt", "r")
print("File contents:")
print(file.read())
file.close()