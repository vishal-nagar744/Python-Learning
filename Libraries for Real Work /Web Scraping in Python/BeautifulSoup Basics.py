# 🕸️ Web Scraping in Python

# Jab hume API nahi milti, tab hum websites ke HTML se direct data extract karte hain.
# Python me do popular libraries hain:

# BeautifulSoup (bs4) → Simple scraping (HTML parsing)

# Scrapy → Large-scale, powerful scraping framework


# 🔹 1. BeautifulSoup Basics

# Example: Scrape Quotes

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Sabhi quotes find karo
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for q, a in zip(quotes, authors):
    print(f"{q.text}  — {a.text}")



# 👉 Yahaan pe humne:

# requests se page download kiya
# BeautifulSoup se HTML parse kiya
# find_all() se particular tags/classes nikale

