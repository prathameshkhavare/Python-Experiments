class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

name = input("Enter name: ")
salary = float(input("Enter salary: "))

m = Manager(name, salary)
m.display()