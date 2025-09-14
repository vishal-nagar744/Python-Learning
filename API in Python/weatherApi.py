# 1. Weather API (GET request)

import requests

API_KEY = "a2be3c6a60748b48b1dcc14cd0e6fe8e"  # Replace with your actual API key
city = "Indore,IN"  # Add country code for accuracy
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print(f"Error {response.status_code}: {response.text}")




# 2. Crypto Price API (GET request)

import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=inr"

response = requests.get(url)
if response.status_code == 200:
    prices = response.json()
    print("₿ Bitcoin (INR):", prices["bitcoin"]["inr"])
    print("Ξ Ethereum (INR):", prices["ethereum"]["inr"])
else:
    print("❌ Error:", response.status_code)


# 3. Fake API (POST request)

import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Learning APIs",
    "body": "Python requests module is cool!",
    "userId": 99
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("✅ Post Created Successfully!")
    print("📥 Response:", response.json())
else:
    print("❌ Error:", response.status_code)
