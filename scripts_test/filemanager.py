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
#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.huawei.hidisk' #手机启动包名
desired_caps['appActivity'] = '.filemanager.FileManager' #启动名
#以下两个变量，可以在输入框中输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app

def huadong():
    pix=driver.get_window_size()
    x1 = pix['width']*0.5
    y1 = pix['height']*0.8
    x2 = pix['width'] * 0.5
    y2 = pix['height']*0.5
    driver.swipe(x1,y1,x2,y2,3000)
#查找信息列表中的数据
def check_info():
    num = 0
    while num<=10:
        name=driver.find_elements_by_id('com.huawei.hidisk:id/file_name')
        for i in name:
            if i.text == 'ANRSnap':
                TouchAction(driver).long_press(name,3000).perform()
                return()
        #获取屏幕信息，滑动屏幕到下一页继续找
        huadong()
        num+=1
try:
    time.sleep(2)
    driver.find_element_by_id('android:id/button1').click()
    driver.find_element_by_xpath("//*[contains(@text,'内部存储')]").click()
    # check_info()
    time.sleep(2)
except Exception as e:
    print(e)
finally:
    driver.quit()