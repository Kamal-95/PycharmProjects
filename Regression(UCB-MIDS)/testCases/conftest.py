from selenium import webdriver
import pytest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager






import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope='class')
def setupBrowser(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
      service_obj = Service("C:\\Users\\kamal.kumar\\Desktop\\chrome\\chromedriver-win64\\chromedriver.exe")
      options = webdriver.ChromeOptions()
      options.add_experimental_option("detach", True)
      driver = webdriver.Chrome(service=service_obj, options=options)

    elif browser_name == 'firefox':
        service_obj1 = Service("C:\\Users\\kamal.kumar\\Desktop\\firefox.exe")
        driver = webdriver.Firefox()
    elif browser_name == 'IE':
        service_obj1 = Service("C:\\Users\\kamal.kumar\\Desktop\\Edge.exe")
        driver = webdriver.Ie()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()