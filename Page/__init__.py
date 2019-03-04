#!/usr/bin/python
#coding=utf-8
from selenium.webdriver.common.by import By
# import importlib
# import sys
# importlib.reload(sys)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#login elements
app_update = (By.ID,'com.taptap:id/btn_update')
app_update_cancel = (By.ID,'com.taptap:id/btn_cancel')

go_to_setting = (By.ID,'com.taptap:id/head_portrait')
login_cellnum = (By.XPATH,"//*[contains(@text,'请输入手机号码')]")
login_regis =(By.ID,'com.taptap:id/login_register_btn')
login_data = '18603060289'
login_has_account = (By.XPATH,"//*[contains(@text,'有帐号?去登录')]")


#主界面元素：
game_recom = (By.ID,'com.taptap:id/game_market')
leaderboard = (By.ID,'com.taptap:id/rank')
plaza = (By.ID,'com.taptap:id/classify')
my_interest = (By.ID,'com.taptap:id/community')
my_games = (By.ID,'com.taptap:id/my_game')












login_account_cellnum = (By.ID,'com.taptap:id/login_phone')
login_account_email = (By.ID,'com.taptap:id/login_mail')
account_cellnum = (By.XPATH,"//*[contains(@text,'请输入手机号码')]")
account_email = (By.XPATH,"//*[contains(@text,'请输入邮箱地址')]")
email_pwd =(By.XPATH,"//*[contains(@text,'请输入登录密码')]")
account_num = '13590356619'
account_ver =(By.ID,'com.taptap:id/login_register_btn')
account_ver_code = (By.ID,'com.taptap:id/item_edittext')
veri_resend = (By.ID,'com.taptap:id/send_again')




verfi_code = '123456'
verfi_error = (By.XPATH,"//*[contains(@text,'验证码错误')]")
verfi_code1 = (By.ID,'com.taptap:id/item_code_iv1')
verfi_code2 = (By.ID,'com.taptap:id/item_code_iv2')
verfi_code3 = (By.ID,'com.taptap:id/item_code_iv3')
verfi_code4 = (By.ID,'com.taptap:id/item_code_iv4')
verfi_code5 = (By.ID,'com.taptap:id/item_code_iv5')
verfi_code6 = (By.ID,'com.taptap:id/item_code_iv6')

login_verfi_close = (By.ID,'com.taptap:id/close')
login_verfi_text = (By.ID,'com.taptap:id/item_edittext')





#已登录设置中心元素
per__set = (By.ID,'com.taptap:id/taper_setting')
set_class = (By.CLASS_NAME,'android.widget.TextView')

#设置密码
input_email = (By.XPATH,"//*[contains(@text,'输入邮箱')]")
input_pwd = (By.XPATH,"//*[contains(@text,'输入密码')]")
input_pwd_again = (By.XPATH,"//*[contains(@text,'再次输入邮箱')]")
input_pwd_old = (By.XPATH,"//*[contains(@text,'输入旧密码')]")
input_pwd_new = (By.XPATH,"//*[contains(@text,'输入新密码')]")
input_pwd__new_again = (By.XPATH,"//*[contains(@text,'再次输入新密码')]")
check_button = (By.ID,'com.taptap:id/password_btn')
pwd_eye = (By.ID,'com.taptap:id/password_pw_eye')
email = '630345353@qq.com'
pwd_old = '0117151026imok'
pwd_new = '0117151026imok'


xinjian = (By.XPATH, "//*[contains(@text,'新建联系人')]")
xinming = (By.XPATH, "//*[contains(@text,'姓名')]")
fanhui = (By.ID, 'android:id/icon1')
fangqi = (By.XPATH, "//*[contains(@text,'放弃')]")

#开发者头条

DEV_mian_login = (By.ID,'io.manong.developerdaily:id/tab_bar_plus')
DEV_login_email = (By.ID,'io.manong.developerdaily:id/btn_email')
DEV_email_count = (By.ID,'io.manong.developerdaily:id/edt_email')
DEV_email_pwd = (By.ID,'io.manong.developerdaily:id/edt_password')
DEV_email_conf = (By.ID,'io.manong.developerdaily:id/edt_password')