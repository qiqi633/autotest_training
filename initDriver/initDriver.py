#!/usr/bin/python
#coding:utf-8
from appium import webdriver
def initDriver(package_name,activity_name):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'S9B7N17819001588'
    desired_caps['appPackage'] = package_name
    desired_caps['appActivity'] = activity_name
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    #声明手机驱动对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #第一个服务端地址、第二个服务端启动参数
    print(desired_caps)
    return driver
