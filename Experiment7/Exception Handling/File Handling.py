try:
    filename = input("Enter file name: ")
    f = open(filename, "r")
    data = f.read()

    print("File Contents:")
    print(data)

    f.close()

except FileNotFoundError:
    print("Error: File does not exist")

except PermissionError:
    print("Error: Permission denied")

finally:
    print("File operation completed")