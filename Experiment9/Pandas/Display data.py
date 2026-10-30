import pandas as pd

df = pd.read_csv('students.csv')

print("Student Data:")
print(df)

print("First 3 Records:")
print(df.head(3))

print("Column Names:")
print(df.columns)