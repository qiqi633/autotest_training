#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.android.settings' #手机启动包名
desired_caps['appActivity'] = '.HWSettings' #启动名
#以下两个变量，可以在输入框中输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app

try:
    t=driver.device_time
    print(t)
    pix=driver.get_window_size()
    print(pix)
    x1 = pix['width']*0.5
    y1 = pix['height']*0.5
    x2 = pix['width'] * 0.5
    y2 = pix['height']*0.8
    time.sleep(10)
    driver.swipe(x1,y1,x2,y2,3000)
    #调节音量
    for i in range(2):
        driver.keyevent(24) #24是音量加
    for i in range(3):
        driver.keyevent(25) #25是音量减

    #打开通知栏
except Exception as e:
    print(e)
finally:
    driver.quit()