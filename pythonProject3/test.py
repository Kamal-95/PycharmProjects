import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from colorama import Fore, Style
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager




Browsername ="Chrome"
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

try:
    Username = driver.find_element("id", "username")
    print(Fore.GREEN + Style.BRIGHT + '\n Username name Textbox is found')
    # Username.send_keys(input("Enter your Username: "))
    Username.send_keys("teacher1")
    print(Fore.GREEN + Style.BRIGHT + '\n Username is Entered')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Username Textbox is not found')
time.sleep(3)

try:
    Next_Button = driver.find_element("xpath", "//button[@id='login-submit']")
    print(Fore.GREEN + Style.BRIGHT + '\n Next Button is found')
    Next_Button.click()
    print(Fore.GREEN + Style.BRIGHT + '\n Next Button is Clicked')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Next Button is not found')
time.sleep(3)

try:
    password = driver.find_element("xpath", "//input[@id='password']")
    print(Fore.GREEN + Style.BRIGHT + '\n Password Textbox is found')
    password.send_keys("-mF9SF^g}{&S1O")
    print(Fore.GREEN + Style.BRIGHT + '\n Password is entered')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Password Textbox is not found')
time.sleep(3)

try:
    Login_Button = driver.find_element("xpath", "//button[@id='login-submit']")
    print(Fore.GREEN + Style.BRIGHT + '\n Login Button is found')
    Login_Button.click()
    print(Fore.GREEN + Style.BRIGHT + '\n Login Button is Clicked')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Login Button is not found')
time.sleep(10)

try:
    Coursework_link = driver.find_element("xpath", "//span[@class='Bwg0m']")
    print(Fore.GREEN + Style.BRIGHT + '\n Coursework_link Button is found')
    Coursework_link.click()
    print(Fore.GREEN + Style.BRIGHT + '\n Coursework_link Button is Clicked')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Coursework_link Button is not found')
time.sleep(10)

try:
    Wall_link = driver.find_element("xpath", '//div[text()="18: Wall"]')
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is found')
    Wall_link.click()
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is Clicked')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is not found')
time.sleep(10)

try:
    Wall_link = driver.find_element("xpath", '//a[text()="18.1 Wall"]')
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is found')
    Wall_link.click()
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is Clicked')

except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Wall_link Button is not found')
time.sleep(20)


