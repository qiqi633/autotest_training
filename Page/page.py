from Page.dev_title import Dev_Title
from Page.login import Login
from Page.phonebook_create_contact import create_contact

class Page_Obj:
    def __init__(self,driver):
        self.driver =driver
    def Dev_T(self):
        return Dev_Title(self.driver)
    def Login_T(self):
        return Login(self.driver)
    def phonebook(self):
        return create_contact(self.driver)
