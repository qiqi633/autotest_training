#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
from Base import Base
import pytest
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Huadong:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self, driver):
        self.driver = driver
    def huadong_up(self):
        pix = self.driver.get_window_size()
        start_x = pix['width' ] *0.5
        start_y = pix['height' ] *0.8
        end_x = pix['width'] * 0.5
        end_y = pix['height'] * 0.5
        self.driver.swipe(start_x ,start_y ,end_x ,end_y ,2000)
    def huadong_down(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.5
        start_y = pix['height'] * 0.8
        end_x = pix['width'] * 0.5
        end_y = pix['height'] * 0.5
        self.driver.swipe(end_x, end_y, start_x, start_y, 2000)
    def huadong_turnright(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.6
        start_y = pix['height'] * 0.5
        end_x = pix['width'] * 0.3
        end_y = pix['height'] * 0.5
        self.driver.swipe(end_x, end_y, start_x, start_y, 2000)
    def huadong_turnleft(self):
        pix = self.driver.get_window_size()
        start_x = pix['width'] * 0.6
        start_y = pix['height'] * 0.5
        end_x = pix['width'] * 0.3
        end_y = pix['height'] * 0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)


