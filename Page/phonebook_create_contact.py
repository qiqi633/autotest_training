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
# import importlib
# import sys
# importlib.reload(sys)
from Base.test_POP import Base
import page

#继承Base父类，子类直接调用Base父类的方法
class create_contact(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.xinjian = page.xinjian
        self.xinming = page.xinming
        self.fanhui = page.fanhui
        self.fangqi = page.fangqi
        #self.base_obj=Base(driver)

    # def creat_test(self,text):
    #     self.base_obj.click_element(self.xinjian)
    #     self.base_obj.input_element(self.xinming,text)
    #     self.base_obj.click_element(self.fanhui)
    #     self.base_obj.click_element(self.fangqi)
    def creat_test(self,text):
        self.click_element(self.xinjian)
        self.input_element(self.xinming,text)
        self.click_element(self.fanhui)
        self.click_element(self.fangqi)

