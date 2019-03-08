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
#以下两个变量，可以在输入框中输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#调起appium工具，会自动打开/重启app

if __name__=='__main__': #当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    try:
        pass
        time.sleep(5)
        #定位输入框
        driver.find_element_by_id('android:id/search_src_text').click()
        time.sleep(5)
        #输入数据
        driver.find_element_by_id('android:id/search_src_text').send_keys(u'更多') # 在中文前加u，表示unicode编码
        time.sleep(5)
        #重复输入,首先清除文本框内数据
        driver.find_element_by_id('android:id/search_src_text').clear()
        time.sleep(2)
        driver.find_element_by_id('android:id/search_src_text').send_keys('WLAN')
        time.sleep(5)
        #循环输入多个数据
        for i in ("WLAN","wi","更多"):
            input_ele=driver.find_element_by_id('android:id/search_src_text')
            input_ele.clear()
            time.sleep(2)
            input_ele.send_keys(unicode(i)) # 在中文前加u，表示unicode编码，否则报错
            time.sleep(2)
            #下拉列表
            xl_data=driver.find_elements_by_id('com.android.settings:id/title')
            for j in xl_data:
                attr = j.get_attribute('text')
                loc = j.location
                print(attr)
                print(loc)
        #返回主界面
        driver.find_element_by_id('com.android.settings:id/back').click()
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        driver.quit()