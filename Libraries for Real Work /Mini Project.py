# Project: Dummy API → Pandas → Matplotlib + Seaborn

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: API se data fetch
url = "https://dummyjson.com/users"
response = requests.get(url)
users = response.json()["users"]

# Step 2: Pandas DataFrame me convert
df = pd.DataFrame(users)
print("✅ DataFrame Created!\n")
print(df.head())

# Step 3: Basic Info
print("\n📊 Basic Info:")
print(df[["firstName", "age", "gender", "height", "weight"]].head())

# Step 4: Data Analysis
print("\n👤 Average Age by Gender:")
print(df.groupby("gender")["age"].mean())

print("\n📏 Average Height & Weight by Gender:")
print(df.groupby("gender")[["height", "weight"]].mean())

# Step 5: Visualization

# 1. Gender Count
sns.countplot(x="gender", data=df)
plt.title("Gender Count")
plt.show()

# 2. Age Distribution
sns.histplot(df["age"], kde=True, color="purple")
plt.title("Age Distribution")
plt.show()

# 3. Height vs Weight Scatter
sns.scatterplot(x="height", y="weight", hue="gender", data=df)
plt.title("Height vs Weight (by Gender)")
plt.show()

# 4. Boxplot - Age by Gender
sns.boxplot(x="gender", y="age", data=df)
plt.title("Age Distribution by Gender")
plt.show()



# ⚡ Workflow Explanation

# API Call → requests.get() se data fetch kiya.
# DataFrame → JSON → pandas.DataFrame me convert.
# Analysis → groupby se average age, height, weight nikala.

# Visualization

# Countplot → gender ratio
# Histogram → age distribution
# Scatter → height vs weight relation
# Boxplot → age distribution by gender

# 👉 Output me tujhko ek mini dashboard jaisa feel milega 📊.