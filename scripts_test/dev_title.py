#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import pytest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from Page.dev_title import Dev_Title

class Dev_title:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'S9B7N17819001588'
        desired_caps['appPackage'] = 'io.manong.developerdaily'
        desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
        #android包的export 属性设置为false 则不能通过adb启动
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print(">>>>>>>>>>>>>>>>>>>>>setup")
        self.obj = Dev_Title(self.driver)
    @pytest.fixture()
    def start_setup(self):
        self.obj.click_add()
        self.obj.chang_login()
    def teardown_class(self):
        print(">>>>>>>>>>>>>>>>>>>>>teardown")
        self.driver.quit()
    @pytest.mark.usefixtures("start_setup")
    @pytest.mark.parametrize("email,pwd",[('123','jdfsjs'),('1@q',''),('630345353@qq.com','111111')])
    def test_login(self,email,pwd):
        print(">>>>>>>>>>>>>>>>>>>>>login")
        self.obj.email_login(email,pwd)
        self.driver.get_screenshot_as_file('./Screenshots/email_login.png')

