import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()


assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()
name = "Rahul"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alertbox = driver.switch_to.alert
alert_text = alertbox.text
assert name in alert_text
print(alert_text)
time.sleep(2)
alertbox.accept()
time.sleep(5)
