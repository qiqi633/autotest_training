#!/usr/bin/python
# coding:utf-8
from appium import webdriver  # 导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
# 没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.android.settings'  # 手机启动包名
desired_caps['appActivity'] = '.HWSettings'  # 启动名
# 以下两个变量，可以在输入框中输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 调起appium工具，会自动打开/重启app

try:
    # 打开通知栏
    driver.open_notifications()
    list=driver.find_elements_by_id('android:id/icon')
    list[3].click()
    time.sleep(2)


    #获取手机当前网络#
    # 0表示都数据，wifi，飞行模式都没开，
    # 1表示只开了飞行模式
    #2只开了wifi
    #4只开了数据模式
    #所有模式都开了
    x=driver.network_connection
    print(x)
    driver.set_network_connection(4)
    y = driver.network_connection
    print(y)

    #获得notication 的消息 并打开APP,报错则截图
    title = driver.find_element_by_xpath("//*[contains(@text,'途牛旅游')]")
    title.click()
    driver.get_screenshot_as_file("./screenshot/error.png")

    #使用手机键来回到主界面
    driver.keyevent(3)
    time.sleep(1)
except Exception as e:
    print(e)
finally:
    driver.quit()