# -*- coding:utf-8 -*-

from urllib.request import urlopen
import requests
import json
from pprint import pprint
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=percent&type=11%2C12"
#TODO: 从网上获取数据

file_name = "stocklist.json"
def my_json_parser():
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        #print(data['stocks'])
        for item in data["stocks"]:
            print("name=%s, symbol=%s " % (item["name"], item["symbol"]))



my_json_parser()