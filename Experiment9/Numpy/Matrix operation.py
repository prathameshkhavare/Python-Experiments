import numpy as np

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter first matrix:")
a = []
for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter second matrix:")
b = []
for i in range(r):
    row = list(map(int, input().split()))
    b.append(row)

x = np.array(a)
y = np.array(b)

print("First Matrix:\n", x)
print("Second Matrix:\n", y)
print("Addition:\n", x + y)
print("Subtraction:\n", x - y)
print("Matrix Multiplication:\n", x @ y)
print("Transpose of First Matrix:\n", x.T)