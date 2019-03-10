#!/usr/bin/python
#coding=utf-8
import requests
import re
import urllib.request
import urllib
url_tap = 'https://cn.bing.com/'
s = requests.session()
res = s.get(url_tap,verify = False)
print(res.status_code)
r = re.findall(r' aria-label="主页图片信息" role="button" target="_blank" href="/search\?q=(.+?)&',res.text)
print(r)
url_search = 'https://cn.bing.com/search'
para = {
    'q':r[0],
    'from':'hpcapt',
    'mkt':'zh-cn'
}
print(para)
search = s.get(url_search,params = para)
print(search.status_code)


