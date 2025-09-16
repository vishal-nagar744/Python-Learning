# Example: Dummy API + NumPy Analysis
# Case: Users ke ages ka analysis

# Dummy API se users fetch karenge aur unki ages ka mean, max, min, standard deviation calculate karenge.

import requests
import numpy as np

# Step 1: Dummy API se data fetch
url = "https://dummyjson.com/users"
response = requests.get(url)
data = response.json()

# Step 2: Ages nikalna
ages = [user["age"] for user in data["users"]]

# Step 3: NumPy Analysis
ages_array = np.array(ages)

print("👥 Users Age Analysis")
print("All Ages:", ages_array)
print("Average Age:", np.mean(ages_array))
print("Max Age:", np.max(ages_array))
print("Min Age:", np.min(ages_array))
print("Std Dev (variation):", np.std(ages_array))
