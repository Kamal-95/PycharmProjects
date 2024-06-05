import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(2)
driver.find_element(By.XPATH, '//span[text()="Veg/fruit name"]').click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)
originalBrowserSortedList = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert browserSortedVeggies == originalBrowserSortedList

