n = int(input("Enter the number of terms: "))
fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + 1 / fact

print("Sum =", sum)