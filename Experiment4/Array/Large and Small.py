from array import array

n = int(input("Enter number of elements: "))
a = array('i')

for i in range(n):
    x = int(input("Enter an element: "))
    a.append(x)

print("Largest element:", max(a))
print("Smallest element:", min(a))