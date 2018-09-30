#coding : utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

bs = BeautifulSoup(html, "html.parser")

#print(bs.prettify() )
#print(bs.title)
#访问Tag
#print(bs.head)
#print(bs.html)
#print(bs.p.attrs)
#print(bs.html.name)
#访问tag的内容
#print(bs.p.string)

#print(bs.head.contents)

#for child in bs.body.children:
#    print(child)

#print (bs.p)
#print(bs.p.next_sibling.next_sibling)
#print(bs.head.next_element.next_element)
print(bs.find_all(re.compile("^a"), limit=2))
