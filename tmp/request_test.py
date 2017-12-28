from bs4 import BeautifulSoup
import requests

r = requests.get("http://sh.lianjia.com/ershoufang/sh4553999.html")

bs = BeautifulSoup(r.text, "lxml")

print(bs)