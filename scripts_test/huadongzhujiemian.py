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
#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#以下信息使用adb命令查看
def phonebook():
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
    return driver
def huadong():
    pix=dri.get_window_size()
    x1 = pix['width']*0.8
    y1 = pix['height']*0.5
    x2 = pix['width'] * 0.3
    y2 = pix['height']*0.5
    dri.swipe(x1,y1,x2,y2,3000)
try:
    dri = phonebook()
    dri.close_app()
    time.sleep(2)
    huadong()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    dri.quit()