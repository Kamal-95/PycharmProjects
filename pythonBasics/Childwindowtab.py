import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
WindowsOpened = driver.window_handles
driver.switch_to.window(WindowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(WindowsOpened[0])
if "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text:
    print(driver.find_element(By.TAG_NAME, "h3").text)
else:
    print("Error")
time.sleep(5)

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.ID, "mce_0_ifr"))
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("this is my Iframe")
time.sleep(5)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
time.sleep(5)