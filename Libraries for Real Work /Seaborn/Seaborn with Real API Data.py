import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dummy Users API
url = "https://dummyjson.com/users"
res = requests.get(url)
users = res.json()["users"]

df = pd.DataFrame(users)

# Gender-wise Age Distribution
sns.boxplot(x="gender", y="age", data=df)
plt.title("Age Distribution by Gender")
plt.show()

# Scatter: Height vs Weight
sns.scatterplot(x="height", y="weight", hue="gender", data=df)
plt.title("Height vs Weight")
plt.show()

# Countplot: Gender Count
sns.countplot(x="gender", data=df)
plt.title("Gender Count")
plt.show()
