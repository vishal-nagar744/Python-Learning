# GET request (server se data lena)

import requests

# Example: Public API se JSON data lena
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200: # ✅ Request successful
    data = response.json()
    print("📥 Data from API:", data)
else:
    print("❌ Error:", response.status_code)   


#  POST request (server ko data bhejna)

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My First Post",
    "body": "Learning API with Python",
    "userId": 101
}

response = requests.post(url, json=payload)

if response.status_code == 201: # ✅ Resource created
    print("Data sent successfully !", response.json())

else:
    print("❌ Error:", response.status_code)



# httpx (async support)
 
import httpx
import asyncio   

async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print("📥 Async Data:", response.json())

    asyncio.run(fetch_data())