import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kamali")
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password1")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.XPATH, '//select[@id="exampleFormControlSelect1"]'))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, '//input[@class="btn btn-success"]').click()
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys("test12")
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message
time.sleep(4)
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()
time.sleep(10)
driver.close()


