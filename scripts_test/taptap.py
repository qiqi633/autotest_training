#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
# from Base.Base import Base
# import Page
# from Page.login import Login
import pytest
import time
import importlib
import sys
importlib.reload(sys)

class Taptap:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'S9B7N17819001588'
        desired_caps['appPackage'] = 'com.taptap'
        desired_caps['appActivity'] = 'com.play.taptap.ui.MainAct'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>setup")
        # self.tap = Login(self.driver)
    def teardown_class(self):
        if self.driver:
            self.driver.quit()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>teardown")
    def tap_test(self):
        print('test message')
        # self.tap.goto_login()
        # # self.tap.register_failture()
        # # self.tap.login_failture()
        # self.tap.change_pwd()
if __name__ =="__main__":
    pytest.main()

