from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import datetime

chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=services, options=option)

driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

# # get cookie element
# cookie = driver.find_element(By.ID, "cookie")

# # five seconds 
# five_seconds = time.time() + 5

# # five minutes
# five_minutes = time.time() + (5 * 60)


# while True:
#     cookie.click()

#     # affordable purchase
#     if time.time() > five_seconds:

#         affordable_purchase = driver.find_elements(By.CSS_SELECTOR, '#store b')
#         print(affordable_purchase.text)
# #amount of money

#     avail_money = driver.find_element(By.ID, 'money')
#     print(avail_money.text)
#     break

#this was my final code import ti

TIMER_DURATION = (5*60)  # in seconds #

# ELEMENTS #
cookie = driver.find_element(By.ID, "cookie")
store_ids = ["buyCursor", "buyGrandma", "buyFactory"]

# TIMER #
timeout = time.time() + (TIMER_DURATION*60)

# MAKE PURCHASES #
purchases = []

def purchase_engine():
    """checks which items are available and buys the most expensive item"""
    for id in store_ids[::-1]:
        item = driver.find_element(By.ID, id)
        if item.get_attribute("class") == "" and id not in purchases:
            item.click()
            purchases.append(id)
            break
        elif len(purchases) >= len(store_ids) and item.get_attribute("class") == "":
             item.click()
             break

# GAMEPLAY LOOP #
while time.time() <= timeout:
    cookie.click()
    if datetime.datetime.now().second % 5 == 0:
        purchase_engine()
cps = driver.find_element(By.ID, "cps").text
driver.quit()
print("Time is up.")
print(cps)
