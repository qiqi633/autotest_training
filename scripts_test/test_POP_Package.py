#!/usr/bin/python
#coding:utf-8
import importlib
import sys
importlib.reload(sys)
from Base.test_POP import Base
from appium import webdriver
from selenium.webdriver.common.by import By
import time
class Test_search:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'S9B7N17819001588'
        desired_caps['appPackage'] = 'com.android.contacts'  # 手机启动包名
        desired_caps['appActivity'] = '.activities.PeopleActivity'  # 启动名
        # 以下两个变量，可以在输入框中输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 调起appium工具，会自动打开/重启app
        #初始化base实实例
        self.base_obj=Base(self.driver)
    def teardown_class(self):
        self.driver.quit()
    def test_001(self):
        # 使用webdriverwait保证健壮性，直接使用find_element可能会找不到数据,*xinjian是解包的意思
        xinjian=(By.XPATH,"//*[contains(@text,'新建联系人')]")
        self.base_obj.click_element(xinjian)
        xinming=(By.XPATH,"//*[contains(@text,'姓名')]")
        data = '123'
        self.base_obj.input_element(xinming,data)
        time.sleep(3)

