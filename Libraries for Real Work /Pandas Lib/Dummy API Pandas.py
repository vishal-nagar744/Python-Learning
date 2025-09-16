
# Dummy API + Pandas Example (Real Time)
# Users ka data fetch karke DataFrame me daalte hain.

import requests
import pandas as pd

# API se data
url = "https://dummyjson.com/users"
res = requests.get(url)
data = res.json()["users"]

# DataFrame banao
df = pd.DataFrame(data)

print(df.head())         # first 5 rows
print(df[["firstName","age","gender"]].head())

# Analysis
print("Average Age:", df["age"].mean())
print("Max Age:", df["age"].max())
print("Users count by gender:")
print(df["gender"].value_counts())