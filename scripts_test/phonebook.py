#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
import random
import string
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import importlib
import sys
importlib.reload(sys)

#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.android.contacts' #手机启动包名
desired_caps['appActivity'] = '.activities.PeopleActivity' #启动名
#以下两个变量，可以在输入框中输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app
#新建联系人

def ran_letter():
    return (random.choice(string.ascii_letters))
try:
    time.sleep(2)
    driver.find_element_by_xpath("//*[contains(@text,'新建联系人')]").click()
    time.sleep(2)
    name=[]
    for z in range(3):
        x=ran_letter()
        name.append(x)
    driver.find_element_by_xpath("//*[contains(@text,'姓名')]").send_keys(name)
    driver.find_element_by_xpath("//*[contains(@text,'工作单位')]").click()
    driver.find_element_by_xpath("//*[contains(@text,'公司')]").click()
    #获得随机字母
    company = []
    for j in range(4):
        y=ran_letter()
        company.append(y)
    driver.find_element_by_xpath("//*[contains(@text,'公司')]").send_keys(company)
    driver.find_element_by_xpath("//*[contains(@text,'电话号码')]").click()
    #使用变量，再send_keys(变量)，直接send_keys(数据)存在退格现象。
    data='13590356619'
    driver.find_element_by_xpath("//*[contains(@text,'电话号码')]").send_keys(data)
    time.sleep(5)
    #界面往下滑动
    
    driver.find_element_by_id('android:id/icon2').click()
    time.sleep(2)
except Exception as e:
    print(e)
finally:
    driver.quit()

