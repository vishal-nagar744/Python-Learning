# Python Requests library ko detail me samjhte hain.
# Ye API se data lene (GET) aur bhejne (POST, PUT, DELETE) ke liye sabse zyada use hoti hai.

# Basic GET Request
import requests

url = "https://dummyjson.com/products/1"
response = requests.get(url)

print("✅ Status Code:", response.status_code)   # 200 = success
print("📦 JSON Response:", response.json())


# GET with Params (Query Parameters)
url = "https://dummyjson.com/products/search"
params = {"q": "phone"}  # ?q=phone
response = requests.get(url, params=params)

print("🔎 Products Found:", response.json()["total"])



# POST Request (Data bhejna)
url = "https://dummyjson.com/users/add"
data = {
    "firstName": "Vishal",
    "lastName": "Nagar",
    "age": 21
}

response = requests.post(url, json=data)
print("✅ Created User:", response.json())



# PUT (Update) Request
url = "https://dummyjson.com/users/1"
update = {"lastName": "Updated"}

response = requests.put(url, json=update)
print("✏️ Updated User:", response.json())



# DELETE Request
url = "https://dummyjson.com/users/1"
response = requests.delete(url)
print("🗑️ Deleted User:", response.json())