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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")
        time.sleep(20)

        try:
            self.lp.verify_Gradelink_present()
            print("Grade link is found")
        except NoSuchElementException:
            print("Grade link is not found")
        time.sleep(5)

        try:
            self.lp.verify_faculty_name_with_tag_name()
            print("faculty name with tag name is found")
        except NoSuchElementException:
            print("faculty name with tag name is not found")
        time.sleep(5)

        try:
            self.lp.Expand_reply_test()
            print("Expand reply button is visible")
        except NoSuchElementException:
            print("Expand reply button is not visible")
        time.sleep(10)



        try:
            self.lp.click_Expand_Discussion_Overview()
            print("Expand Discussion Overview link is clicked")
        except NoSuchElementException:
            print("Expand Discussion Overview link is not found")

        try:
            self.lp.click_Create_New_Post()
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
            self.lp.Expand_post()
            print("Discussion Post is Expanded")
        except NoSuchElementException:
            print("Expand post button is not working")

        try:
            self.lp.Collapse_post()
            print("Discussion post is Collapsed ")
        except NoSuchElementException:
            print("Collapse post button is not working")

        try:
            self.lp.Open_discussion_prompt_page()
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
            self.lp.back_to_top()
            print("Back to top button is found and clicked")
        except NoSuchElementException:
            print("Back to top button is not found")

        try:
            self.lp.Back_to_Most_expensive_pizza()
            print("Back to Most_expensive_pizza button is found and clicked")
        except NoSuchElementException:
            print("Back to Most_expensive_pizza button is not found")



        try:
            self.lp.Expand_all_post()
            print("Expand All post is open")
        except NoSuchElementException:
            print("Expand all post button is not working")

        try:
            self.lp.Collapse_all_post()
            print("Collapse All post is open")
        except NoSuchElementException:
            print("Collapse all post button is not working")




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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")

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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")
        time.sleep(10)
        try:
            self.lp.click_Expand_Discussion_Overview()
            print("Expand Discussion Overview link is clicked")
        except NoSuchElementException:
            print("Expand Discussion Overview link is not found")

        try:
            self.lp.click_Create_New_Post()
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
        time.sleep(10)

        try:
            self.lp.Faculty_discussion_prompt_page()
            print("Faculty discussion_prompt_page is Opened")
        except NoSuchElementException:
            print("Faculty discussion_prompt_page is not Opened")
        time.sleep(5)

        try:
            self.lp.Back_to_Most_expensive_pizza()
            print("Back to Most_expensive_pizza button is found and clicked")
        except NoSuchElementException:
            print("Back to Most_expensive_pizza button is not found")
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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")


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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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
    baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
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



class Test_011_Login(BaseClass):
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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")

        time.sleep(25)

        try:
            self.lp.verify_Gradebooklink_present()
            print("Grade book link is found")
        except NoSuchElementException:
            print("Grade book link is not found")
        self.lp.select_student_publish_score()
        time.sleep(10)



class Test_012_Login(BaseClass):
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
            self.lp.click_Discussion()
            print("Discussion link is clicked")
        except NoSuchElementException:
            print("Discussion link is not found")

        try:
            self.lp.click_Most_Expensive_Pizza()
            print("Most_Expensive_Pizza link is clicked")
            act_title = self.driver.title
            if act_title == "15.1 Most Expensive Pizza!":
                assert True
                print(act_title, "Page is opened")
            else:
                assert False
        except NoSuchElementException:
            print("Most_Expensive_Pizza link is not found")
        time.sleep(20)

        try:
            self.lp.Student_Gradelink()
            print("Grade link is clicked")
        except NoSuchElementException:
            print("Grade link is not found")
        time.sleep(10)



# class Test_013_Login(BaseClass):
#     baseURL = "https://learn.datascience.berkeley.edu/ap/courses/262/sections/252816a5-7896-4046-a3bf-a86b8e2d1216/coursework/module/2e882bba-829d-4b2a-84a3-05e7b1cc9c53/segment/a6bd72f1-c57f-4007-8b91-1637dbfe9646"
#     username = "teacher1"
#     password = "-mF9SF^g}{&S1O"
#
#     def test_login(self):
#         self.driver.implicitly_wait(40)
#         self.driver.get(self.baseURL)
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.ClickNext()
#         self.lp.setPassword(self.password)
#         self.lp.ClickSubmit()
#         time.sleep(30)
#         try:
#             self.lp.faculty_edit_own_reply()
#             time.sleep(20)
#             print("edited")
#         except NoSuchElementException:
#             print("faculty reply not found")
#         try:
#             self.lp.faculty_delete_own_reply()
#             time.sleep(20)
#             print("Deleted")
#         except NoSuchElementException:
#             print("faculty reply not found")
#
#         try:
#             self.lp.faculty_delete_student_reply()
#             time.sleep(20)
#             print("Deleted student reply on post")
#         except NoSuchElementException:
#             print("Student reply not found")
#
#         try:
#             self.lp.Back_to_Most_expensive_pizza()
#             print("Back to Most_expensive_pizza button is found and clicked")
#         except NoSuchElementException:
#             print("Back to Most_expensive_pizza button is not found")
#         time.sleep(3)
#
#         try:
#             self.lp.Edit_faculty_post()
#             print("Faculty post name is edited")
#         except NoSuchElementException:
#             print("faculty post name is not able to edit")
#         time.sleep(30)
#
#         try:
#             self.lp.Delete_faculty_post()
#             print("Faculty post is Deleted Successfully")
#         except NoSuchElementException:
#             print("faculty post name is not able to Delete")
#         time.sleep(30)
#
#         try:
#             self.lp.Delete_student_post()
#             print("Student post is deleted Successfully")
#         except NoSuchElementException:
#             print("Student Post is not able to Delete")
#         time.sleep(30)
#
