import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dummy DataFrame
data = {
    "Name": ["Vishal", "Honey", "Raj", "Simran", "Aman"],
    "Age": [21, 22, 23, 20, 24],
    "Marks": [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)

# Histogram (distribution)
sns.histplot(df["Marks"], kde=True)
plt.title("Marks Distribution")
plt.show()

# Scatter Plot
sns.scatterplot(x="Age", y="Marks", data=df, hue="Name", s=100)
plt.title("Age vs Marks")
plt.show()

# Box Plot (outliers dikhata hai)
sns.boxplot(x="Marks", data=df)
plt.title("Boxplot of Marks")
plt.show()
