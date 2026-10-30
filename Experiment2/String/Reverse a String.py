s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reverse string =", rev)