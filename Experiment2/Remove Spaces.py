s = input("Enter a string: ")
result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)