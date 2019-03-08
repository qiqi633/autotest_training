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
#滑动屏幕
def huadong():
    pix=dri.get_window_size()
    x1 = pix['width']*0.5
    y1 = pix['height']*0.8
    x2 = pix['width'] * 0.5
    y2 = pix['height']*0.5
    dri.swipe(x1,y1,x2,y2,3000)
#查找信息列表中的数据
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
try:
    dri=phonebook()
    time.sleep(2)
    #查找当前页面所有的元素，如果元素中有YOX则点击，否则滑动屏幕到下一页
    check_info()
    time.sleep(2)
    #进入联系人页面后，点击信息发送按钮；
    dri.find_element_by_id('com.android.contacts:id/primary_action_button').click()

    #生成消息内容，将消息放入输入框
    def ran_letter():
        return (random.choice(string.ascii_letters))
    name = []
    for z in range(3):
        x = ran_letter()
        name.append(x)
    #dri.find_element_by_xpath("//*[contains(@text,'输入信息')]").send_keys(name)
    #为了保证健壮性，可以用以下方法写查找信息语句
    # shuru = WebDriverWait(dri,5,0.5).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'输入信息')]"))
    # shuru.send_keys(name)
    #也可以WebDriverWait提炼出来作为函数
    def xpath_check(self,xpath):
        return WebDriverWait(dri,5,0.5).until(lambda x:x.find_element_by_xpath(xpath))
    xpath_check("//*[contains(@text,'输入信息')]").send_keys(name)
    time.sleep(2)
    dri.find_element_by_id('com.android.mms:id/send_button_sms').click()
except Exception as e:
    print(e)
finally:
    dri.quit()
