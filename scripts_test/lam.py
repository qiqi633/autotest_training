#!/usr/bin/python
#coding:utf-8
from initDriver.initDriver import initDriver

def open_redtides():
    initDriver()  #初始化数据
    initDriver().quit()
if __name__=='__main__': #当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    open_redtides()