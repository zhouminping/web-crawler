from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Area(object):
	"""docstring for Area"""
	def __init__(self, name):
		self.name = name

class Location():
	"""docstring for Location"""
	def __init__(self, name, area):
		self.name = name
		self.area = area

class House(object):
	"""docstring for House"""
	def __init__(self, unit_price, total_price, location):
		self.unit_price = unit_price
		self.total_price = total_price
		self.location = location

def getBsObj(url):
	html = urlopen(url)
	return BeautifulSoup(html.read(), "lxml")

domain = "http://sh.lianjia.com"
home_page_bs = getBsObj(domain + "/ershoufang")
area_list = []
location_list = []
house_list = []

# total_price = home_page_bs.find("ul", {"class": "js_fang_list"}).find("span", {"class", "total-price strong-num"}).getText()
# unit_price_part = home_page_bs.find("ul", {"class": "js_fang_list"}).find("span", {"class", "info-col price-item minor"}).getText().strip()
# unit_price = re.search('\d+', unit_price_part).group(0)

# print(total_price)
# print(unit_price)

# total_price_all = home_page_bs.find("ul", {"class": "js_fang_list"}).findAll("span", {"class", "total-price strong-num"})

# for total_price in total_price_all:
# 	print(total_price.getText())

# unit_price_all = home_page_bs.find("ul", {"class": "js_fang_list"}).findAll("span", {"class", "info-col price-item minor"})

# for unit_price in unit_price_all:
# 	unit_price_part = unit_price.getText().strip()
# 	print(re.search('\d+', unit_price_part).group(0))

area_links = home_page_bs.find("div", {"class": "level1"}).findAll("a")

f = open('data.csv', 'w+')

for area_link in area_links[1:]:
	area = Area(area_link.getText())
	area_list.append(area)
	area_page_bs = getBsObj(domain + area_link.get('href'))
	location_links = area_page_bs.find("div", {"class": "level2 gio_plate"}).findAll("a")
	for location_link in location_links[1:]:
		location = Location(location_link.getText(), area)
		location_list.append(location)
		location_page_bs = getBsObj(domain + location_link.get('href'))
		house_infos = location_page_bs.findAll("div", {"class": "info-table"})
		for house_info in house_infos:
			unit_price = re.search('\d+', house_info.find("span", {"class": "price-item"}).getText().strip()).group(0)
			total_price = house_info.find("span", {"class": "total-price"}).getText()
			house = House(unit_price, total_price, location)
			house_list.append(house)
			f.write(house.unit_price + ', ' + house.total_price + ', ' + location.name + ', ' + area.name + '\n')

f.close()