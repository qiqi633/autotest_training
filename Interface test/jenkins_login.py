#!usr/bin/python
#coding=utf-8
import requests
import pytest
import yaml
from readout_weather_data import ret_weather_data
def get_dir_para():
    dir_para = ret_weather_data('weather_data').get('jenkins_login')
    dir_list = []
    for i in dir_para:
        # print(dir_para[i])
        dir_list.append((i,dir_para[i]))
    # print(type(dir_list[1]),type(dir_list[1][0]),type(dir_list[1][1]))
    return dir_list


class Post_jenkins:
    def setup(self):
        print("setup>>>>>>>>>>>>>>>>>>>")
    def teardown(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>teardown")
    #给接口地址定位变量名称
    url = "http://192.168.1.165:8080/j_acegi_security_check"
    @pytest.mark.parametrize('testcase, params',get_dir_para())
    def post_send(self,testcase,params):
        p_send = requests.post(self.url,params)
        with open('./jenkins_test_result.yaml','a+') as f:
            yaml.dump(p_send,f,encoding='utf-8',allow_unicode=True)
            f.close()






