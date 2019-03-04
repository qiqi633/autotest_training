#!/usr/bin/python
#coding:utf-8
from appium import webdriver #导入driver对象
import base64
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from initDriver.initDriver import initDriver
#没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式。 可以使用以下方式更改python编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')