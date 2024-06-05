import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class HomePage:
    AboutUs = (By.XPATH, '//li[@class="nav-item dropdown pr-4 level-0"]/a[@href="/about-us"]')
    OurTeam_dropdown_menu = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Our Team"]')
    Mission_dropdown_menu = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Mission, Vision and Values"]')
    studywithus_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Why study with us?"]')
    Acrediation_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Accreditations, Partnerships and Memberships"]')
    Student_Experience_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Student Experience"]')
    Student_Testimonials_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[text()="Student Testimonials"]')


    Programs = (By.XPATH, '//a[@class="nav-link font-bold-18" and @title="Programs"]')
    Technology_ddm = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Technology"]')
    Technology_ddmb = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Technology"]//..//i')
    CRM_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Cybersecurity Risk Management with Co-op"]')
    DEA_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Data Engineering and Analytics with Co-op"]')
    UEID_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="User Experience and Interactive Design with Co-op"]')
    SQA_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Software Quality Assurance Engineering with Co-op"]')
    FWD_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Full-Stack Web Development with Co-op"]')
    IST_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Information Systems Technology"]')


    Business_ddm = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Business"]')
    Business_ddmb = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Business"]//..//i')
    DigitalMarketing_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Digital Marketing with Co-op"]')
    Business_Management_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Business Management with Co-op"]')
    Business_Administration_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Business Administration with Co-op"]')


    Hospitality_ddm = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Hospitality"]')
    Hospitality_ddmb = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Hospitality"]//..//i')
    HTM_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Hospitality and Tourism Management with Co-op"]')
    HTA_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Hospitality and Tourism Administration with Co-op"]')


    Education_ddm = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Continuing Education"]')
    Education_ddmb = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Continuing Education"]//..//i')
    Cybersecurity_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Diploma in Cybersecurity Analyst Practicum"]')


    Pathways_ddm = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Pathways"]')
    Pathways_ddmb = (By.XPATH, '//li[@class="nav-item dropdown angle-toggle"]//a[text()="Pathways"]//..//i')
    EAP_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="EAP (English for Academic Purposes)"]')
    UCW_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="University Canada West (UCW)"]')
    VCC_xpath = (By.XPATH, '//li[@class="dropdown-item"]//a[text()="Vancouver Community College (VCC)"]')


    Admissions = (By.XPATH, '//a[@class="nav-link font-bold-18" and @title="Admissions"]')
    HowtoApply_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="How to Apply"]')
    English_Prof_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="English Proficiency"]')
    Enrolment_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="Enrolment"]')
    Fees_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="Program Fees"]')
    Payment_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="Payment Options"]')
    Scholarships_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="Scholarships"]')
    Policies_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="Policies"]')
    FAQs_ddm = (By.XPATH, '//div[@class="dropdown-menu shadow"]//a[@title="FAQs"]')


    Accommodation = (By.XPATH, '//a[@class="nav-link font-bold-18" and @title="Accommodation"]')
    Location = (By.XPATH, '//a[@class="nav-link font-bold-18" and text()="Location"]')
    ContactUs = (By.XPATH, '//a[@class="nav-link font-bold-18" and text()="Contact Us"]')


    Search_Icon_xpath = (By.XPATH, '//div[@id="searchform"]')
    searchModalClose_xpath = (By.XPATH, '//i[@id="searchModalClose"]')

    Nav_VirtualStudent_items = (By.XPATH, '//li[@class="nav-item spacing"]//a[@title="Virtual Student Lounge"]')
    Nav_Student_exp_items = (By.XPATH, '//li[@class="nav-item spacing"]//a[@title="Student Experience"]')
    Nav_News_blog_items = (By.XPATH, '//li[@class="nav-item spacing"]//a[@title="News & Blog"]')
    Nav_Convocation_items = (By.XPATH, '//li[@class="nav-item spacing"]//a[@title="Convocation"]')
    Nav_Apply_Now = (By.XPATH, '//li[@class="nav-item spacing"]//a[@title="Apply Now"]')

    info_icon = (By.XPATH, '//span[@class="label"]//*[local-name()="svg" and @data-icon="info-circle"]')
    Video_icon = (By.XPATH, '//li[@class="videocall"]')
    id_close = (By.ID, 'close')

    Technology_img = (By.XPATH, "//a[@title='Technology']//div[@class='wrapper']")
    Business_img = (By.XPATH, "//a[@title='Business']//img[@title='Diplomas']")
    Hospitality_img = (By.XPATH, "//a[@title='Hospitality']//img[@title='Diplomas']")

    See_All_Programs = (By.XPATH, "//a[@title='See All Programs']")

    Verify_text = (By.XPATH, '//section[@id="home"]//h3[text()]')
    About_Us_xpath = (By.XPATH, '//div[@class="container"]//a[@href="/about-us" and @title="About Us"]')
    Why_CCTB_xpath = (By.XPATH, '//div[@class="container"]//a[@href="/about-us/why-cctb" and @title="Why CCTB?"]')
    our_faculty_xpath = (By.XPATH, '(//a[@href="/about-us/why-cctb/our-team" and @title="Our Faculty"])[1]')
    Verify_text2_xpath = (By.XPATH, '(//section[@class="home-section"]//h3[text()])[2]')
    Verify_text3_xpath = (By.XPATH, '//section[@class="home-section bg-grey-light"]//h3[text()]')

    first_card_xpath = (By.XPATH, '//div[@data-category="Program"]')
    second_card_xpath = (By.XPATH, '(//div[@data-category="News"])[1]')
    third_card_xpath = (By.XPATH, '//div[@data-category="Career Advice"]')
    fourth_card_xpath = (By.XPATH, '(//div[@data-category="News"])[2]')

    share_card1_xpath = (By.XPATH, '//div[@data-category="Program"]//span//i')
    share_card2_xpath = (By.XPATH, '(//div[@data-category="News"])[1]//span//i')
    share_card3_xpath = (By.XPATH, '//div[@data-category="Career Advice"]//span//i')
    share_card4_xpath = (By.XPATH, '(//div[@data-category="News"])[2]//span//i')

    program_facebook_link_xpath = (By.XPATH, '//div[@data-category="Program"]//div[@class="sharelinks"]//a[@class="facebook"]')
    program_linkedin_link_xpath = (By.XPATH, '//div[@data-category="Program"]//div[@class="sharelinks"]//a[@class="linkedin"]')
    News1_facebook_link_xpath = (By.XPATH, '(//div[@data-category="News"]//div[@class="sharelinks"]//a[@class="facebook"])[1]')
    News1_linkedin_link_xpath = (By.XPATH, '(//div[@data-category="News"]//div[@class="sharelinks"]//a[@class="linkedin"])[1]')
    Carrer_facebook_link_xpath = (By.XPATH, '//div[@data-category="Career Advice"]//div[@class="sharelinks"]//a[@class="facebook"]')
    Carrer_linkedin_link_xpath = (By.XPATH, '//div[@data-category="Career Advice"]//div[@class="sharelinks"]//a[@class="linkedin"]')
    News2_facebook_link_xpath = (By.XPATH, '(//div[@data-category="News"]//div[@class="sharelinks"]//a[@class="facebook"])[2]')
    News2_linkedin_link_xpath = (By.XPATH, '(//div[@data-category="News"]//div[@class="sharelinks"]//a[@class="linkedin"])[2]')

    Explore_news_xpath = (By.XPATH, '//div[@class="d-none d-sm-none d-md-none d-lg-block"]//a[text()="Explore All News"]')

    follow_us_on_text_xpath = (By.XPATH, '//section[@class="home-section"]//h2[text()="Follow us on"]//a')
    Insta_Image_xpath1 = (By.XPATH, '//div[@id="curator-feed-cctb-layout"]//div[contains(@aria-label, "Post 1")]')
    Insta_Image_xpath2 = (By.XPATH, '//div[@id="curator-feed-cctb-layout"]//div[contains(@aria-label, "Post 2")]')
    Insta_Image_xpath3 = (By.XPATH, '//div[@id="curator-feed-cctb-layout"]//div[contains(@aria-label, "Post 3")]')
    Insta_Image_xpath4 = (By.XPATH, '//div[@id="curator-feed-cctb-layout"]//div[contains(@aria-label, "Post 4")]')
    previous_post_xpath = (By.XPATH, '//a[@aria-label="go to previous post"]')
    next_post_xpath = (By.XPATH, '//a[@aria-label="go to next post"]')
    close_popup_xpath = (By.XPATH, "//a[@aria-label='close popup']//*[name()='svg']//*[name()='path' and contains(@transform,'scale(1,-1')]")

    why_CCTB_xpath = (By.XPATH, "//li/a[@title='Why CCTB']")
    programs_xpath = (By.XPATH, '//span[text()="Programs"]')
    Ourfaculty_xpath = (By.XPATH, '//span[text()="Our Faculty"]')
    Student_Testimonials_xpath = (By.XPATH, '//span[text()="Student Testimonials"]')
    footer_Career_xpath = (By.XPATH, '//span[text()="Career"]')
    footer_Policies_xpath = (By.XPATH, '//span[text()="Policies"]')
    footer_Legal_Notices_xpath = (By.XPATH, '//li//span[text()="Legal Notices"]')
    footer_Privacy_Policy_xpath = (By.XPATH, '//li//span[text()="Privacy Policy"]')
    footer_Sitemap_xpath = (By.XPATH, '//li//span[text()="Sitemap"]')

    footer_facebook_link_xpath = (By.XPATH, '//a[@id="f-facebook"]')
    footer_linkedin_link_xpath = (By.XPATH, '//a[@id="f-linkedin"]')
    footer_youtube_link_xpath = (By.XPATH, '//a[@id="f-youtube"]')
    footer_insta_link_xpath = (By.XPATH, '//a[@id="f-instagram"]')
    footer_tiktok_link_xpath = (By.XPATH, '//a[@id="f-tiklok"]')

    copywrite_xpath = (By.XPATH, '//hr[@class="footer-hr"]//..//p[text()]')

    land_acknowledgement_xpath = (By.XPATH, "//div[@class='land-acknowledgement']//h2")
    land_acknowledgement_para_xpath = (By.XPATH, "//div[@class='land-acknowledgement']//p")


















    def __init__(self, driver):
        self.driver = driver

    def click_AboutUs(self):
         return self.driver.find_element(*HomePage.AboutUs)

    def click_Programs(self):
        return self.driver.find_element(*HomePage.Programs)

    def click_Admissions(self):
        return self.driver.find_element(*HomePage.Admissions)

    def click_Accommodation(self):
        return self.driver.find_element(*HomePage.Accommodation)

    def click_Location(self):
        return self.driver.find_element(*HomePage.Location)

    def click_ContactUs(self):
        return self.driver.find_element(*HomePage.ContactUs)

    def hover_AboutUs(self):
        action = ActionChains(self.driver)
        return action.move_to_element(HomePage.click_AboutUs(self))

    def click_Our_team_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.OurTeam_dropdown_menu))

    def click_Mission_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Mission_dropdown_menu))

    def click_study_with_us_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.studywithus_ddm))

    def click_Accrediation_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Acrediation_ddm))

    def click_Student_Experience_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Student_Experience_ddm))

    def click_Student_Testimonials_drop_down_menu(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Student_Testimonials_ddm))

    def hover_Programs(self):
        action = ActionChains(self.driver)
        return action.move_to_element(HomePage.click_Programs(self))

    def click_Technology_ddm(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Technology_ddm))

    def click_Business_ddm(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Business_ddm))

    def click_Hospitality_ddm(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Hospitality_ddm))

    def click_Education_ddm(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Education_ddm))

    def click_Pathways_ddm(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Pathways_ddm))


    def click_Technology_ddmb(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Technology_ddmb))

    def click_CRM(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.CRM_xpath))
        # return self.driver.find_element(*HomePage.CRM_xpath)

    def click_DEA(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.DEA_xpath))

    def click_UEID(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.UEID_xpath))

    def click_SQA(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.SQA_xpath))

    def click_FWD(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.FWD_xpath))

    def click_IST(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.IST_xpath))

    def click_Business_ddmb(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Business_ddmb))


    def click_DigitalMarketing(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.DigitalMarketing_xpath))

    def click_Business_Management(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Business_Management_xpath))

    def click_Business_Administration(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Business_Administration_xpath))


    def click_Hospitality_ddmb(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Hospitality_ddmb))


    def click_HTM(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.HTM_xpath))

    def click_HTA(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.HTA_xpath))

    def click_Continuous_Edu_ddmb(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Education_ddmb))


    def click_Cybersecurity(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Cybersecurity_xpath))

    def click_Pathways_ddmb(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Pathways_ddmb))


    def click_EAP(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.EAP_xpath))

    def click_UCW(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.UCW_xpath))

    def click_VCC(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.VCC_xpath))

    def hover_Admissions(self):
        action = ActionChains(self.driver)
        return action.move_to_element(HomePage.click_Admissions(self))

    def Click_How_to_Apply(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.HowtoApply_ddm))

    def Click_English_prof(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.English_Prof_ddm))

    def Click_Enrolment(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Enrolment_ddm))

    def Click_Program_fees(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Fees_ddm))

    def Click_Payment(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Payment_ddm))

    def Click_Scholarships(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Scholarships_ddm))

    def Click_Policies(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.Policies_ddm))

    def Click_FAQs(self):
        action = ActionChains(self.driver)
        return action.move_to_element(self.driver.find_element(*HomePage.FAQs_ddm))

    def Click_searchIcon(self):
        return self.driver.find_element(*HomePage.Search_Icon_xpath)

    def Click_searchModalClose(self):
        return self.driver.find_element(*HomePage.searchModalClose_xpath)

    def click_Virtual_student(self):
        return self.driver.find_element(*HomePage.Nav_VirtualStudent_items)

    def click_Nav_Student_exp_items(self):
        return self.driver.find_element(*HomePage.Nav_Student_exp_items)

    def click_Nav_News_blog_items(self):
        return self.driver.find_element(*HomePage.Nav_News_blog_items)

    def click_Nav_Convocation_items(self):
        return self.driver.find_element(*HomePage.Nav_Convocation_items)

    def click_Nav_Apply_Now(self):
        return self.driver.find_element(*HomePage.Nav_Apply_Now)

    def click_info_icon(self):
        return self.driver.find_element(*HomePage.info_icon)

    def click_id_close(self):
        return self.driver.find_element(*HomePage.id_close)

    def click_video_icon(self):
        return self.driver.find_element(*HomePage.Video_icon)

    def click_Technology_img(self):
        return self.driver.find_element(*HomePage.Technology_img)

    def click_Business_img(self):
        return self.driver.find_element(*HomePage.Business_img)

    def click_Hospitality_img(self):
        return self.driver.find_element(*HomePage.Hospitality_img)

    def click_See_All_Programs(self):
        return self.driver.find_element(*HomePage.See_All_Programs)

    def verify_text_present(self):
        store = self.driver.find_element(*HomePage.Verify_text).text
        return store

    def click_About_Us_pic(self):
        return self.driver.find_element(*HomePage.About_Us_xpath)

    def click_Why_CCTB_pic(self):
        return self.driver.find_element(*HomePage.Why_CCTB_xpath)

    def click_our_faculty_pic(self):
        return self.driver.find_element(*HomePage.our_faculty_xpath)

    def Verify_text2(self):
        store = self.driver.find_element(*HomePage.Verify_text2_xpath).text
        return store

    def Verify_text3(self):
        store = self.driver.find_element(*HomePage.Verify_text3_xpath).text
        return store

    def click_first_card(self):
        return self.driver.find_element(*HomePage.first_card_xpath)

    def click_second_card(self):
        return self.driver.find_element(*HomePage.second_card_xpath)

    def click_third_card(self):
        return self.driver.find_element(*HomePage.third_card_xpath)

    def click_fourth_card(self):
        return self.driver.find_element(*HomePage.fourth_card_xpath)

    def click_share_card1(self):
        return self.driver.find_element(*HomePage.share_card1_xpath)

    def click_fb_card1(self):
        return self.driver.find_element(*HomePage.program_facebook_link_xpath)

    def click_linkedin_card1(self):
        return self.driver.find_element(*HomePage.program_linkedin_link_xpath)

    def click_share_card2(self):
        return self.driver.find_element(*HomePage.share_card2_xpath)

    def click_fb_card2(self):
        return self.driver.find_element(*HomePage.News1_facebook_link_xpath)

    def click_linkedin_card2(self):
        return self.driver.find_element(*HomePage.News1_linkedin_link_xpath)

    def click_share_card3(self):
        return self.driver.find_element(*HomePage.share_card3_xpath)

    def click_fb_card3(self):
        return self.driver.find_element(*HomePage.Carrer_facebook_link_xpath)

    def click_linkedin_card3(self):
        return self.driver.find_element(*HomePage.Carrer_linkedin_link_xpath)

    def click_share_card4(self):
        return self.driver.find_element(*HomePage.share_card4_xpath)

    def click_fb_card4(self):
        return self.driver.find_element(*HomePage.News2_facebook_link_xpath)

    def click_linkedin_card4(self):
        return self.driver.find_element(*HomePage.News2_linkedin_link_xpath)

    def click_explore_news(self):
        return self.driver.find_element(*HomePage.Explore_news_xpath)

    def click_follow_us_on_text(self):
        return self.driver.find_element(*HomePage.follow_us_on_text_xpath)

    def click_Insta_Image1(self):
        return self.driver.find_element(*HomePage.Insta_Image_xpath1)

    def click_Insta_Image2(self):
        return self.driver.find_element(*HomePage.Insta_Image_xpath2)

    def click_Insta_Image3(self):
        return self.driver.find_element(*HomePage.Insta_Image_xpath3)

    def click_Insta_Image4(self):
        return self.driver.find_element(*HomePage.Insta_Image_xpath4)

    def click_prenextclose_post(self):
        time.sleep(3)
        self.driver.find_element(*HomePage.previous_post_xpath).click()
        time.sleep(3)
        self.driver.find_element(*HomePage.next_post_xpath).click()
        time.sleep(3)
        self.driver.find_element(*HomePage.close_popup_xpath).click()

    def click_why_CCTB(self):
        return self.driver.find_element(*HomePage.why_CCTB_xpath)

    def click_footer_Programs(self):
        return self.driver.find_element(*HomePage.programs_xpath)

    def click_footer_Ourfaculty(self):
        return self.driver.find_element(*HomePage.Ourfaculty_xpath)

    def click_footer_Student_Testimonials(self):
        return self.driver.find_element(*HomePage.Student_Testimonials_xpath)

    def click_footer_Career(self):
        return self.driver.find_element(*HomePage.footer_Career_xpath)

    def click_footer_Policies(self):
        return self.driver.find_element(*HomePage.footer_Policies_xpath)

    def click_footer_Legal_Notices(self):
        return self.driver.find_element(*HomePage.footer_Legal_Notices_xpath)

    def click_footer_Privacy_Policy(self):
        return self.driver.find_element(*HomePage.footer_Privacy_Policy_xpath)

    def click_footer_Sitemap(self):
        return self.driver.find_element(*HomePage.footer_Sitemap_xpath)

    def click_footer_facebook_link(self):
        return self.driver.find_element(*HomePage.footer_facebook_link_xpath)

    def click_footer_linkedin_link(self):
        return self.driver.find_element(*HomePage.footer_linkedin_link_xpath)

    def click_footer_youtube_link(self):
        return self.driver.find_element(*HomePage.footer_youtube_link_xpath)

    def click_footer_instagram_link(self):
        return self.driver.find_element(*HomePage.footer_insta_link_xpath)

    def click_footer_tiktok_link(self):
        return self.driver.find_element(*HomePage.footer_tiktok_link_xpath)

    def verify_copyrite_text(self):
        return self.driver.find_element(*HomePage.copywrite_xpath)

    def verify_land_acknowledgement_text(self):
        return self.driver.find_element(*HomePage.land_acknowledgement_xpath)

    def verify_land_acknowledgement_para_text(self):
        return self.driver.find_element(*HomePage.land_acknowledgement_para_xpath)





















