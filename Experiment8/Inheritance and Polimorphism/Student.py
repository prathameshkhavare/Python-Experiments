class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

class Result(Student):
    def display(self):
        total = self.m1 + self.m2 + self.m3
        print("Name:", self.name)
        print("Total Marks:", total)

name = input("Enter name: ")
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

s = Result(name, m1, m2, m3)
s.display()