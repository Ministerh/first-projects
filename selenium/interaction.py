from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Key
import time
#add .exe for windows annd ordinary chromeriver for mc
chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
#option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # link_text = driver.find_element(By.LINK_TEXT, "View history")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Huzzain")
# search.send_keys(Keys.END)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# fname = driver.find_element(By.NAME, "fName")
# lname = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")
# fname.send_keys("Minister")
# lname.send_keys("Huzzain")
# email.send_keys("ministerpython@gmail.com")
# sender = driver.find_element(By.TAG_NAME, "button")
# sender.send_keys(Keys.ENTER)


# driver.close()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# get cookie element
cookie = driver.find_element(By.ID, "#cookie")

#get upgrade Item
item = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrade_item = [items.getAttribute("id") for items in item]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = upgrade_item[n]

        #Get current cookie count
        money_element = driver.find_element(By.ID, "#money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "#cps").text
        print(cookie_per_s)
        break

input("It's is done")
driver.quit()




