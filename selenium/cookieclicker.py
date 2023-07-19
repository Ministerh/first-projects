from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=services, options=option)

driver.get("http://orteil.dashnet.org/experiments/cookie/ ")

# get cookie element
cookie = driver.find_element(By.ID, "cookie")

# five seconds 
five_seconds = time.time() + 5

# five minutes
five_minutes = time.time() + (5 * 60)


while True:
    cookie.click()

    # affordable purchase
    if time.time() > five_seconds:

        affordable_purchase = driver.find_elements(By.CSS_SELECTOR, '#store b')
        print(affordable_purchase.text)
#amount of money

    avail_money = driver.find_element(By.ID, 'money')
    print(avail_money.text)
    break



input("The cookie clicker project")

