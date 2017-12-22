from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://lianjia.com")
bs = BeautifulSoup(html, "lxml")
print(bs)