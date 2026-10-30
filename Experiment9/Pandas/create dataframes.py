import pandas as pd

data = {
    'Roll_No': [1, 2, 3, 4],
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Marks': [85, 90, 75, 95]
}

df = pd.DataFrame(data)
print(df)