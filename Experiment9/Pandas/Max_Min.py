import pandas as pd

marks = pd.Series([75, 85, 90, 65, 95])

print("Maximum:", marks.max())
print("Minimum:", marks.min())
print("Mean:", marks.mean())
print("Standard Deviation:", marks.std())
print("Sum:", marks.sum())