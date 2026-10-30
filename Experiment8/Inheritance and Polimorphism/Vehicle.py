class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

brand = input("Enter brand: ")
model = input("Enter model: ")

c = Car(brand, model)
c.display()