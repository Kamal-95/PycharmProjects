from datetime import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from pageObjects.LoginPage import Login
import time


from utilities.BaseClass import BaseClass



class Test_001_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu"
    username = "student6"
    password = "-mF9SF^g}{&S1O"



    def test_login(self):
        self.driver.implicitly_wait(40)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.ClickNext()
        self.lp.setPassword(self.password)
        self.lp.ClickSubmit()
        act_title = self.driver.title
        if act_title == "Dashboard":
            assert True
        else:
            assert False
        try:
            self.lp.Click_coursework()
            print("Coursework link is clicked")
        except NoSuchElementException:
            print("Coursework link is not found")
        time.sleep(10)
        self.lp.click_Social_group()
        time.sleep(10)
        self.lp.Click_Start_SG()
        time.sleep(5)
        self.lp.Add_GroupName()
        time.sleep(5)
        self.lp.Add_shortName()
        time.sleep(2)
        self.lp.About_Group()
        time.sleep(2)
        self.lp.Whoshouldjoin()
        time.sleep(2)
        self.lp.Add_Topics()
        time.sleep(1)
        self.lp.Check_private()
        time.sleep(5)
        self.lp.Check_Invites()
        time.sleep(5)
        self.lp.Save_changes_button()
