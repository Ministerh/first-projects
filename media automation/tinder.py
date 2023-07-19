from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


#add .exe for windows annd ordinary chromeriver for mc
chrome_driver_path  = "c:/Users/MINISTER/Documents/chromedriver.exe"
services = Service(executable_path= chrome_driver_path)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=services, options=option)

driver.get("https://tinder.com/)")

accept_cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="I accept"]')))
accept_cookies.click()

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Log in"]')))
login_button.click()

#facebook sign in
# sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')))
# sign_in.click()


# email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'email')))
# #email = driver.find_element(By.ID, 'email')
# email.send_keys("ministerhussein@gmail.com")
# time.sleep(2)

# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pass')))
# # password = driver.find_element(By.ID, 'pass')
# password.send_keys("orlarmiy1?")

# time.sleep(3)
# log = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_0_3F"]')))
# # log = driver.find_element(By.XPATH, '//*[@id="u_0_0_3F"]')
# log.send_keys(Keys.ENTER)
# input("where are you")
