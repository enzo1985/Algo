from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bs = BeautifulSoup(html, "html.parser")
#print(bs.head)

for child in bs.find_all(src=True):
    print(child)

img_location = bs.find("a", id="logo").find("img")["src"]
print(img_location)

