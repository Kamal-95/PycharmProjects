import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# 1st way
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://Google.com")

# 2nd Way
service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/practice-project")
time.sleep(5)
driver.minimize_window()
driver.back()
time.sleep(3)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(10)
driver.close()




# service_obj = Service()
# driver = webdriver.Edge(service=service_obj)
# driver.get("https://youtube.com")


# service_obj = Service()
# driver = webdriver.Firefox(service=service_obj)
# driver.get("https://Google.com")