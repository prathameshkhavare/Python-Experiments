import os

name = input("Enter directory name: ")

if os.path.isdir(name):
    print("Directory exists.")
else:
    print("Directory does not exist.")