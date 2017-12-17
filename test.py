from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://sh.lianjia.com/ershoufang/beicai")

bsObj = BeautifulSoup(html.read(), "lxml")

info_table = bsObj.find("div", {"class": "info-table"})

# info = info_table.find("span", {"class": "row1-text"}).getText().split('|')

# base_infos = [i.strip() for i in info]

# layers = re.search('\d+', base_infos[2].split('/')[1]).group(0)
# floor = base_infos[2].split('/')[0]
# orientation = base_infos[3]

# print(re.search('\d+.\d+', base_infos[1]).group(0))

# print(layers)
# print(floor)
# print(orientation)

# info = info_table.find("span", {"class": "row2-text"}).getText().split('|')
# base_infos = [i.strip() for i in info]
# print(base_infos)

property = info_table.find_next_sibling("div").getText()
if "满五" in property:
	print("1")
else:
	print("0")
print(property)