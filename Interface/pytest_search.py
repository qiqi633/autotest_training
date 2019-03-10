#coding=utf-8
import requests
import pytest
class Pytest_search:
    def test(self):
        url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-73109892605658-zhongtong.html"
        r = requests.get(url)
        res = r.json()
        print(res.get('company'))
        print(r.status_code)
        assert '参数异常' in res.get('reason'),'request error'

