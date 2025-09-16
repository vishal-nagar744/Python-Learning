# Pandas kya hai?

# Pandas ek data analysis aur manipulation library hai.
# Isme 2 main data structures hote hain:
# Series → 1D (like list / column)
# DataFrame → 2D (like Excel sheet / table)


# Series Example (1D Data)
import pandas as pd

# list se Series
data = [10, 20, 30, 40]
series = pd.Series(data, name="Marks")
print(series)



# DataFrame Example (2D Data)
# dictionary → DataFrame
data = {
    "Name": ["Vishal", "Honey", "Raj"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)



# CSV Read / Write
# CSV file read
df = pd.read_csv("students.csv")
print(df.head())   # first 5 rows

# CSV write
df.to_csv("output.csv", index=False)



