import numpy as np

n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    m = float(input("Enter marks: "))
    marks.append(m)

a = np.array(marks)

print("All Marks:", a)
print("Total Marks:", np.sum(a))
print("Average Marks:", np.mean(a))
print("Highest Marks:", np.max(a))
print("Lowest Marks:", np.min(a))