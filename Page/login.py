#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Base.Base import Base
from Base.Huadong import Huadong
import page
import sys
import time
from selenium.webdriver.common.touch_actions import TouchActions
# import importlib
# import sys
# importlib.reload(sys)
import pytest


class Login:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self, driver):
        self.obj = Base(driver)
        self.hua = Huadong(driver)
        self.driver =driver
    def goto_login(self):
        update = self.obj.find_element_x(page.app_update)
        assert update,'no update'
        self.driver.get_screenshot_as_file("./Screenshots/login/update_window.png")
        self.obj.click_element(page.app_update_cancel)
        self.driver.get_screenshot_as_file("./Screenshots/login/main_scene.png")
        time.sleep(2)
        self.obj.click_element(page.leaderboard)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_leaderboard.png")
        self.obj.click_element(page.plaza)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_plaza.png")
        self.obj.click_element(page.my_interest)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_community.png")
        self.obj.click_element(page.my_games)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_games.png")
        self.obj.click_element(page.game_recom)
        self.driver.get_screenshot_as_file("./Screenshots/main_page/main_market.png")
        self.obj.click_element(page.go_to_setting)
        time.sleep(2)
    def register_failture(self):

        assert self.obj.find_element_x(page.login_has_account), 'goto setting page failed'
        time.sleep(2)
        #注册用例
        #空号码点击注册
        self.obj.click_element(page.login_regis)

        #输入号码注册
        assert self.obj.find_element_x(page.login_cellnum), 'cant find input text'
        self.obj.input_element(page.login_cellnum, page.login_data)
        time.sleep(5)
        self.driver.get_screenshot_as_file("./Screenshots/login/login_cellnum.png")
        self.obj.click_element(page.login_regis)

        #输入验证码界面，不输入直接关闭，输入错误的关闭
        self.obj.click_element(page.login_verfi_close)
        self.obj.click_element(page.login_regis)
        self.obj.input_element(page.login_verfi_text, page.verfi_code)
        assert self.obj.find_element_x(page.verfi_error), 'verify error'
        self.driver.get_screenshot_as_file('./Screenshots/login/verfiy_error')
        self.obj.click_element(page.login_verfi_close)
        time.sleep(5)

    def login_failture(self):
        #切换登录方式页签，使用邮箱登录
        self.obj.click_element(page.login_has_account)
        self.driver.get_screenshot_as_file('./Screenshots/login/login_page')
        self.obj.click_element(page.login_account_email)
        time.sleep(2)
        self.obj.click_element(page.login_account_cellnum)

        self.obj.click_element(page.account_ver)

        self.obj.input_element(page.account_cellnum, page.account_num)
        self.driver.get_screenshot_as_file('./Screenshots/login/phonenumber_login')
        self.obj.click_element(page.account_ver)
        self.obj.input_element(page.account_ver_code, page.verfi_code)
        assert self.obj.find_element_x(page.verfi_error), 'verify error'
        # #重新发送验证码,点击重新发送按钮失败，为啥
        # cc = self.obj.find_element_x(Page.account_ver_code)
        # cc.clear()
        # self.obj.click_element(Page.veri_resend)
        # print("checkpoint:send message again")
        # assert self.obj.find_element_x(Page.verfi_code1).text is None,'resend verify code error'
        self.obj.click_element(page.login_verfi_close)
        time.sleep(2)



    #修改密码
    def get_need_element_down(self,ele_na,need_ele):
        """

        :param ele_name: class_name
        :param need_element: 待查找的text
        :return:
        """
        i = 20
        while i>=0:
            ele = self.driver.find_elements_by_class_name(ele_na)
            for e in ele:
                if e.text == need_ele:
                    e.click()
                    return
            self.hua.huadong_down()
            i-=1
    def change_pwd(self):
        self.obj.click_element(page.per__set)
        need_element = '密码安全'
        self.get_need_element_down(page.set_class, need_element)


        self.obj.input_element(page.input_pwd_old, page.pwd_old)
        self.obj.input_element(page.input_pwd_new, page.pwd_new)
        self.obj.input_element(page.input_pwd__new_again, page.pwd_new)
        self.obj.click_element(page.pwd_eye)
        self.driver.get_screenshot_as_file('./Screenshots/login/set_pwd.png')
        self.obj.click_element(page.check_button)
        time.sleep(5)










