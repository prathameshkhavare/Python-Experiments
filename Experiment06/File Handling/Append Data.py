f = open("employee.txt", "a")

emp_id = input("Enter employee ID: ")
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = input("Enter salary: ")

f.write("Employee ID: " + emp_id + "\n")
f.write("Name: " + name + "\n")
f.write("Department: " + department + "\n")
f.write("Salary: " + salary + "\n\n")
f.close()

f = open("employee.txt", "r")
print("\nAll Employee Records:")
print(f.read())
f.close()