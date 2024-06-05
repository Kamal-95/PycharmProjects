import time

import pytest
from selenium.common import NoSuchElementException

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestHomePage(BaseClass):


    def test_AboutUsNav(self):
        homepage = HomePage(self.driver)
        homepage.click_AboutUs().click()
        AboutUs_title = self.driver.title
        assert AboutUs_title == "About CCTB - Canadian College of Technology and Business"
        homepage.hover_AboutUs().perform()
        homepage.click_Our_team_drop_down_menu().click().perform()
        homepage.hover_AboutUs().perform()
        homepage.click_Mission_drop_down_menu().click().perform()
        homepage.hover_AboutUs().perform()
        homepage.click_study_with_us_drop_down_menu().click().perform()
        homepage.hover_AboutUs().perform()
        homepage.click_Accrediation_drop_down_menu().click().perform()
        homepage.hover_AboutUs().perform()
        homepage.click_Student_Experience_drop_down_menu().click().perform()
        homepage.hover_AboutUs().perform()
        homepage.click_Student_Testimonials_drop_down_menu().click().perform()
        time.sleep(2)

    def test_ProgramsNav(self):
        homepage = HomePage(self.driver)
        homepage.click_Programs().click()
        Programs_title = self.driver.title
        assert Programs_title == "Diploma Programs in Vancouver, Canada | CCTB"
        homepage.hover_Programs().perform()
        homepage.click_Technology_ddm().click().perform()
        homepage.hover_Programs().perform()
        homepage.click_Business_ddm().click().perform()
        homepage.hover_Programs().perform()
        homepage.click_Hospitality_ddm().click().perform()
        homepage.hover_Programs().perform()
        homepage.click_Education_ddm().click().perform()
        homepage.hover_Programs().perform()
        homepage.click_Pathways_ddm().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_CRM().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_DEA().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_UEID().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_SQA().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_FWD().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Technology_ddmb().click().perform()
        homepage.click_IST().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Business_ddmb().click().perform()
        homepage.click_DigitalMarketing().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Business_ddmb().click().perform()
        homepage.click_Business_Management().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Business_ddmb().click().perform()
        homepage.click_Business_Administration().click().perform()


        homepage.hover_Programs().perform()
        homepage.click_Hospitality_ddmb().click().perform()
        homepage.click_HTM().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Hospitality_ddmb().click().perform()
        homepage.click_HTA().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Continuous_Edu_ddmb().click().perform()
        homepage.click_Cybersecurity().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Pathways_ddmb().click().perform()
        homepage.click_EAP().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Pathways_ddmb().click().perform()
        homepage.click_UCW().click().perform()

        homepage.hover_Programs().perform()
        homepage.click_Pathways_ddmb().click().perform()
        homepage.click_VCC().click().perform()

        time.sleep(2)


    def test_AdmissionsNav(self):
        homepage = HomePage(self.driver)
        homepage.click_Admissions().click()
        Admissions_title = self.driver.title
        assert Admissions_title == "Admissions | Canadian College of Technology and Business"
        homepage.hover_Admissions().perform()
        homepage.Click_How_to_Apply().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_English_prof().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_Enrolment().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_Program_fees().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_Payment().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_Scholarships().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_Policies().click().perform()
        homepage.hover_Admissions().perform()
        homepage.Click_FAQs().click().perform()
        time.sleep(2)

    def test_AccommodationNav(self):
        homepage = HomePage(self.driver)
        homepage.click_Accommodation().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        Accommodation_title = self.driver.title
        assert Accommodation_title == "Canadian College of Technology and Business | Off Campus Housing & Student Apartments Search"
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

    def test_LocationNav(self):
        homepage = HomePage(self.driver)
        homepage.click_Location().click()
        Location_title = self.driver.title
        assert Location_title == "Why Choose Vancouver to study in Canada | CCTB"
        time.sleep(3)

    def test_ContactUsNav(self):
        homepage = HomePage(self.driver)
        homepage.click_ContactUs().click()
        ContactUs_title = self.driver.title
        assert ContactUs_title == "Contact CCTB - Canadian College of Technology and Business"
        time.sleep(2)


    def test_SearchBar(self):
        homepage = HomePage(self.driver)
        homepage.Click_searchIcon().click()
        time.sleep(2)
        homepage.Click_searchModalClose().click()
        time.sleep(2)

    def test_VirtualStudent(self):
        homepage = HomePage(self.driver)
        homepage.click_Virtual_student().click()
        time.sleep(2)

    def test_StudentExp(self):
        homepage = HomePage(self.driver)
        homepage.click_Nav_Student_exp_items().click()
        time.sleep(2)

    def test_NewsBlogs(self):
        homepage = HomePage(self.driver)
        homepage.click_Nav_News_blog_items().click()
        time.sleep(2)

    def test_Convocations(self):
        homepage = HomePage(self.driver)
        homepage.click_Nav_Convocation_items().click()
        self.driver.get("https://www.canadianctb.ca/")
        time.sleep(2)


    def test_Apply_Now(self):
        homepage = HomePage(self.driver)
        homepage.click_Nav_Apply_Now().click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)

    def test_info_icon(self):
        homepage = HomePage(self.driver)
        homepage.click_info_icon().click()
        time.sleep(3)
        homepage.click_id_close().click()
        time.sleep(2)

    @pytest.mark.xfail
    def test_video_icon(self):
        homepage = HomePage(self.driver)
        homepage.click_video_icon().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(10)
        self.driver.close()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_Technology_img(self):
        homepage = HomePage(self.driver)
        homepage.click_Technology_img().click()
        self.driver.back()

    def test_Business_img(self):
        homepage = HomePage(self.driver)
        homepage.click_Business_img().click()
        self.driver.back()

    def test_hospitality_img(self):
        homepage = HomePage(self.driver)
        homepage.click_Hospitality_img().click()
        self.driver.back()

    def test_See_All_Programs(self):
        homepage = HomePage(self.driver)
        homepage.click_See_All_Programs().click()
        self.driver.back()
        self.driver.implicitly_wait(3)

    def test_text_present(self):
        homepage = HomePage(self.driver)
        text = homepage.verify_text_present()
        print(text)
        assert "Why study at CCTB" in text
        time.sleep(5)

    def test_About_Us_pic(self):
        homepage = HomePage(self.driver)
        homepage.click_About_Us_pic().click()
        self.driver.back()

    def test_click_Why_CCTB(self):
        homepage = HomePage(self.driver)
        homepage.click_Why_CCTB_pic().click()
        self.driver.back()

    def test_click_our_faculty(self):
        homepage = HomePage(self.driver)
        homepage.click_our_faculty_pic().click()
        self.driver.back()

    def test_text2_present(self):
        homepage = HomePage(self.driver)
        text = homepage.Verify_text2()
        print(text)
        assert "Learn more about CCTB" in text
        time.sleep(5)

    def test_text3_present(self):
        homepage = HomePage(self.driver)
        text = homepage.Verify_text3()
        print(text)
        assert "News & Blog" in text
        time.sleep(5)


    def test_card1(self):
        homepage = HomePage(self.driver)
        homepage.click_first_card().click()
        card1_title = self.driver.title
        assert "Engineering Data Management: A Comprehensive Guide | CCTB" in card1_title
        print(card1_title)
        self.driver.back()


    def test_card2(self):
        homepage = HomePage(self.driver)
        homepage.click_second_card().click()
        card2_title = self.driver.title
        assert "CCTB announces new GUS Canada Colleges Pathway Scholarship" in card2_title
        print(card2_title)
        self.driver.back()


    def test_card3(self):
        homepage = HomePage(self.driver)
        homepage.click_third_card().click()
        card3_title = self.driver.title
        assert "How to Balance Your Academic and Personal Life" in card3_title
        print(card3_title)
        self.driver.back()


    def test_card4(self):
        homepage = HomePage(self.driver)
        homepage.click_fourth_card().click()
        card4_title = self.driver.title
        assert "Understanding the Basics of AI and Machine Learning" in card4_title
        print(card4_title)
        self.driver.back()


    def test_click_share_card1(self):
        homepage = HomePage(self.driver)
        # self.driver.execute_script('window.scrollBy(0, 2800)')
        time.sleep(3)
        homepage.click_share_card1().click()
        homepage.click_fb_card1().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        homepage.click_linkedin_card1().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)


    def test_click_share_card2(self):
        homepage = HomePage(self.driver)
        time.sleep(3)
        homepage.click_share_card2().click()
        homepage.click_fb_card2().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        homepage.click_linkedin_card2().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)



    def test_click_share_card3(self):
        homepage = HomePage(self.driver)
        time.sleep(3)
        homepage.click_share_card3().click()
        homepage.click_fb_card3().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        homepage.click_linkedin_card3().click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)


    def test_click_share_card4(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 100)')
        # self.driver.execute_script('window.scrollBy(0, 2800)')
        homepage.click_share_card4().click()
        homepage.click_fb_card4().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        facebook_title = self.driver.title
        assert "Canadian College of Technology and Business | Vancouver BC | Facebook" in facebook_title
        print(facebook_title)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        homepage.click_linkedin_card4().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        linkedin_title = self.driver.title
        assert "Canadian College of Technology and Business (CCTB) | LinkedIn" in linkedin_title
        print(linkedin_title)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



    def test_explore_news_button(self):
        homepage = HomePage(self.driver)
        # self.driver.execute_script('window.scrollBy(0, 3000)')
        homepage.click_explore_news().click()
        get_title = self.driver.title
        assert "Blog and News - Canadian College of Technology and Business" in get_title
        print("Page Successfully loaded:\t" + get_title)
        self.driver.back()

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_Instagram_link(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 3200)')
        homepage.click_follow_us_on_text().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(
            (By.XPATH, "/html/head/title")))
        Instagram_link = self.driver.title
        assert "Canadian College of Technology and Business (@canadian_ctb) • Instagram photos and videos" in Instagram_link
        print(Instagram_link)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



    def test_click_Insta_Image(self):
        homepage = HomePage(self.driver)
        homepage.click_Insta_Image1().click()
        homepage.click_prenextclose_post()
        homepage.click_Insta_Image2().click()
        homepage.click_prenextclose_post()
        homepage.click_Insta_Image3().click()
        homepage.click_prenextclose_post()
        homepage.click_Insta_Image4().click()
        homepage.click_prenextclose_post()
        time.sleep(2)




    def test_click_why_CCTB(self):
        homepage = HomePage(self.driver)
        target_element = homepage.click_why_CCTB()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)
        # self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_why_CCTB().text
        assert "Why CCTB" in text
        homepage.click_why_CCTB().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Why CCTB? | Reasons to choose CCTB to enhance your skills" in page_title
        print("Page Title:\t"+page_title)
        print("CCTB Page is loaded Successfully!!")


    def test_click_Programs(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Programs().text
        assert "Programs" in text
        homepage.click_footer_Programs().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Diploma Programs in Vancouver, Canada | CCTB" in page_title
        print("Page Title:\t"+page_title)
        print("Programs Page is loaded Successfully!!")


    def test_click_OurFaculty(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Ourfaculty().text
        assert "Our Faculty" in text
        homepage.click_footer_Ourfaculty().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Faculty and Team | Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Our Faculty Page is loaded Successfully!!")


    def test_click_Student_Testimonials(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Student_Testimonials().text
        assert "Student Testimonials" in text
        homepage.click_footer_Student_Testimonials().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Student Testimonials | Students Success Stories | CCTB" in page_title
        print("Page Title:\t"+page_title)
        print("Student Testimonials Page is loaded Successfully!!")


    def test_click_Career(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Career().text
        assert "Career" in text
        homepage.click_footer_Career().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Career | Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Career Page is loaded Successfully!!")


    def test_click_Policies(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Policies().text
        assert "Policies" in text
        homepage.click_footer_Policies().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Policies | Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Policies Page is loaded Successfully!!")


    def test_click_Legal_Notices(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Legal_Notices().text
        assert "Legal Notices" in text
        homepage.click_footer_Legal_Notices().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Legal Notices | Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Legal Notices Page is loaded Successfully!!")


    def test_click_Privacy_Policy(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Privacy_Policy().text
        assert "Privacy Policy" in text
        homepage.click_footer_Privacy_Policy().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Privacy Policy | Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Privacy Policy Page is loaded Successfully!!")


    def test_click_Sitemap(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_Sitemap().text
        assert "Sitemap" in text
        homepage.click_footer_Sitemap().click()
        print("Clicked Successfully!!")
        page_title = self.driver.title
        assert "Canadian College of Technology and Business" in page_title
        print("Page Title:\t"+page_title)
        print("Sitemap Page is loaded Successfully!!")



    def test_click_Facebook(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_facebook_link().get_attribute("class")
        print(text)
        assert "facebook" in text
        homepage.click_footer_facebook_link().click()
        print("Clicked Successfully!!")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="facebook"]/head/title')))
        page_title = self.driver.title
        print(page_title)
        assert 'Canadian College of Technology and Business | Vancouver BC | Facebook' in page_title
        print("Page Title:\t"+page_title)
        print("Facebook Page is loaded Successfully!!")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



    def test_click_Linkedin(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_linkedin_link().get_attribute("id")
        print(text)
        assert "f-linkedin" in text
        homepage.click_footer_linkedin_link().click()
        print("Clicked Successfully!!")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/head/title')))
        page_title = self.driver.title
        print(page_title)
        assert 'Canadian College of Technology and Business (CCTB) | LinkedIn' in page_title
        print("Page Title:\t"+page_title)
        print("LinkedIn Page is loaded Successfully!!")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    @pytest.mark.xfail
    def test_click_youtube(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_youtube_link().get_attribute("id")
        print(text)
        assert "f-youtube" in text
        homepage.click_footer_youtube_link().click()
        print("Clicked Successfully!!")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/title')))
        # time.sleep(5)
        page_title = self.driver.title
        print(page_title)
        assert 'Canadian College of Technology and Business - CCTB - YouTube' in page_title
        print("Page Title:\t"+page_title)
        print("YouTube Page is loaded Successfully!!")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def test_click_instagram(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_instagram_link().get_attribute("class")
        print(text)
        assert "instagram" in text
        homepage.click_footer_instagram_link().click()
        print("Clicked Successfully!!")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/head/title')))
        page_title = self.driver.title
        print(page_title)
        assert 'Canadian College of Technology and Business (@canadian_ctb) • Instagram photos and videos' in page_title
        print("Page Title:\t"+page_title)
        print("Instagram Page is loaded Successfully!!")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])




    def test_click_tiktok(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text = homepage.click_footer_tiktok_link().get_attribute("id")
        print(text)
        assert "f-tiklok" in text
        homepage.click_footer_tiktok_link().click()
        print("Clicked Successfully!!")
        self.driver.switch_to.window(self.driver.window_handles[1])
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/head/title')))
        page_title = self.driver.title
        print(page_title)
        assert 'TikTok' in page_title
        print("Page Title:\t"+page_title)
        print("TikTok Page is loaded Successfully!!")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])




    def test_copyrite_text(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text1 = homepage.verify_copyrite_text().text
        assert "© 2024 Canadian College of Technology & Business (CCTB)" in text1
        print(text1)


    def test_land_acknowledgement_text(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text2 = homepage.verify_land_acknowledgement_text().text
        assert "Land" in text2
        print(text2)

    @pytest.mark.skip
    def test_land_acknowledgement_para_text(self):
        homepage = HomePage(self.driver)
        self.driver.execute_script('window.scrollBy(0, 5000)')
        text3 = homepage.verify_land_acknowledgement_para_text().text
        assert "xʷməθkʷəy̓əm (Musqueam), Sḵwx̱wú7mesh (Squamish) and Sel̓íl̓witulh (Tsleil-Waututh) Nations" in text3
        print(text3)