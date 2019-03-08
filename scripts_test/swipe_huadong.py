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
#新建联系人
try:
    #swipe 点对点滑动
    driver.swipe(374,701,378,1056,2000)
    driver.swipe(378, 1056,374,701,2000)
    #scroll 元素间滑动
    sta = driver.find_element_by_xpath("//*[contains(@text,'双卡管理')]")
    des = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
    driver.scroll(sta,des)
    time.sleep(2)

    #drag 拖拽，从A滑动到B，B元素代替第一个元素
    driver.drag_and_drop(sta,des)
    time.sleep(2)
    # 应用置于后台
    driver.background_app(10)

    #操作手机主界面，滑动失败，因为是appium线性处理，必须先关掉应用，10s时间结束后，应用自动切到前端。
    # driver.swipe(228,914, 914,914, 2000)
    # time.sleep(5)
    # driver.tap(677,1083)
    # time.sleep(2)


except Exception as e:
    print(e)
finally:
    driver.quit()