import math

x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms: "))
s = 0

for i in range(n):
    s = s + ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)

print("Cosine series =", s)