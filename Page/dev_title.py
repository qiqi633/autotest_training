from Base.Base import Base
import Page
class Dev_Title(Base):
    def __init__(self,driver):
        Base.__init__(self.driver)
    def click_add(self):
        self.click_element(Page.DEV_mian_login)
    def chang_login(self):
        self.click_element(Page.DEV_login_email)
    def email_login(self,email,pwd):
        self.input_element(Page.DEV_email_count, email)
        self.input_element(Page.DEV_email_pwd, pwd)
        self.click_element(Page.DEV_email_conf)