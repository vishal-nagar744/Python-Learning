from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook

# ---------- STEP 1: Chrome Browser Start ----------
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# ---------- STEP 2: Search on Google ----------
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium tutorial")
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # results load hone do

# ---------- STEP 3: Get first 5 results ----------
results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]

data = []
for i, result in enumerate(results, start=1):
    title = result.text
    link = result.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
    print(f"{i}. {title} -> {link}")
    data.append([i, title, link])

# ---------- STEP 4: Save in Excel ----------
wb = Workbook()
ws = wb.active
ws.title = "Google Search Results"

# Header row
ws.append(["S.No", "Title", "Link"])

# Data rows
for row in data:
    ws.append(row)

wb.save("google_results.xlsx")
print("✅ Results saved in google_results.xlsx")

# ---------- STEP 5: Close Browser ----------
driver.quit()


# 🔥 Is project me kya hoga? 

# Chrome browser open hoga.
# "Python Selenium tutorial" Google pe search karega.
# Pehle 5 results ka title + link nikaalega.
# Console me print karega.
# Data ek Excel file (google_results.xlsx) me save ho jaayega.
# Browser close ho jaayega.