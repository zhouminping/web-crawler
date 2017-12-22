import util
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time

domain = "http://sh.lianjia.com"

def get_bs_obj(url):
	print("\n Get bs: " + url + "\n")
	time.sleep(1)
	html = urlopen(url)
	return BeautifulSoup(html.read(), "lxml")

# bs_obj = get_bs_obj("http://www.baidu.com")
# # print(bs_obj)

@util.retry(10)
def get_area_bs():
	home_page_bs = get_bs_obj(domain + "/ershoufang")
	return home_page_bs.find("div", {"class": "level1"})

@util.retry(10)
def get_location_bs(area):
	return get_bs_obj(area['href']).find("div", {"class": "level2"})

def get_all_areas():
	area_bs = get_area_bs()
	area_list = []
	for area_info in area_bs.findAll("a")[1:]:
		area = {}
		area['href'] = domain + area_info.get("href")
		area['name'] = area_info.getText()
		area_list.append(area)
	return area_list

def get_all_locations(area):
	location_bs = get_location_bs(area)
	location_list = []
	for location_info in location_bs.findAll("div", {"class": "level2-item"})[1:]:
		location = {}
		location['href'] = domain + location_info.find("a").get("href")
		location['name'] = location_info.find("a").getText()
		location_list.append(location)
	return location_list

@util.retry(10)
def get_house_pages(location):
	# print(location['href'])
	pos = get_bs_obj(location['href']).find("a", text="下一页")
	# print(pos)
	if pos is None:
		return 1;
	else: 
		return int(pos.find_previous_sibling().getText())

@util.retry(10)
def get_house_info(house_link):
	house_bs = get_bs_obj(house_link)
	print(house_link)
	house = {}
	house['house_id'] = re.search('\d+', house_link).group(0)
	print('house_id: ' + house['house_id'])
	house['href'] = house_link
	print('house_href: ' + house['href'])
	house['total_price'] = int(house_bs.find("div", {"class": "price-total"}).find("span", {"class": "price-num"}).getText())
	print('total_price: ' + str(house['total_price']))
	house['unit_price'] = int(house_bs.find("div", {"class": "price-unit"}).find("span").getText())
	print('unit_price: ' + str(house['unit_price']))
	try:
		house['facing'] = house_bs.find(text="房屋朝向").find_next().getText().strip()
	except Exception as e:
		house['facing'] = ''
	print('facing: ' + house['facing']) 
	house_floor_info = house_bs.find(text="所在楼层").find_next().getText().strip().split('/')
	house['floor'] = house_floor_info[0]
	print('floor: ' + house['floor'])
	try:
		house['layers'] = int(re.search('\d+', house_floor_info[1]).group(0)) 
	except Exception as e:
		house['layers'] = 0
	print('layers: ' + str(house['layers']))
	house_size = house_bs.find(text="建筑面积").find_next().getText().strip()
	house['size'] = float(re.search('\d+.\d+', house_size).group(0))
	print('size: ' + str(house['size']))
	house['decorate'] = house_bs.find(text="装修情况").find_next().getText().strip()
	print('decorate: ' + house['decorate'])

	main_info = house_bs.find("ul", {"class": "maininfo-main"}).getText()
	main_infos = ','.join(main_info.split()).split(',')

	try:
		house['age'] = int(re.search('\d+', main_infos[5]).group(0))
	except Exception as e:
		try:
			age_info = house_bs.find(text="建筑年代").find_next().getText().strip()
			house['age'] = int(re.search('\d+', age_info).group(0)) 
		except Exception as e:
			house['age'] = 0
	print('age: ' + str(house['age']))

	house_region = house_bs.find(text="小区名称").find_next().getText()
	house_region_list = ','.join(house_region.split()).split(',')
	house['community'] = house_region_list[0]
	print('community: ' + house['community'])
	house['area'] = re.search('[^\(]+', house_region_list[1]).group(0)
	print('area: ' + house['area'])
	house['location'] = re.search('.[^\(]', house_region_list[2]).group(0)
	print('location:' + house['location'])
	
	house['buy_time'] = house_bs.find(text="上次交易").find_next().getText().strip()
	print('buy_time: ' + house['buy_time'])
	house['years'] = house_bs.find(text="房本年限").find_next().getText().strip()
	print('years: ' + house['years'])

	house['7_days_watch'] = int(house_bs.find("look-list")['count7'])
	print('7_days_watch: ' + str(house['7_days_watch']))
	house['total_watch'] = int(house_bs.find("look-list")['count90'])
	print('total_watch: ' + str(house['total_watch']))

	visit_data = house_bs.findAll("script")[1].getText()
	# try:
	# 	house['first_visit'] = util.parse_js(visit_data)['date']
	# except Exception as e:
	# 	house['first_visit'] = ''
	# print('first_visit: ' + house['first_visit'])
	return house


@util.retry(10)
def get_one_page_house(link):
	one_page_house_bs = get_bs_obj(link).find("ul", {"class": "js_fang_list"})
	houses = []
	for house_info in one_page_house_bs.findAll("li"):
		house_link = domain + house_info.find("a")['href']
		houses.append(get_house_info(house_link))
	return houses

def get_all_houses(location):
	pages = get_house_pages(location)
	all_houses = []
	# print(location['name'] + ": ")
	for page in range(1, pages+1):
		# print('p' + str(page) + '\n')
		houses = get_one_page_house(location['href'] + '/d' + str(page))
		all_houses.extend(houses)
	return all_houses
		
# get_one_page_house("http://sh.lianjia.com/ershoufang/beicai/d17")

# get_house_info("http://sh.lianjia.com/ershoufang/sh4886001.html")

# get_house_info("http://sh.lianjia.com/ershoufang/sh4782249.html")



# bs = get_bs_obj("http://sh.lianjia.com/ershoufang/sh4847349.html")
# print(bs)