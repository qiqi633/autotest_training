#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import string

#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



import pytest


#setup teardown是运行于函数级别，每个函数始末都会运行一次
class Test_ST:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'S9B7N17819001588'
        desired_caps['appPackage'] = 'com.android.contacts'  # 手机启动包名
        desired_caps['appActivity'] = '.activities.PeopleActivity'  # 启动名
        # 以下两个变量，可以在输入框中输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 调起appium工具，会自动打开/重启app

        print("setup----")
    def teardown_class(self):
        self.driver.quit()
        print ("teardown----")
    def huadong(self):
        pix = self.driver.get_window_size()
        x1 = pix['width'] * 0.5
        y1 = pix['height'] * 0.8
        x2 = pix['width'] * 0.5
        y2 = pix['height'] * 0.5
        self.driver.swipe(x1, y1, x2, y2, 3000)

    # 查找信息列表中的数据
    def check_info(self):
        num = 0
        while num <= 10:
            name = self.driver.find_elements_by_class_name('android.widget.TextView')
            for i in name:
                if i.text == 'Yox':
                    i.click()
                    return ()
            # 获取屏幕信息，滑动屏幕到下一页继续找
            self.huadong()
            num += 1
    def test_001(self):
        #实际操作
        self.check_info()
        l = self.driver.find_elements_by_id('com.android.contacts:id/data')
        li = []
        for i in l:
            li.append(i.text)
        assert "135 9035 6619" in li,"失败"

if __name__ == "__main__":
    pytest.main()