import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, '[href*="shop"]').click()
products = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    print(productName)
    if productName == "Blackberry":
        driver.find_element(By.XPATH, '//button[text()="Add "]').click()


driver.find_element(By.CSS_SELECTOR, 'a[class*="btn-primary"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
time.sleep(5)
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText