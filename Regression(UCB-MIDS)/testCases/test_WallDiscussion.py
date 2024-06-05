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

        try:
            self.lp.click_WallDiscussion()
            print("Wall Discussion link is clicked")
        except NoSuchElementException:
            print("Wall Discussion link is not found")

        try:
            self.lp.click_wall()
            print("Wall link is clicked")
            act_title = self.driver.title
            if act_title == "18.1 Wall":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Wall link is not found")
        time.sleep(20)



        try:
            self.lp.click_Create_New_Wall_Post()
            print("click_Create_New_Post button is clicked")
        except NoSuchElementException:
            print("click_Create_New_Post button is not found")

        try:
            self.lp.Discussion_title()
            print("Discussion Title is printed")
        except NoSuchElementException:
            print("Discussion tile textbox is not found")

        try:
            self.lp.Discussion_content()
            print("Discussion content is printed")
        except NoSuchElementException:
            print("Discussion content textbox is not found")

        try:
            self.lp.Attachment()
            print("Choose local file button is found and clicked")
        except NoSuchElementException:
            print("Choose local file button is not found")

        try:
            self.lp.Discussion_Submit_button()
            print("Discussion Submit button is found and clicked")
        except NoSuchElementException:
            print("Discussion Submit button is not found")



        try:
            self.lp.Open_Wall_discussion_prompt_page()
            print("discussion_prompt_page is Opened")
        except NoSuchElementException:
            print("discussion_prompt_page is Opened")


        try:
            self.lp.Collapse_post()
            print("Discussion post is Collapsed ")
            time.sleep(10)
        except NoSuchElementException:
            print("Collapse post button is not working")


        try:
            self.lp.Expand_post()
            print("Discussion Post is Expanded")
        except NoSuchElementException:
            print("Expand post button is not working")

        try:
            self.lp.back_to_top()
            time.sleep(10)
            print("Back to top button is found and clicked")
        except NoSuchElementException:
            print("Back to top button is not found")

        try:
            self.lp.Back_to_Most_expensive_pizza()
            time.sleep(10)
            print("Back to Wall button is found and clicked")
        except NoSuchElementException:
            print("Back to WAll button is not found")








class Test_002_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu"
    username = "teacher1"
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
            self.lp.Click_faculty_coursework()
            print("Coursework link is clicked")
        except NoSuchElementException:
            print("Coursework link is not found")

        try:
            self.lp.click_WallDiscussion()
            print("Wall Discussion link is clicked")
        except NoSuchElementException:
            print("Wall Discussion link is not found")

        try:
            self.lp.click_wall()
            print("Wall link is clicked")
            act_title = self.driver.title
            if act_title == "18.1 Wall":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Wall link is not found")
        time.sleep(20)


        try:
            self.lp.Open_faculty_discussion_prompt_page()
            print("discussion_prompt_page is Opened")
        except NoSuchElementException:
            print("discussion_prompt_page is Opened")

        try:
            self.lp.Collapse_post()
            print("Discussion post is Collapsed ")
        except NoSuchElementException:
            print("Collapse post button is not working")


        try:
            self.lp.Expand_post()
            print("Discussion Post is Expanded")
        except NoSuchElementException:
            print("Expand post button is not working")

        try:
            self.lp.PostaReply()
            print("post a reply button is clicked by faculty")
        except NoSuchElementException:
            print("post a reply button is not found & clicked by faculty")

        try:
            self.lp.faculty_reply_on_student_post()
            print("Reply is working fine")
        except NoSuchElementException:
            print("faculty_reply_on_student_post is not working")



class Test_003_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
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
        self.lp.Student_Expand_reply()
        self.lp.Open_discussion_prompt_page()
        time.sleep(10)
        self.lp.Student_reply_button_click()
        time.sleep(5)
        self.lp.student_reply_on_faculty_reply()



class Test_004_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
    username = "teacher1"
    password = "-mF9SF^g}{&S1O"

    def test_login(self):
        self.driver.implicitly_wait(40)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.ClickNext()
        self.lp.setPassword(self.password)
        self.lp.ClickSubmit()
        self.lp.Student_Expand_reply()
        self.lp.Open_discussion_prompt_page()
        time.sleep(10)
        self.lp.click_mention_reply_button()
        time.sleep(5)
        self.lp.mention_reply_by_faculty()




class Test_005_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
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
        self.lp.Student_Expand_reply()
        self.lp.Open_discussion_prompt_page()
        time.sleep(10)
        self.lp.Student_reply_on_his_own_post_button()
        time.sleep(5)
        self.lp.student_reply_on_own_post()
        time.sleep(5)
        try:
            self.lp.Expand_reply_test()
            print("Expand reply button is visible")
        except NoSuchElementException:
            print("Expand reply button is not visible")
        time.sleep(10)

#################################################################################################################



class Test_006_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu"
    username = "teacher1"
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
            self.lp.Click_faculty_coursework()
            print("Coursework link is clicked")
        except NoSuchElementException:
            print("Coursework link is not found")

        try:
            self.lp.click_WallDiscussion()
            print("Wall Discussion link is clicked")
        except NoSuchElementException:
            print("Wall Discussion link is not found")

        try:
            self.lp.click_wall()
            print("Wall link is clicked")
            act_title = self.driver.title
            if act_title == "18.1 Wall":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Wall link is not found")
        time.sleep(20)

        # try:
        #     self.lp.click_Expand_Wall_Discussion_Overview()
        #     print(" Discussion Summary link is expanded")
        # except NoSuchElementException:
        #     print("Discussion Summary link is not found")
        #
        # try:
        #     self.lp.click_Collapsed_Wall_Discussion_Overview()
        #     print(" Discussion Summary link is Collapsed")
        # except NoSuchElementException:
        #     print("Discussion Summary link is not found")

        try:
            self.lp.click_Create_New_Wall_Post()
            print("click_Create_New_Post button is clicked")
        except NoSuchElementException:
            print("click_Create_New_Post button is not found")

        try:
            self.lp.Faculty_Discussion_title()
            print("Discussion Title is printed")
        except NoSuchElementException:
            print("Discussion tile textbox is not found")
        time.sleep(2)

        try:
            self.lp.Faculty_Discussion_content()
            print("Discussion content is printed")
        except NoSuchElementException:
            print("Discussion content textbox is not found")


        try:
            self.lp.Attachment()
            print("Choose local file button is found and clicked")
        except NoSuchElementException:
            print("Choose local file button is not found")

        try:
            self.lp.Discussion_Submit_button()
            print("Discussion Submit button is found and clicked")
        except NoSuchElementException:
            print("Discussion Submit button is not found")
        time.sleep(20)

        try:
            self.lp.Faculty_discussion_prompt_page()
            print("Faculty discussion_prompt_page is Opened")
        except NoSuchElementException:
            print("Faculty discussion_prompt_page is not Opened")
        time.sleep(5)

        try:
            self.lp.Back_to_Most_expensive_pizza()
            print("Back to Wall button is found and clicked")
        except NoSuchElementException:
            print("Back to Wall button is not found")
        time.sleep(3)




class Test_007_Login(BaseClass):
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

        try:
            self.lp.click_WallDiscussion()
            print("Wall Discussion link is clicked")
        except NoSuchElementException:
            print("Wall Discussion link is not found")

        try:
            self.lp.click_wall()
            print("Wall link is clicked")
            act_title = self.driver.title
            if act_title == "18.1 Wall":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Wall link is not found")
        time.sleep(20)


        try:
            self.lp.Faculty_Open_discussion_prompt_page()
            print("Faculty discussion_prompt_page is Opened")
        except NoSuchElementException:
            print("Faculty discussion_prompt_page is not Opened")
        time.sleep(2)

        try:
            self.lp.Faculty_Collapse_post()
            print("Discussion post is Collapsed ")
        except NoSuchElementException:
            print("Collapse post button is not working")


        try:
            self.lp.Faculty_Expand_post()
            print("Discussion Post is Expanded")
        except NoSuchElementException:
            print("Expand post button is not working")

        try:
            self.lp.PostaReply()
            print("post a reply button is clicked by Student")
        except NoSuchElementException:
            print("post a reply button is not found & clicked by Student")

        try:
            self.lp.Student_reply_on_Faculty_post()
            print("Student reply on faculty post")
        except NoSuchElementException:
            print("Student reply on faculty post is not working")


class Test_008_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
    username = "teacher1"
    password = "-mF9SF^g}{&S1O"

    def test_login(self):
        self.driver.implicitly_wait(40)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.ClickNext()
        self.lp.setPassword(self.password)
        self.lp.ClickSubmit()
        time.sleep(30)
        self.lp.Faculty_Open_discussion_prompt_page()
        time.sleep(10)
        self.lp.Student_reply_button_click()
        time.sleep(5)
        self.lp.faculty_reply_on_student_reply()
        time.sleep(10)




class Test_009_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
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
        time.sleep(20)
        self.lp.Faculty_Open_discussion_prompt_page()
        time.sleep(20)
        self.lp.click_mention_reply_button()
        time.sleep(5)
        self.lp.mention_reply_by_student()
        time.sleep(10)




class Test_010_Login(BaseClass):
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/ce70973b-619f-49d5-a2c7-90f4074bf46d/segment/d3e592f2-eb71-483b-a2e9-d56883a8a176"
    username = "teacher1"
    password = "-mF9SF^g}{&S1O"

    def test_login(self):
        self.driver.implicitly_wait(40)
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.ClickNext()
        self.lp.setPassword(self.password)
        self.lp.ClickSubmit()
        time.sleep(20)
        self.lp.Faculty_Open_discussion_prompt_page()
        time.sleep(10)
        self.lp.Student_reply_on_his_own_post_button()
        time.sleep(5)
        self.lp.Faculty_reply_on_own_post()
        time.sleep(10)
        self.lp.faculty_post_reply_count()
        time.sleep(10)






