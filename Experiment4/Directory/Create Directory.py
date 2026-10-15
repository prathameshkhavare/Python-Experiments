import os

name = input("Enter directory name: ")

os.makedirs(name, exist_ok=True)

print("Directory created successfully.")
print("Directory contents:", os.listdir("."))