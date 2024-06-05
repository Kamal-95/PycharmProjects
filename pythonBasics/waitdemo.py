import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
results = driver.find_elements(By.XPATH, "//div[@class='product']")
count = len(results)
assert count > 0
for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div//button").click()

assert expected_list == actual_list
print(actual_list)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#----------------------------------------------EXPLICIT WAIT----------------------------------------------------------#
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
code_text = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(code_text)
assert "Code applied ..!" in code_text

prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discounted_amount

time.sleep(5)
