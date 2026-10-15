try:
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("\nStudent Details")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

except ValueError as e:
    print("Error:", e)

finally:
    print("Student validation completed")