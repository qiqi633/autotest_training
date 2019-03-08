#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import string
import pytest
from Page.phonebook_create_contact import create_contact
class Test_create:
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
        self.create_obj=create_contact(self.driver)
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize("text",[1,2,3])
    def test_create(self,text):
        self.create_obj.creat_test(text)

