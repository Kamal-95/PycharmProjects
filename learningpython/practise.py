import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.context_click(driver.find_element(By.XPATH, '//select[@name="dropdown-class-example"]')).perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(5)
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(10)