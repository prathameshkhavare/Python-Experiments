import numpy as np

n = int(input("Enter number of elements: "))
values = []

for i in range(n):
    values.append(int(input("Enter element: ")))

a = np.array(values)

print("Original Array:", a)
print("Sorted Array:", np.sort(a))
print("Reverse Array:", np.sort(a)[::-1])
print("Unique Elements:", np.unique(a))