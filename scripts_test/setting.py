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

#声明手机驱动对象
#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.android.settings' #手机启动包名
desired_caps['appActivity'] = '.HWSettings' #启动名

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app
try:
    pass
    time.sleep(5)
    driver.find_element_by_id('android:id/search_src_text').click()
    time.sleep(5)
    driver.find_element_by_id('com.android.settings:id/back').click()
    time.sleep(5)

    #以上id定位是id是唯一的。 当通过id不能直接定位以下数据时，请使用下面方法:find_elements_by_id

    ele_list=driver.find_elements_by_id("android:id/title")# find_elements返回一组数据
    ele_list[0].click() #点击第一个id.
    time.sleep(5)
    for i in ele_list:  #循环查看ele_list里的元素
        # print(i.text,type(i.text))  中文字需要统一编码
        if i.text == 'WLAN':
            i.click()
        elif i.text == '双卡管理': #中文处理需要修改编码
            i.click()
            break
    time.sleep(5)
    #使用find_elements_by_class_name()定位一组元素
    # ele_class_list=driver.find_elements_by_class_name('android.widget.ImageView')#返回一组list
    # ele_class_list[0].click()
    driver.find_element_by_id('android:id/up').click()
    time.sleep(5)
    #定位一组元素 xpath
    xpath_value="//*[contains(@class,'android.widget.TextView')]"
    ele_xpath_list=driver.find_elements_by_xpath(xpath_value)
    for i in ele_xpath_list:
        if i.text == '主屏幕':
            i.click()
            break

    #显示等待方法很重要，可以测试代码卡顿的地方
    print(time.strftime('%H:%M:%S', time.localtime()))
    #WebDriverWait(driver,timeout=5,poll_frequency=0.5).until(lambda x:x.find_element_by_id('xxx'))
    ele = WebDriverWait(driver, timeout=5, poll_frequency=0.5).until(\
        lambda x: x.find_element_by_xpath("//*[contains(@text,'飞行模式')]"))
    ele.click()
    print(time.strftime('%H:%M:%S', time.localtime()))



    time.sleep(50)

except Exception as e:
    print(e)
finally:
    driver.quit()