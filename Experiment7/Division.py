try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b

    print("First Number:", a)
    print("Second Number:", b)
    print("Division:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero")

except ValueError:
    print("Error: Please enter valid numbers")

finally:
    print("Division operation completed")