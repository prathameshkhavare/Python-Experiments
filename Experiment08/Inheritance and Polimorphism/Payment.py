class Cash:
    def pay(self):
        print("Payment by Cash")

class UPI:
    def pay(self):
        print("Payment by UPI")

c = Cash()
u = UPI()

c.pay()
u.pay()