# Isme user ek product ka naam dalta hai → API (dummyjson.com) se data fetch hota hai
#  → Pandas table + Matplotlib graph me show hota hai.

import requests
import pandas as pd
import matplotlib.pyplot as plt

def search_products(query):
    url = "https://dummyjson.com/products/search"
    params = {"q": query}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data["products"]
    else:
        print("❌ Error:", response.status_code)
        return []

def display_table(products):
    if not products:
        print("⚠️ No products found!")
        return
    
    df = pd.DataFrame(products)[["id", "title", "price", "rating", "stock"]]
    print("\n📦 Products Found:\n")
    print(df)

    # Save CSV
    df.to_csv("products.csv", index=False)
    print("\n✅ Data saved in products.csv")

    return df

def plot_prices(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df["title"], df["price"], color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Product")
    plt.ylabel("Price")
    plt.title("Product Prices")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    query = input("🔎 Enter product name to search: ")
    products = search_products(query)

    df = display_table(products)
    if df is not None:
        plot_prices(df)
