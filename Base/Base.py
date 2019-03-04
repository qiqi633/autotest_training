#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
import importlib
import sys
importlib.reload(sys)
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import pytest
class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_element_x(self,loc,timeout = 20,poll = 1):
        """
        :param loc: 键值对，元素定位方式，和元素值（By.ID,'VALUE'）
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))
        # return self.driver.find_element(*loc)
    def click_element(self,loc):
        self.find_element_x(loc).click()
    def input_element(self,loc,text):
        self.find_element_x(loc).send_keys(text)
    def long_press_element(self,loc):
        button = self.find_element_x(loc)
        TouchActions(self.driver).long_press(button,2000).release().perform()





