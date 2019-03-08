#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time

#声明手机驱动对象
#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = '4321ad89'
desired_caps['appPackage'] = 'com.gamesci.u1.herou.prod' #手机启动包名
desired_caps['appActivity'] = 'com.gamesci.u1.UnityPlayerActivity' #启动名

#声明手机驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #第一个服务端地址、第二个服务端启动参数
try:
    time.sleep(5)
    X = driver.get_window_size()['width']
    Y = driver.get_window_size()['height']
    print(X,Y)
    driver.tap(X*0.5,Y*0.5)
    time.sleep(50)

except Exception as e:
    print(e)
finally:
    driver.quit()



 #class name 不是唯一的，不能定位元素,
    #以下是元素定位方法
    # 1.获取需定位元素的绝对坐标（x1, y1)，开启指针位置后，通过点击定位元素位置获取坐标；
    # 2. 获取测试手机的屏幕大小（x2, y2）, 开启指针位置后，点击手机屏幕右下角，获取坐标
    # 3.得出该定位元素的相对位置坐标系x = x1 / x2, y = y1 / y2(控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数)
    # 4.获取当前手机的屏幕大小(n, m)，通过driver.get_window_size()['width'], dirver.get_window_size()['height']
    # 分辨获取当前手机的n、m坐标;
    # 5.获取指定控件在测试手机中的坐标：(x * n, y * m)
    # 6.获取到坐标之后同样使用tap()函数点击该控件。
    # X = driver.get_window_size()['width']
    # Y = driver.get_window_size()['height']
    # driver.tap(,)