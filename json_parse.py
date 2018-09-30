# -*- coding:utf-8 -*-

from urllib.request import urlopen
import requests
import json
from pprint import pprint
import sys, time
from random import randint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
start_url = "https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=percent&type=11%2C12"

home_site = "https://xueqiu.com/"
file_name = "stocklist.json"
def get_json_data():
    #有些网站检查User-Agent，是否由浏览器发起的操作
    #需要先访问主页获取cookie才能得到数据
    # 使用session可以在多条请求之间保持cookies
    session = requests.Session()
    session.headers = headers
    session.get(home_site)
    for i in range(1,3):
        delay = randint(3,7)
        print (time.time())
        time.sleep(delay)
        print (time.time())
        url = "https://xueqiu.com/stock/cata/stocklist.json?page=" + str(i) +"&size=30&order=desc&orderby=percent&type=11%2C12"
        r = session.get(url,headers = headers)
        #pprint(r.text)
        data = json.loads(r.text, encoding="utf-8")
        for item in data["stocks"]:
            print("name=%s, symbol=%s " % (item["name"], item["symbol"]))

        pprint("*"*80)


def my_json_parser():
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        #print(data['stocks'])
        for item in data["stocks"]:
            print("name=%s, symbol=%s " % (item["name"], item["symbol"]))



get_json_data()

#my_json_parser()