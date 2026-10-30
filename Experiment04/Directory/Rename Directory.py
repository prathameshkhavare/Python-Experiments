import os

name = input("Enter directory name: ")
os.mkdir(name)
print("Directory created successfully.")

new_name = input("Enter new directory name: ")
os.rename(name, new_name)
print("Directory renamed successfully.")

os.rmdir(new_name)
print("Directory removed successfully.")