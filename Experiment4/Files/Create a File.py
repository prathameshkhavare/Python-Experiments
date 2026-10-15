file = open("sample.txt", "w")
data = input("Enter data to write: ")
file.write(data)
file.close()

file = open("sample.txt", "r")
print("File contents:")
print(file.read())
file.close()