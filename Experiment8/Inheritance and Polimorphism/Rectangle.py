class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Rectangle(Shape):
    def area(self):
        print("Area:", self.length * self.breadth)

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

r = Rectangle(length, breadth)
r.area()