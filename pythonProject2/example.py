import time
from selenium import webdriver

#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
driver.maximize_window()
#launch URL
driver.get("https://www.google.com/")
#identify search box
driver.find_element("name","q").send_keys("Kgf3")
time.sleep(5)
driver.find_element("name","btnK").click()
driver.close()




