# database: 192.168.1.7

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
	def __init__(self, house_id, community, age, size, layers, floor, orientation, five_years, two_years, unit_price, total_price, location):
		self.house_id = house_id
		self.community = community
		self.age = age
		self.size = size
		self.layers = layers
		self.floor = floor
		self.orientation = orientation
		self.five_years = five_years
		self.two_years = two_years
		self.unit_price = unit_price
		self.total_price = total_price
		self.location = location

def getBsObj(url):
	count = 0
	while (count < 9):
		try:
	 		html = urlopen(url)
	 		break
		except Exception as e:
			count += 1
	return BeautifulSoup(html.read(), "lxml")

domain = "http://sh.lianjia.com"
home_page_bs = getBsObj(domain + "/ershoufang")
area_list = []
location_list = []
house_list = []

area_links = home_page_bs.find("div", {"class": "level1"}).findAll("a")

f = open('data.csv', 'a')

for area_link in area_links[1:]:
	area = Area(area_link.getText())
	area_list.append(area)
	area_page_bs = getBsObj(domain + area_link.get('href'))
	location_links = area_page_bs.find("div", {"class": "level2 gio_plate"}).findAll("a")
	for location_link in location_links[1:]:
		location = Location(location_link.getText(), area)
		location_list.append(location)
		location_page_home_bs = getBsObj(domain + location_link.get('href'))
		try:
			page_nums = int(location_page_home_bs.find("div", {"class": "c-pagination"}).find("a", text="下一页").find_previous_sibling().getText())
		except Exception as e:
			page_nums = 1
		for p in range(1, page_nums+1):
			location_page_bs = getBsObj(domain + location_link.get('href') + '/d' + str(p))
			print(p)
			house_infos = location_page_bs.find("ul", {"class": "js_fang_list"}).findAll("li")
			for house_info in house_infos:
				house_id = re.search('\d+', house_info.find("div", {"class": "prop-title"}).find("a")["key"]).group(0)
				info_table = house_info.find("div", {"class": "info-table"})
				base_infos1 = info_table.find("span", {"class": "row1-text"}).getText().split('|')
				base_infos1 = [ base_info.strip() for base_info in base_infos1 ]
				print(base_infos1)
				size = re.search('\d+.\d+', base_infos1[1]).group(0)
				try:
					layers = re.search('\d+', base_infos1[2].split('/')[1]).group(0)
				except Exception as e:
					layers = base_infos1[2]
				try:
					floor = base_infos1[2].split('/')[0]
				except Exception as e:
					floor = base_infos1[2]
				try:
					orientation = base_infos1[3]
				except Exception as e:
					orientation = ''

				base_infos2 = info_table.find("span", {"class": "row2-text"}).getText().split('|')
				base_infos2 = [ base_info.strip() for base_info in base_infos2 ]
				print(base_infos2)
				community = base_infos2[0]
				try:
					age = re.search('\d+', base_infos2[3]).group(0)
				except Exception as e:
					age = ''
				property = house_info.find("div", {"class": "property-tag-container"}).getText()
				if "满五" in property:
					five_years = '1'
					two_years = '1'
				elif "满二" in property:
					five_years = '0'
					two_years = '1'
				else:
					five_years = '0'
					two_years = '0'
				unit_price = re.search('\d+', info_table.find("span", {"class": "price-item"}).getText().strip()).group(0)
				total_price = info_table.find("span", {"class": "total-price"}).getText()
				house = House(house_id, community, age, size, layers, floor, orientation, five_years, two_years, unit_price, total_price, location)
				house_list.append(house)
				f.write(house.house_id + ', '
					+ house.community + ', '
					+ house.age + ', '
					+ house.size + ', '
					+ house.layers + ', '
					+ house.floor + ', '
					+ house.orientation + ', '
					+ house.five_years + ', '
					+ house.two_years + ', '	
					+ house.unit_price + ', ' 
					+ house.total_price + ', ' 
					+ location.name + ', ' 
					+ area.name + '\n')

f.close()