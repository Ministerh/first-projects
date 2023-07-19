from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#add .exe for windows annd ordinary chromeriver for mc
chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=services, options=option)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3649871286&f_AL=true&keywords=python%20automation&refresh=true")
signin = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
signin.click()
time.sleep(5)
#LogIn session
username = driver.find_element(By.ID, "username")
username.send_keys("ministerhussein@gmail.com")
time.sleep(1)
password = driver.find_element(By.ID, "password")
password.send_keys("orlarmiy1?")
time.sleep(1)
button = driver.find_element(By.TAG_NAME, "button")
button.send_keys(Keys.ENTER)
time.sleep(5)

input("Pres Enter to exit")
driver.quit()

