project1 = set(input("Enter employees in Project 1: ").split())
project2 = set(input("Enter employees in Project 2: ").split())

print("Employees in both projects:", project1 & project2)
print("Employees only in Project 1:", project1 - project2)
print("Employees only in Project 2:", project2 - project1)
print("Total unique employees:", project1 | project2)