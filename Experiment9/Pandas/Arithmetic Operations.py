import pandas as pd

data = {
    'A': [10, 20, 30, 40],
    'B': [5, 10, 15, 20]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("Addition:")
print(df['A'] + df['B'])

print("Subtraction:")
print(df['A'] - df['B'])

print("Multiplication:")
print(df['A'] * df['B'])