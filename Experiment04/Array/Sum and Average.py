from array import array

n = int(input("Enter number of elements: "))
a = array('i')

for i in range(n):
    x = int(input("Enter an element: "))
    a.append(x)

total = sum(a)

print("Sum:", total)

if n > 0:
    print("Average:", total / n)
else:
    print("Average cannot be calculated")