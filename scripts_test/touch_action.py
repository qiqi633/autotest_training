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
def check_info():
    num = 0
    while num<=10:
        name=dri.find_elements_by_class_name('android.widget.TextView')
        for i in name:
            if i.text == 'Yox':
                i.click()
                return()
        #获取屏幕信息，滑动屏幕到下一页继续找
        huadong()
        num+=1
#TouchAction  模拟手势高级操作  ，将一系列操作发送到服务器，再逐个解析执行
try:
    dri = phonebook()

    #使用TouchAction(driver).tap(element).perform()方法点击
    ele = dri.find_element_by_xpath("//*[contains(@text,'新建联系人')]")
    #TouchAction(dri).tap(ele).perform()   # perform() 发送命令到服务器执行
    # print(ele.location.get('x'),ele.location.get('y'))
    # TouchAction(dri).tap(x=ele.location.get('x'),y=ele.location.get('y')).perform()

    #press\release 通过元素方式点击控件,一系列动作放到一个命令发送
    # TouchAction(dri).press(ele).release().perform()


    #长按wait
    # TouchAction(dri).press(ele).wait(2000).release().perform()

    #long_press
    # TouchAction(dri).long_press(ele,1000).release().perform()
    
    time.sleep(2)
except Exception as e:
    print(e)
finally:
    dri.quit()