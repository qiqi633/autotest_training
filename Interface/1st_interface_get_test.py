#!usr/bin/python
#coding=utf-8
import requests
import pytest
import json
from readout_weather_data import ret_weather_data
def get_data_para():
    para_list = []
    para = ret_weather_data('weather_data').get('para')
    # print(para)
    for i in para:
        para_list.append((i,para[i].get('key'),para[i].get('city_id'),para[i].get('weather_date')))
    return para_list
@pytest.fixture(scope='module')
def get_dir_para():
    dir_para = ret_weather_data('weather_data').get('para')
    dir_list = []
    for i in dir_para:
        # print(dir_para[i])
        dir_list.append((i,dir_para[i]))
    # print(type(dir_list[1]),type(dir_list[1][0]),type(dir_list[1][1]))
    return dir_list


class Get_test:
    def setup(self):
        print("setup>>>>>>>>>>>>>>>>>>>")
    def teardown(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>teardown")
    #给接口地址定位变量名称
    url = "http://v.juhe.cn/historyWeather/weather"
    @pytest.mark.parametrize('testcase, params',get_dir_para())
    def get_send(self,testcase,params):
        g_send = requests.get(self.url,params=params)
        res =g_send.json()
        # with open("./interface test/test_result.txt",'a+') as f:
        #     f.write('\nstatus code : ' + str(g_send.status_code) + '\nresult : ' + str(res))
        #     f.close()
        # print("\n"+'testcase:'+testcase+'\n'+'test status code:'+str(g_send.status_code)+'\n'+'test result:'+str(res))
        # print("\ntestcase : {0},\ntest status code : {1},\ntest result : {2}".format(testcase,g_send.status_code,res))
        with open("./interface test/test_result.json",'a+') as f:
            json.dump(res,f,encoding='utf-8')
            f.close()