n = int(input("Enter number of tuples: "))
data = []

for i in range(n):
    a = input("Enter first element: ")
    b = int(input("Enter second element: "))
    data.append((a, b))

sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted list:", sorted_data)