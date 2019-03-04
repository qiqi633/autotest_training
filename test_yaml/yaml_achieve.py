import os,sys
sys.path.append(os.getcwd())
from appium import webdriver
import test_yaml
import base64
from Base.Base import Base
import yaml
import allure
import pytest
import importlib
importlib.reload(sys)
from test_yaml.page_search import Search_page
from initDriver.initDriver import initDriver
from test_yaml.readout import ret_yaml_data
def get_data():
    data_list = []
    data = ret_yaml_data('data').get("Search_Data")
    for i in data:
        data_list.append((i,data[i].get('test')))
    print(data_list)
    return data_list
class search:
    def setup_class(self):
        print("setup>>>>>>>>>>>>>>>>>>>")
        self.driver = initDriver('com.android.settings','.HWSettings')
        self.obj = Search_page(self.driver)
    def teardown_class(self):
        self.driver.quit()
        print(">>>>>>>>>>>>>>>>>>>>>>>>teardown")
    @allure.step(step = "this is allure step")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL )
    @allure.issue("http://www.baidu.com")
    @pytest.allure.testcase('http://www.baidu.com/test_001')
    @pytest.mark.parametrize('test_case_name,test_case_value',get_data())
    def test_fun(self,test_case_name,test_case_value):
        @allure.attach("title","describe detail")
        self.obj.click_search_btn()
        print("test case num :{0},test case value :{1}".format(test_case_name,test_case_value))
        self.obj.search_input(test_case_value)
        self.driver.get_screenshot_as_file('./Screenshots/%s.png'% test_case_name)
        self.obj.search_return()
