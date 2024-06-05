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

    if "No Courses" in driver.title:
        print(Fore.GREEN + Style.BRIGHT + '\n Login Successfully')
        break
    else:
        print(Fore.GREEN + Style.BRIGHT + '\n Login Failed!!')
        continue
time.sleep(10)



Click_courses = driver.find_element("xpath","//a[contains(text(),'Courses')]")


try:
    if Click_courses.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n Click_courses Button is found')
        Click_courses.click()
        print(Fore.GREEN + Style.BRIGHT + '\n Click_courses Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Click_courses Button is not found')
time.sleep(7)


View_all_past_courses = driver.find_element("xpath",'//a[text()="View all past courses"]')


try:
    if View_all_past_courses.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n View_all_past_courses Button is found')
        View_all_past_courses.click()
        print(Fore.GREEN + Style.BRIGHT + '\n View_all_past_courses Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n View_all_past_courses Button is not found')
time.sleep(7)


QA_main = driver.find_element("xpath","//a[contains(text(),'QA Main Section 1')]")


try:
    if QA_main.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n QA_main Button is found')
        QA_main.click()
        print(Fore.GREEN + Style.BRIGHT + '\n QA_main Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n QA_main Button is not found')
time.sleep(7)


Turn_edit_on = driver.find_element("xpath",'//a[@title="Turn editing on"]')


try:
    if Turn_edit_on.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n Turn_edit_on Button is found')
        Turn_edit_on.click()
        print(Fore.GREEN + Style.BRIGHT + '\n Turn_edit_on Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Turn_edit_on Button is not found')
time.sleep(7)



select_Quiz = driver.find_element("xpath",'//li[@id="section-1"]//option[text()="Quiz"]')


try:
    if select_Quiz.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n select_Quiz Button is found')
        select_Quiz.click()
        print(Fore.GREEN + Style.BRIGHT + '\n select_Quiz Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n select_Quiz Button is not found')
time.sleep(7)



Add_assignment_name = driver.find_element("xpath",'//input[@id="id_name"]')


try:
    if Add_assignment_name.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n Add_assignment_name textbox is found')
        Add_assignment_name.send_keys("Quiz 2nd May 2023")
        print(Fore.GREEN + Style.BRIGHT + '\n Assignment_name is Entered')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Add_assignment_name textbox is not found')
time.sleep(7)

iframe_window_xpath = '//table[@id="id_introeditor_tbl"]//iframe'
iframe_text_xpath = '//body[@id="tinymce"]'
driver.switch_to.frame(driver.find_element("xpath", iframe_window_xpath))
Add_assignment_text = driver.find_element("xpath", iframe_text_xpath)

try:
    if Add_assignment_text.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n Assignment_name iframe textbox is found')
        Add_assignment_text.send_keys("Quiz 2nd May 2023")
        print(Fore.GREEN + Style.BRIGHT + '\n Assignment_name is Entered in Iframe')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n Assignment_name iframe textbox is not found')
time.sleep(7)
driver.switch_to.default_content()
time.sleep(7)



save_display_button = driver.find_element("xpath",'/html/body/div[3]/main/div/div[1]/div/div/div[1]/div/form/fieldset[11]/div/div[1]/fieldset/input[2]')


try:
    if save_display_button.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n save_display_button Button is found')
        save_display_button.click()
        print(Fore.GREEN + Style.BRIGHT + '\n save_display_button Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n save_display_button Button is not found')
time.sleep(7)



click_edit_quiz_button = driver.find_element("xpath", '//input[@value= "Edit quiz"]')

try:
    if click_edit_quiz_button.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n edit_quiz Button is found')
        click_edit_quiz_button.click()
        print(Fore.GREEN + Style.BRIGHT + '\n edit_quiz Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n edit_quiz Button is not found')
time.sleep(7)


click_add_question = driver.find_element("xpath", "//input[@value = 'Add a question ...' and @type='button']")

try:
    if click_add_question.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n click_add_question Button is found')
        click_add_question.click()
        print(Fore.GREEN + Style.BRIGHT + '\n click_add_question Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n click_add_question Button is not found')
time.sleep(5)



click_essay_radio = driver.find_element("xpath", '//input[@id="qtype_essay"]')

try:
    if click_essay_radio.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n click_essay_radio Button is found')
        click_essay_radio.click()
        print(Fore.GREEN + Style.BRIGHT + '\n click_essay_radio Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n click_essay_radio Button is not found')
time.sleep(10)


click_next = driver.find_element("xpath", "//input[@id='chooseqtype_submit']")

try:
    if click_next.is_displayed():
        print(Fore.GREEN + Style.BRIGHT + '\n click_next Button is found')
        click_next.click()
        print(Fore.GREEN + Style.BRIGHT + '\n click_next Button is Clicked')
except NoSuchElementException:
    print(Fore.GREEN + Style.BRIGHT + '\n click_next Button is not found')
time.sleep(10)







