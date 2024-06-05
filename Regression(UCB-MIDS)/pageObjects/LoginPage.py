import time
from datetime import date
from datetime import datetime
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass




class Login(BaseClass):

    textbox_username_id = "username"
    next_button_xpath = "//button[@id='login-submit']"
    textbox_password_id = "//input[@id='password']"
    submit_button_xpath = "//button[@id='login-submit']"
    coursework_xpath = '//a[text()="Coursework"]'
    Discussion_xpath = '//div[text()="15: Discussions"]'
    Most_Expensive_Pizza_xpath = '//a[text()="15.1 Most Expensive Pizza!"]'
    Wall_xpath = '//a[text()="18.1 Wall"]'
    Expand_Discussion_Overview_iframe_xpath = "//iframe[@title='Content: 15.1 Most Expensive Pizza!']"
    Expand_Discussion_Overview_xpath = "(//button[@aria-label='Expand Discussion Overview'])[2]"
    Create_New_Post_xpath = '(//a[text()="Create New Post"])[1]'
    GD_Create_New_Post_xpath = '//article[@aria-label="Group 1, discussion"]//a[text()="Create New Post"]'
    Discussion_title_xpath = "//input[@id='title']"
    Discussion_content_xpath = "//div[@id='text']//p"
    Mention_faculty_xpath = '//span[text()="Florence Hayes"]'
    Bold_xpath = "//i[@class='fa fa-bold']"
    Unordered_list_xpath = "//i[@class='fa fa-list-ul']"
    ordered_list_xpath = "//i[@class='fa fa-list-ol']"
    Italic_test_xpath = "//i[@class='fa fa-italic']"
    Underline_test_xpath = "//button[@id='underline-1']"
    strikeThrough_xpath = "//button[@id='strikeThrough-1']"
    Undo_xpath = "//i[@class='fa fa-rotate-left']"
    Do_xpath = "//i[@class='fa fa-rotate-right']"
    Insert_link_xpath = '//button[@id="insertLink-1"]'
    link_insert_layer_url_xpath = '//input[@placeholder="URL"]'
    link_insert_layer_text_xpath = '//input[@placeholder="Text"]'
    Insert_url_button_xpath = '//button[text()="Insert" and @data-cmd="linkInsert"]'
    Insert_image_link_xpath = '//button[@id="insertImage-1"]'
    Image_by_url_xpath = '//input[@placeholder="http://"]'
    imageInsertByURL_xpath = '//button[@data-cmd="imageInsertByURL"]'
    text_xpath = '//div[@id="text"]'
    insert_video_xpath = '//button[@data-cmd="insertVideo"]'
    paste_in_video_url_xpath = '//input[@placeholder="Paste in a video URL"]'
    videoInsertByURL_xpath = '//button[@data-cmd="videoInsertByURL"]'
    Choose_local_file_button_xpath = "//button[normalize-space()='Choose a local file']"
    camera_xpath = '//div[@title="Camera"]'
    direct_link_xpath = '//div[@title="Direct Link"]'
    paste_your_link_here_xpath = '//input[@placeholder="Paste your link here..."]'
    upload_button_xpath = "//button[normalize-space()='Upload']"
    Google_drive_xpath = '//div[@title="Google Drive"]'
    select_file_Gdrive = '//a[@title="A- Sample rsume.docx"]//div[text()="48 KB"]'
    Dropbox_icon_xpath = '//div[@title="Dropbox"]'
    Discussion_submit_button_xpath = "//button[normalize-space()='Submit']"
    Discussion_submit_button2 = '//button[text()="Submit"]'
    Discussion_post_name_xpath = "(//li//div[@class='_1ryOq']//h2//a[contains(text(),'Automation Student Discussion Post')])[1]"
    Expand_post_xpath = "(//a[contains(text(),'Automation Student Discussion Post')])[1]//..//..//..//button[text()='Expand Post']/*[name()='svg']"
    Collapse_post_xpath = "(//a[contains(text(),'Automation Student Discussion Post')])[1]//..//..//..//button[text()='Collapse Post']/*[name()='svg']"
    back_to_top_xpath = "//button[@aria-label='Back to top']"
    Back_to_Most_expensive_pizza_xpath = '//div[contains(text(), "Back to")]'
    Expand_all_post_xpath = "//button[@aria-label='Expand All Posts']//*[name()='svg']"
    Collapse_all_post_xpath = "//button[@aria-label='Collapse All Posts']//*[name()='svg']"
    iframe_xpath = '//*[@id="root"]//iframe'
    iframe_GD_xpath = '//iframe[@role="main"]'
    faculty_post_a_reply_xpath = '//button[text()="Post a Reply"]'
    Student_Expand_reply_xpath = "(//a[contains(text(),'Automation Student Discussion Post')])[1]//..//..//following-sibling::button[2]/*[name()='svg'][2]"
    faculty_post_reply_count_xpath = "(//a[contains(text(),'Automation Faculty Discussion Post')])[1]//..//..//following-sibling::button//span"
    Student_reply_xpath = '//button[text()="Reply"]'
    mention_reply_button_xpath = "(//button[normalize-space()='Reply'])[2]"
    Grade_link_xpath = "//span[text()='Grades']"
    Faculty_name_xpath = '(//span[text()="Florence Hayes"])[1]'
    Faculty_tag_xpath = '(//span[text()="Florence Hayes"]//..//span[text()="FACULTY"])[1]'
    Mention_student_xpath = '//span[text()="Jason Stone"]'
    Faculty_Expand_post_xpath = "(//a[contains(text(),'Automation Faculty Discussion Post')])[1]//..//..//..//button[text()='Expand Post']/*[name()='svg']"
    Faculty_Collapse_post_xpath = "(//a[contains(text(),'Automation Faculty Discussion Post')])[1]//..//..//..//button[text()='Collapse Post']/*[name()='svg']"
    Faculty_Discussion_post_name_xpath = "(//li//div[@class='_1ryOq']//h2//a[contains(text(),'Automation Faculty Discussion Post')])[1]"
    Faculty_Expand_reply_xpath = "(//a[contains(text(),'Automation Faculty Discussion Post')])[1]//..//..//following-sibling::button[2]/*[name()='svg'][2]"
    Gradebook_link_xpath = '//span[text()="Gradebook"]'
    Student_Profile_label_xpath = '//button[@aria-label="Profile Menu"]'
    student_name_xpath = '//a[text()="Stone, Jason"]'
    Unpublish_button_xpath = "//button[@class='button button--caution']"
    publish_button_xpath = "//button[contains(text(),'Publish')]"
    score_text_xpath = '//input[@id="score-text"]'
    faculty_feedback_xpath = '//div[@class="feedback-input"]//div[@class="fr-wrapper"]//div[@class="fr-element fr-view"]'
    Edit_faculty_post_xpath = '(//button[contains(@aria-label,"Edit Automation Faculty Discussion Post")])[1]'
    Delete_faculty_post_xpath = '(//button[contains(@aria-label,"Delete Automation Faculty Discussion Post")])[1]'
    Delete_continue_button_xpath = '//button[contains(text(),"Continue")]'
    Delete_student_post_xpath = '(//button[contains(@aria-label,"Delete Automation Student Discussion Post")])[1]'
    faculty_edit_own_reply_xpath = '(//button[contains(@aria-label,"Edit reply by Florence Hayes")])[1]'
    faculty_delete_own_reply_xpath = '(//button[contains(@aria-label,"Delete reply by Florence Hayes")])[1]'
    faculty_delete_student_reply_xpath = '(//button[contains(@aria-label,"Delete reply by Jason Stone")])[1]'
    Group_Discussion_xpath = '//a[text()="15.2 Group Discussion on Most Expensive Pizza"]'
    WallDiscussion_xpath = '//div[text()="18: Wall"]'
    Collapsed_Discussion_Overview_xpath = '(//button[@aria-label="Collapse Discussion Overview"])[1]'
    Social_group_xpath = '//a[@href="/local/groups/searchgroups.php"]'
    Start_SG_xpath = '//a[text()="Start a Social Group"]'
    Add_GroupName_xpath = '//input[@name="groupname"]'
    Add_shortName_xpath = '//input[@name="shortname"]'
    About_Group_xpath = '//textarea[@name="aboutgroup"]'
    Whoshouldjoin_xpath = '//textarea[@name="whoshouldjoin"]'
    Topic1_xpath = '//input[@id="id_topic1"]'
    Topic2_xpath = '//input[@id="id_topic2"]'
    Check_private_xpath = '//input[@id="id_chk_private"]'
    Check_Invites_xpath = '//input[@id="id_chk_invite"]'
    Save_changes_button_xpath = '//input[@name="submitbutton"]'



    def __init__(self, driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element("id",self.textbox_username_id).send_keys(username)

    def ClickNext(self):
        self.driver.find_element("xpath", self.next_button_xpath).click()

    def setPassword(self,password):
        self.driver.find_element("xpath", self.textbox_password_id).send_keys(password)

    def ClickSubmit(self):
        self.driver.find_element("xpath", self.submit_button_xpath).click()

    def Click_coursework(self):
        self.driver.find_element("xpath", self.coursework_xpath).click()

    def Click_faculty_coursework(self):
        self.coursework_xpath = '//span[normalize-space()="Coursework"]'
        self.driver.find_element("xpath", self.coursework_xpath).click()

    def click_Discussion(self):
        self.driver.find_element("xpath", self.Discussion_xpath).click()

    def click_WallDiscussion(self):
        self.driver.find_element("xpath", self.WallDiscussion_xpath).click()

    def click_Most_Expensive_Pizza(self):
        self.driver.find_element("xpath", self.Most_Expensive_Pizza_xpath).click()

    def click_Group_Discussion(self):
        self.driver.find_element("xpath", self.Group_Discussion_xpath).click()

    def verify_Gradelink_present(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        Grade_Link = self.driver.find_element("xpath", self.Grade_link_xpath)
        Grade_Link_text = self.driver.find_element("xpath", self.Grade_link_xpath).text
        if Grade_Link.is_displayed():
             print("Grade link is visible =  ", Grade_Link_text)
        else:
             print("Grade link is not Visible")

    def verify_faculty_name_with_tag_name(self):
        faculty_name = self.driver.find_element("xpath", self.Faculty_name_xpath).text
        faculty_tag_name = self.driver.find_element("xpath", self.Faculty_tag_xpath).text
        print(faculty_name, faculty_tag_name)

    def click_Expand_Discussion_Overview(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath",self.Expand_Discussion_Overview_iframe_xpath))
        self.driver.find_element("xpath", self.Expand_Discussion_Overview_xpath).click()

    def click_Collapsed_Wall_Discussion_Overview(self):
        self.driver.find_element("xpath", self.Collapsed_Discussion_Overview_xpath).click()
        self.driver.switch_to.default_content()

    def click_Expand_Wall_Discussion_Overview(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_GD_xpath))
        self.driver.find_element("xpath", self.Expand_Discussion_Overview_xpath).click()

    def click_GD_Create_New_Post(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_GD_xpath))
        self.driver.find_element("xpath", self.GD_Create_New_Post_xpath).click()

    def click_Create_New_Post(self):
        Create_a_new_post_text = self.driver.find_element("xpath", self.Create_New_Post_xpath).text
        print(Create_a_new_post_text)
        Create_a_new_post = self.driver.find_element("xpath", self.Create_New_Post_xpath)
        if Create_a_new_post.is_displayed():
            print("Create a new post button is present")
            Create_a_new_post.click()
        else:
            print("Create a new post button is Not present")


    def Discussion_title(self):
        now = datetime.now()
        d2 = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.driver.find_element("xpath", self.Discussion_title_xpath).send_keys("Automation Student Discussion Post", d2)

    def Discussion_content(self):
        today = date.today()
        d2 = today.strftime(" %B %d, %Y")
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Student Discussion Post", d2, '\nStudent Discussion Post ', d2, '\n@florence')
        self.driver.find_element("xpath", self.Mention_faculty_xpath).click()
        self.driver.find_element("xpath", self.Bold_xpath).click()
        self.driver.find_element("xpath", self.Unordered_list_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nTest Bold & Unordered list")
        self.driver.find_element("xpath", self.Bold_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER, Keys.ENTER)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Test Un bold & ordered List")
        self.driver.find_element("xpath", self.ordered_list_xpath).click()
        self.driver.find_element("xpath", self.Italic_test_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nItalic Test")
        self.driver.find_element("xpath", self.Underline_test_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nUnderline Test")
        self.driver.find_element("xpath", self.strikeThrough_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nStrikeThrough Test")
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nDO & UNDO Test")
        self.driver.find_element("xpath", self.Undo_xpath).click()
        self.driver.find_element("xpath", self.Do_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER)
        self.driver.find_element("xpath", self.Insert_link_xpath).click()
        self.driver.find_element("xpath", self.link_insert_layer_url_xpath).send_keys("http://Google.com")
        self.driver.find_element("xpath", self.link_insert_layer_url_xpath).send_keys(Keys.TAB)
        self.driver.find_element("xpath", self.link_insert_layer_text_xpath).send_keys("Google")
        self.driver.find_element("xpath", self.Insert_url_button_xpath).click()
        self.driver.find_element("xpath", self.text_xpath).click()
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER)
        self.driver.find_element("xpath", self.Insert_image_link_xpath).click()
        self.driver.find_element("xpath", self.Image_by_url_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.imageInsertByURL_xpath).click()
        self.driver.find_element("xpath", self.text_xpath).click()
        self.driver.find_element("xpath", self.insert_video_xpath).click()
        self.driver.find_element("xpath", self.paste_in_video_url_xpath).send_keys("https://www.youtube.com/watch?v=NgjERPTaC4Y")
        self.driver.find_element("xpath", self.videoInsertByURL_xpath).click()

    def Attachment(self):
        #self.driver.find_element("xpath", self.camera_xpath).click()
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        self.driver.find_element("xpath", self.Google_drive_xpath).click()
        self.driver.find_element("xpath", self.Dropbox_icon_xpath).click()
        time.sleep(10)

    def Discussion_Submit_button(self):
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()

    def Expand_post(self):
        self.driver.find_element("xpath", self.Expand_post_xpath).click()

    def Collapse_post(self):
        self.driver.find_element("xpath", self.Collapse_post_xpath).click()

    def Open_discussion_prompt_page(self):
        self.driver.find_element("xpath", self.Discussion_post_name_xpath).click()

    def Open_Wall_discussion_prompt_page(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Discussion_post_name_xpath).click()

    def back_to_top(self):
        self.driver.find_element("xpath", self.back_to_top_xpath).click()

    def Back_to_Most_expensive_pizza(self):
        self.driver.find_element("xpath", self.Back_to_Most_expensive_pizza_xpath).click()

    def Expand_reply_test(self):
        Expand_reply_button = self.driver.find_element("xpath", self.Student_Expand_reply_xpath)
        if Expand_reply_button.is_displayed():
            print("Expand reply link is present")
            Expand_reply_button.click()
            time.sleep(10)
        else:
            print("Not present")

    def faculty_post_reply_count(self):
        Expand_reply_button_text = self.driver.find_element("xpath", self.faculty_post_reply_count_xpath).text
        print(Expand_reply_button_text)

    def Expand_all_post(self):
        self.driver.find_element("xpath", self.Expand_all_post_xpath).click()

    def Collapse_all_post(self):
        self.driver.find_element("xpath", self.Collapse_all_post_xpath).click()

    def PostaReply(self):
        self.driver.find_element("xpath", self.faculty_post_a_reply_xpath).click()

    def faculty_reply_on_student_post(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Faculty reply on student post")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(10)
        reply = self.driver.find_element("xpath", "//p[contains(text(),'Faculty reply on student post')]")
        reply_text = self.driver.find_element("xpath", "//p[contains(text(),'Faculty reply on student post')]").text
        if reply.is_displayed():
            print("reply text is visible =  ", reply_text)
        else:
            print("Reply text is not Visible")

    def Open_faculty_discussion_prompt_page(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Discussion_post_name_xpath).click()

    def Student_Expand_reply(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Student_Expand_reply_xpath).click()
        self.driver.find_element("xpath", self.Student_Expand_reply_xpath).click()
        time.sleep(5)

    def Student_reply_button_click(self):
        self.driver.find_element("xpath", self.Student_reply_xpath).click()

    def student_reply_on_faculty_reply(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("student reply on faculty reply")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(15)

    def click_mention_reply_button(self):
        self.driver.find_element("xpath", self.mention_reply_button_xpath).click()

    def mention_reply_by_faculty(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("mention reply by faculty")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(15)

    def Student_reply_on_his_own_post_button(self):
        self.driver.find_element("xpath", self.faculty_post_a_reply_xpath).click()

    def student_reply_on_own_post(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("student reply on his own post")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(20)

####################################################################################################################

    def Faculty_Discussion_title(self):
        now = datetime.now()
        d2 = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.driver.find_element("xpath", self.Discussion_title_xpath).send_keys("Automation Faculty Discussion Post", d2)


    def Faculty_Discussion_content(self):
        today = date.today()
        d2 = today.strftime(" %B %d, %Y")
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Faculty Discussion Post", d2, '\nFaculty Discussion Post ', d2, '\n')
        self.driver.find_element("xpath", self.Bold_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Unordered_list_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nTest Bold & Unordered list")
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element("xpath", self.Bold_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Test Un bold & ordered List")
        time.sleep(2)
        self.driver.find_element("xpath", self.ordered_list_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Italic_test_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nItalic Test")
        time.sleep(2)
        self.driver.find_element("xpath", self.Underline_test_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nUnderline Test")
        time.sleep(2)
        self.driver.find_element("xpath", self.strikeThrough_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nStrikeThrough Test")
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("\nDO & UNDO Test")
        time.sleep(2)
        self.driver.find_element("xpath", self.Undo_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Do_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element("xpath", self.Insert_link_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.link_insert_layer_url_xpath).send_keys("http://Google.com")
        time.sleep(2)
        self.driver.find_element("xpath", self.link_insert_layer_url_xpath).send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element("xpath", self.link_insert_layer_text_xpath).send_keys("Google")
        time.sleep(2)
        self.driver.find_element("xpath", self.Insert_url_button_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.text_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element("xpath", self.Insert_image_link_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Image_by_url_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        time.sleep(2)
        self.driver.find_element("xpath", self.imageInsertByURL_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.text_xpath).click()
        time.sleep(5)
        self.driver.find_element("xpath", self.insert_video_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.paste_in_video_url_xpath).send_keys("https://www.youtube.com/watch?v=NgjERPTaC4Y")
        time.sleep(2)
        self.driver.find_element("xpath", self.videoInsertByURL_xpath).click()
        time.sleep(20)

    def Faculty_Open_discussion_prompt_page(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Faculty_Discussion_post_name_xpath).click()

    def Faculty_Expand_post(self):
        self.driver.find_element("xpath", self.Faculty_Expand_post_xpath).click()

    def Faculty_Collapse_post(self):
        self.driver.find_element("xpath", self.Faculty_Collapse_post_xpath).click()

    def Student_reply_on_Faculty_post(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Student reply on Faculty post")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(20)

    def click_wall(self):
        self.driver.find_element("xpath", self.Wall_xpath).click()

    def Faculty_Expand_reply(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Faculty_Expand_reply_xpath).click()
        self.driver.find_element("xpath", self.Faculty_Expand_reply_xpath).click()
        time.sleep(15)

    def faculty_reply_on_student_reply(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("Faculty reply on Student reply")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(15)

    def mention_reply_by_student(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("mention reply by student")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(15)

    def Faculty_reply_on_own_post(self):
        self.driver.find_element("xpath", self.Discussion_content_xpath).send_keys("faculty reply on his own post")
        self.driver.find_element("xpath", self.direct_link_xpath).click()
        self.driver.find_element("xpath", self.paste_your_link_here_xpath).send_keys('https://media.istockphoto.com/id/1146517111/photo/taj-mahal-mausoleum-in-agra.jpg?s=612x612&w=0&k=20&c=vcIjhwUrNyjoKbGbAQ5sOcEzDUgOfCsm9ySmJ8gNeRk=')
        self.driver.find_element("xpath", self.upload_button_xpath).click()
        time.sleep(10)
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()
        time.sleep(20)

    def verify_Gradebooklink_present(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        Gradebook_Link = self.driver.find_element("xpath", self.Gradebook_link_xpath)
        Gradebook_Link_text = self.driver.find_element("xpath", self.Gradebook_link_xpath).text
        if Gradebook_Link.is_displayed():
             print("Gradebook link is visible =  ", Gradebook_Link_text)
             Gradebook_Link.click()
        else:
             print("Gradebook link is not Visible")

    def Student_Profile_label(self):
        self.driver.find_element("xpath", self.Student_Profile_label_xpath).click()
        time.sleep(10)
        student_name = self.driver.find_element("xpath", "//button[@aria-label='Profile Menu']//div//img").get_attribute("alt")
        print(student_name)


    def select_student_publish_score(self):
        self.driver.find_element("xpath", self.student_name_xpath).click()
        time.sleep(3)
        self.driver.find_element("xpath", self.Unpublish_button_xpath).click()
        time.sleep(4)
        self.driver.find_element("xpath", self.score_text_xpath).clear()
        time.sleep(3)
        self.driver.find_element("xpath", self.score_text_xpath).send_keys("78")
        time.sleep(3)
        today = date.today()
        d2 = today.strftime(" %B %d, %Y")
        self.driver.find_element("xpath", '//div[@class="fr-element fr-view"]//p').click()
        time.sleep(1)
        self.driver.find_element("xpath", self.faculty_feedback_xpath).send_keys("Faculty Feedback", d2)
        time.sleep(1)
        self.driver.find_element("xpath", '//div[@class="focus container"]').click()
        time.sleep(5)
        self.driver.find_element("xpath", self.publish_button_xpath).click()


    def Student_Gradelink(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        Grade_Link = self.driver.find_element("xpath", self.Grade_link_xpath)
        Grade_Link_text = self.driver.find_element("xpath", self.Grade_link_xpath).text
        if Grade_Link.is_displayed():
             print("Grade link is visible =  ", Grade_Link_text)
             Grade_Link.click()
        else:
             print("Grade link is not Visible")

    def Faculty_discussion_prompt_page(self):
        self.driver.find_element("xpath", self.Faculty_Discussion_post_name_xpath).click()

    def Edit_faculty_post(self):
        #self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Edit_faculty_post_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.Discussion_title_xpath).send_keys("Edited")
        self.driver.find_element("xpath", self.Discussion_submit_button2).click()

    def Delete_faculty_post(self):
        self.driver.find_element("xpath", self.Delete_faculty_post_xpath).click()
        self.driver.find_element("xpath", self.Delete_continue_button_xpath).click()

    def Delete_student_post(self):
        self.driver.find_element("xpath", self.Delete_student_post_xpath).click()
        self.driver.find_element("xpath", self.Delete_continue_button_xpath).click()

    def faculty_edit_own_reply(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        self.driver.find_element("xpath", self.Faculty_Discussion_post_name_xpath).click()
        time.sleep(2)
        self.driver.find_element("xpath", self.faculty_edit_own_reply_xpath).click()
        self.driver.find_element("xpath", self.text_xpath).send_keys(" edited")
        self.driver.find_element("xpath", self.Discussion_submit_button_xpath).click()

    def faculty_delete_own_reply(self):
        self.driver.find_element("xpath", self.faculty_delete_own_reply_xpath).click()
        self.driver.find_element("xpath", self.Delete_continue_button_xpath).click()

    def faculty_delete_student_reply(self):
        self.driver.find_element("xpath", self.faculty_delete_student_reply_xpath).click()
        self.driver.find_element("xpath", self.Delete_continue_button_xpath).click()

    def click_Create_New_Wall_Post(self):
        self.driver.switch_to.frame(self.driver.find_element("xpath", self.iframe_xpath))
        Create_a_new_post_text = self.driver.find_element("xpath", self.Create_New_Post_xpath).text
        print(Create_a_new_post_text)
        Create_a_new_post = self.driver.find_element("xpath", self.Create_New_Post_xpath)
        if Create_a_new_post.is_displayed():
            print("Create a new post button is present")
            Create_a_new_post.click()
        else:
            print("Create a new post button is Not present")

    def click_Social_group(self):
        self.driver.find_element("xpath", self.Social_group_xpath).click()

    def Click_Start_SG(self):
        self.driver.find_element("xpath", self.Start_SG_xpath).click()

    def Add_GroupName(self):
        self.driver.find_element("xpath", self.Add_GroupName_xpath).send_keys("SG-28th-9-2023")

    def Add_shortName(self):
        self.driver.find_element("xpath", self.Add_shortName_xpath).send_keys("SG-28th-9-2023")

    def About_Group(self):
        self.driver.find_element("xpath", self.About_Group_xpath).send_keys("Programming Group")

    def Whoshouldjoin(self):
        self.driver.find_element("xpath", self.Whoshouldjoin_xpath).send_keys("Student,Teacher")

    def Add_Topics(self):
        self.driver.find_element("xpath", self.Topic1_xpath).send_keys("C")
        self.driver.find_element("xpath", self.Topic2_xpath).send_keys("C++")

    def Check_private(self):
        self.driver.find_element("xpath", self.Check_private_xpath).click()

    def Check_Invites(self):
        self.driver.find_element("xpath", self.Check_Invites_xpath).click()

    def Save_changes_button(self):
        self.driver.find_element("xpath", self.Save_changes_button_xpath).click()










