#!/usr/bin/python
#coding=utf-8
import importlib
import sys
importlib.reload(sys)
from selenium.webdriver.common.by import By
search_txt = (By.CLASS_NAME,'android.widget.EditText')
search_btn = (By.ID,'android:id/search_src_text')
search_rtn = (By.ID,'com.android.settings:id/back')
