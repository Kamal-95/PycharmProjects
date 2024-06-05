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


Browsername = "Chrome"
a = Service(ChromeDriverManager().install())
b = Service(GeckoDriverManager().install())
c = Service(EdgeChromiumDriverManager().install())

if Browsername == "Chrome":
    driver = webdriver.Chrome(service=a)
elif Browsername == "edge":
    driver = webdriver.Edge(service=c)
elif Browsername == "firefox":
    driver = webdriver.Firefox(service=b)
else:
    print("Browser Not Found")


driver.maximize_window()
driver.get("https://learn.datascience.berkeley.edu")
current_time = datetime.datetime.now()
print(Fore.GREEN + Style.BRIGHT + '\n Script Start Time', current_time.strftime("%Y-%m-%d %H:%M"))

while True:
    Username_textbox = driver.find_element("id", "username")
    Next_Button = driver.find_element("xpath", "//button[@id='login-submit']")
    password_box = driver.find_element("id", "password")
    Login_Button = driver.find_element("xpath", "//button[@id='login-submit']")

    try:
        assert Username_textbox.is_displayed(), " "
        print(Fore.GREEN + Style.BRIGHT + '\n Username name Textbox is found')
        Username_textbox.clear()
        Username_textbox.send_keys(input("Enter username: "))
        print(Fore.GREEN + Style.BRIGHT + '\n Username is Entered')
    except NoSuchElementException:
        print(Fore.GREEN + Style.BRIGHT + '\n Username Textbox is not found')
    time.sleep(7)

    try:
        if Next_Button.is_displayed():
            print(Fore.GREEN + Style.BRIGHT + '\n Next Button is found')
            Next_Button.click()
            print(Fore.GREEN + Style.BRIGHT + '\n Next Button is Clicked')
    except NoSuchElementException:
        print(Fore.GREEN + Style.BRIGHT + '\n Next Button is not found')
    time.sleep(7)

    try:
        #assert password_box.is_displayed(), " "
        print(Fore.GREEN + Style.BRIGHT + '\n Password Textbox is found')
        password_box.clear()
        password_box.send_keys(input("Enter password: "))
        print(Fore.GREEN + Style.BRIGHT + '\n Password is entered')
    except NoSuchElementException:
        print(Fore.GREEN + Style.BRIGHT + '\n Password Textbox is not found')
    time.sleep(7)

    try:
        assert Login_Button.is_displayed(), " "
        print(Fore.GREEN + Style.BRIGHT + '\n Login Button is found')
        Login_Button.click()
        print(Fore.GREEN + Style.BRIGHT + '\n Login Button is Clicked')
    except NoSuchElementException:
        print(Fore.GREEN + Style.BRIGHT + '\n Login Button is not found')
    time.sleep(10)

    if "Dashboard" in driver.title:
        print(Fore.GREEN + Style.BRIGHT + '\n Login Successfully')
        break
    else:
        print(Fore.GREEN + Style.BRIGHT + '\n Login Failed!!')
        continue
