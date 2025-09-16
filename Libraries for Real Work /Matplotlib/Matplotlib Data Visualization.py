# ab data analysis ke baad Data Visualization seekhna important hai.
# Python me do most popular libraries hain:

# Matplotlib → low-level, powerful but thoda verbose.
# Seaborn → high-level, Matplotlib ke upar bani hai → easy aur beautiful plots.


# Matplotlib Basics

import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Line plot
plt.plot(x, y, label="Line Graph", color="blue", marker="o")
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()




# Matplotlib Bar, Scatter, Pie
# Bar Chart
plt.bar(["A", "B", "C"], [10, 20, 15], color="orange")
plt.title("Bar Chart Example")
plt.show()

# Scatter Plot
plt.scatter([5,7,8,7], [5,6,7,8], color="red")
plt.title("Scatter Plot Example")
plt.show()

# Pie Chart
sizes = [30, 40, 20, 10]
labels = ["Apples", "Bananas", "Mangoes", "Grapes"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart Example")
plt.show()