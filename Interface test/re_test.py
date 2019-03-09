import requests
import re

url_tap = 'https://www.baidu.com/'
s = requests.session()
res = s.get(url_tap)
print(res)