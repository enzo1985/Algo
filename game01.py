# coding: utf-8


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, "html.parser")

#for child in bs.find("table", {"id":"giftList"}).children:
#    print(child)

for sibling in bs.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)

images = bs.findAll("img", {"src":re.compile("\.\./img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)