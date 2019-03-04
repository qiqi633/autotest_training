from appium import webdriver
import test_yaml
from Base.Base import Base
class Search_page():
    def __init__(self,driver):
        self.obj = Base(driver)
        print("search page check point,after Base init")
        self.driver = driver
        print("search page check point,after self.driver")
    def click_search_btn(self):
        self.obj.click_element(test_yaml.search_txt)
    def search_input(self,text):
        self.obj.input_element(test_yaml.search_btn,text)
    def search_return(self):
        self.obj.click_element(test_yaml.search_rtn)
