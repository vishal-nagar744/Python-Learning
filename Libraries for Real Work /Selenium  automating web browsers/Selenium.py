# Selenium kya hai?

# Selenium ek library hai jo browser (Chrome, Firefox, Edge) ko control karne ke liye use hoti hai.
# Isse hum button click, form fill, login automation, data scrape karna, ya testing sab kar sakte hain.
# Basically jo kaam insaan manually karta hai browser pe, vo Selenium automatically kar deta hai.

# 2. ChromeDriver / GeckoDriver

# Agar Chrome use karte ho → Download ChromeDriver
# Agar Firefox use karte ho → GeckoDriver use hoga.
# (⚡ New Selenium versions me selenium-manager aata hai jo automatically driver handle kar leta hai, to manual download ki zaroorat nahi.)


# Example 1: Open Google & search automatically

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome browser start karo
driver = webdriver.Chrome()

# Website open
driver.get("https://www.google.com")

# Search box find karo
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium tutorial")  # text type
search_box.send_keys(Keys.RETURN)  # Enter press

time.sleep(5)  # 5 sec rukke result dekhne do
driver.quit()  # browser close


# 👉 Ye code automatically Google open karega → "Python Selenium tutorial" search karega → result show karega → band ho jaayega.



# Example 2: Automate login form
# Suppose ek dummy login page hai https://practicetestautomation.com/practice-test-login/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Username & password dalna
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")

# Login button click
driver.find_element(By.ID, "submit").click()

time.sleep(5)
driver.quit()


# 👉 Ye code automatically login form fill karega aur submit karega.




# Example 3: Scrape product names from website

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")

# All book titles nikalna
books = driver.find_elements(By.TAG_NAME, "h3")
for book in books:
    print(book.text)

time.sleep(5)
driver.quit()

# 🔥 Real-world use cases

# Testing: Website ka login/logout, signup automation.
# Web scraping: Jab data JavaScript se load hota ho.
# Bots: Auto form filling, ticket booking bots, auto-emailing.
# Data entry automation: Browser me repetitive kaam automate karna.