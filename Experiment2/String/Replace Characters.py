s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New string =", result)