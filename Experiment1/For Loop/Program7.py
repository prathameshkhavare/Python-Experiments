import math

n = int(input("Enter a number: "))

if n < 0:
    print("Square root is not prime")
else:
    root = math.isqrt(n)

    if root * root != n or root < 2:
        print("Square root is not prime")
    else:
        prime = True

        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

        if prime:
            print("Square root is prime")
        else:
            print("Square root is not prime")