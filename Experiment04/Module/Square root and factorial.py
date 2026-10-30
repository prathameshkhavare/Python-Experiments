import math

n = int(input("Enter a number: "))

if n >= 0:
    print("Square root:", math.sqrt(n))
    print("Factorial:", math.factorial(n))
else:
    print("Enter a non-negative number")