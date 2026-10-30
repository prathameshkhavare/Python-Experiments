class Manager:
    def role(self):
        print("Manager manages the team")

class Developer:
    def role(self):
        print("Developer writes code")

m = Manager()
d = Developer()

m.role()
d.role()