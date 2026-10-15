students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append(name)
    grades.append(grade)
    print("Student added successfully.")

def update_grade():
    name = input("Enter student name to update grade: ")
    if name in students:
        index = students.index(name)
        grades[index] = float(input("Enter new grade: "))
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully.")
    else:
        print("Student not found.")

def average_grade():
    if grades:
        print("Average Grade:", sum(grades) / len(grades))
    else:
        print("No grades available.")

def extreme_grades():
    if grades:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No grades available.")

def display_students():
    if students:
        for i in range(len(students)):
            print(students[i], ":", grades[i])
    else:
        print("No students available.")

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grades")
    print("6. Display All Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_grade()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        average_grade()
    elif choice == "5":
        extreme_grades()
    elif choice == "6":
        display_students()
    elif choice == "7":
        print("Program terminated.")
        break
    else:
        print("Invalid choice. Please try again.")