import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.canadianctb.ca/")

driver.maximize_window()

time.sleep(10)
store = driver.find_element(By.XPATH, '//section[@id="home"]//h3[text()]').text
print(store)
driver.find_element(By.XPATH, '//span[text()="Why CCTB"]').click()
time.sleep(5)
driver.close()