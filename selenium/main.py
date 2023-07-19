from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#add .exe for windows annd ordinary chromeriver for mc
chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services, options=option)

driver.get("https://www.python.org/")
# to get element by id
# search_bar = driver.find_element(by="id", value="id-search-field")
# print(search_bar.get_attribute("placeholder"))

Event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time' )
Event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
Events = {}
for n in range(len(Event_name)):
    Events[n] = {
        "time":Event_time[n].text,
        "name":Event_name[n].text
    }
print(Events)

driver.quit()


