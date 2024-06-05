import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service_obj = Service(executable_path="C://Users//kamal.kumar//Desktop//chrome//chromedriver-win64//chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element("xpath", '(//a[text()="Data Structures"])[1]')

# create action chain object
action = ActionChains(driver)

# context click the item
action.context_click(on_element=element)

# perform the operation
action.perform()


# driver.get("https://www.youtube.com/results?search_query=learning+python")
# time.sleep(10)
# driver.find_element("xpath", '(//div[@id="playlist-thumbnails"])[1]').click()
# time.sleep(5)
# element = "(//div[@id='playlist-thumbnails'])[2]"
# context_click(on_element=element)
# driver.execute_script("window.open('(//div[@id='playlist-thumbnails'])[2]');")
# time.sleep(10)
# driver.quit()




