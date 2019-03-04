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

#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import importlib
import sys
importlib.reload(sys)
from Base.test_POP import Base

class create_contact:
    def __init__(self,driver):
        self.dCT = (By.XPATH, "//*[contains(@text,'dCT')]")
        self.action_button = (By.ID, "com.android.contacts:id/primary_action_button")
        self.input_text_view = (By.XPATH,"//*[contains(@text,'输入信息')]")
        self.click_send_sms = (By.ID,"com.android.mms:id/send_button_sms")
        self.base_obj=Base(driver)
    def creat_test(self,text):
        self.base_obj.click_element(self.dCT)
        self.base_obj.click_element(self.action_button)
        self.base_obj.input_element(self.input_text_view,text)
        self.base_obj.click_element(self.click_send_sms)



