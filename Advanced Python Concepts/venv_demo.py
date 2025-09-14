# venv_demo.py

import os
import sys
import requests
import pandas as pd

# 1. Check if virtual environment is active
def check_venv():
    if sys.prefix != sys.base_prefix:
        print("✅ Virtual Environment is ACTIVE")
    else:
        print("⚠️ Virtual Environment is NOT active. Please activate venv before running.")

# 2. Fetch sample API data
def fetch_api_data():
    print("\n🌐 Fetching data from API...")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("✅ API Data fetched successfully!\n")
        return data
    else:
        print("❌ Failed to fetch API data")
        return []

# 3. Display data using pandas
def display_data(data):
    if data:
        df = pd.DataFrame(data, columns=["id", "name", "email"])
        print("📊 User Data from API:")
        print(df)
     # ✅ Save to CSV
        df.to_csv("users.csv", index=False)
        print("\n💾 Data saved to users.csv")
    else:
        print("⚠️ No data to display")

if __name__ == "__main__":
    check_venv()
    users = fetch_api_data()
    display_data(users)



# 🛠 Run Karne Ka Tareeka

# Venv activate karo:

# source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate      # Windows


# Install required libs:

# pip install requests pandas


# Run script:
# python venv_demo.py
