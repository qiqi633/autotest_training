#!\usr\bin\python
# -*-coding:utf-8-*-
from appium import webdriver #导入driver对象
import base64

#声明手机驱动对象
#以下信息使用adb命令查看
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'S9B7N17819001588'
desired_caps['appPackage'] = 'com.gamesci.u1.herou.prod' #手机启动包名
desired_caps['appActivity'] = 'com.gamesci.u1.UnityPlayerActivity' #启动名

#声明手机驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #第一个服务端地址、第二个服务端启动参数


#关闭app
#driver.close_app()

"""
以下内容测试通过

#启动其他app
driver.start_activity('com.android.calculator2','.Calculator')

#安装app，首先判断是否已存在app.不存在则安装，存在则不安装,以下内容测试通过

if driver.is_app_installed("com.mgyapp.android"):
    print('应用已存在')
    driver.remove_app('com.mgyapp.android')
else:
    print('尚未安装应用')
driver.install_app("E:\p4\u2_main\version\Android_mother\app-herou-release.apk")


#向手机里发送数据
data=str(base64.b64encode("miaomiaomiao".encode('utf-8')))
driver.push_file("/sdcard/push.txt",data)

#从手机里读取数据
data=driver.pull_file("/sdcard/push.txt")
print(str(base64.b64decode(data.decode('utf-8'))))
"""
#获取当前页面元素结构

data=driver.page_source.decode('utf-8')
for i in ('抵制不良游戏'):
    if i in data:
        print(True)
    else:
        print(false)






#关闭驱动
#driver.quit()
