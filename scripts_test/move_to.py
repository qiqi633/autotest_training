#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#声明手机驱动对象
#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.android.settings' #手机启动包名
desired_caps['appActivity'] = '.HWSettings' #启动名

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app


def huadong():
    pix=driver.get_window_size()
    x1 = pix['width']*0.5
    y1 = pix['height']*0.8
    x2 = pix['width'] * 0.5
    y2 = pix['height']*0.5
    driver.swipe(x1,y1,x2,y2,3000)
#查找信息列表中的数据
def check_info(data):
    num = 0
    while num<=10:
        name=driver.find_elements_by_class_name('android.widget.TextView')
        for i in name:
            if i.text == data:
                i.click()
                return()
        #获取屏幕信息，滑动屏幕到下一页继续找
        huadong()
        num+=1


try:
    pass
    data='锁屏和密码'
    check_info(data)
    driver.find_element_by_xpath("//*[contains(@text,'智能解锁')]").click()
    driver.find_element_by_xpath("//*[contains(@text,'第一步，设置锁屏密码')]").click()
    dri = driver.find_elements_by_id('com.android.settings:id/arrow')
    dri[0].click()

    #使用move_to 画图，取坐标：（329,814），（541,814），（814,814），（814,1087），（814,1360）
    #以下参数需要说明x,y参数值，否者默认将参数给第一个和第二个参数位 .move_to(x=273,y=0).move_to(x=0,y=273).move_to(x=0,y=273)  move_to(None,212,0).
    TouchAction(driver).press(None,329,814).move_to(None,541,814).wait(3000).release().perform()
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.quit()

