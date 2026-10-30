import pandas as pd

data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Marks': [75, 92, 68, 88]
}

df = pd.DataFrame(data)

print("Students Scoring Above 80:")
print(df[df['Marks'] > 80])

print("Students Sorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))