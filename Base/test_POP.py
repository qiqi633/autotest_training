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
class Base:
    def __init__(self,driver):
        self.driver = driver
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.0'
        # desired_caps['deviceName'] = 'S9B7N17819001588'
        # desired_caps['appPackage'] = 'com.android.contacts'  # 手机启动包名
        # desired_caps['appActivity'] = '.activities.PeopleActivity'  # 启动名
        # # 以下两个变量，可以在输入框中输入中文
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        #
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 调起appium工具，会自动打开/重启app

    # driver.find_element_by_id("xxx").click()
    #driver.find_element_by_xpath("//*[contains(@text,'新建联系人')]").click()
    # def find_element(self,loc,loc_value,timeout=5,poll=1):
    #     """
    #     :param loc: 定位方式，类似于,By.XPATH,By.ID，By.CLASS_NAME
    #     :param loc_value: loc的值，比如id的值
    #     :return:
    #     """
    #     return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(loc,loc_value))

    #使用元组方式传参
    def find_element(self,loc,timeout=5,poll=1):
        """
        :param loc: 定位方式+属性值，是一个元组类型，类似于（By.XPATH,"XPATH值"）
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc)) #*loc可以将loc元组中的数据解出来
    def click_element(self,loc):
        self.find_element(loc).click()
    def input_element(self,loc,data):
        """
        :param loc:
        :param loc_value:
        :param data:  输入数据
        :return:
        """
        self.find_element(loc).send_keys(data)

