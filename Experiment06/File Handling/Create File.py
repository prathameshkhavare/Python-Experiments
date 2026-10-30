f = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll + "\n")
f.write("Course: " + course + "\n")
f.write("Marks: " + marks + "\n")
f.close()

f = open("student.txt", "r")
print("\nStudent Details:")
print(f.read())
f.close()