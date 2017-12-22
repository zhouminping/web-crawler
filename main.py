import crawler
import db
from bs4 import BeautifulSoup
import time

db_config = {
	'user': 'zhouminping',
	'password': 'qazwsx',
	'host': '178.62.122.173',
	'database': 'house_info',
	'charset': 'utf8'
}

# connection = db.connect(db_config)
# db.close(connection)

area_list = crawler.get_all_areas()
# print(area_list)

for area in area_list:
	location_list = crawler.get_all_locations(area)
	# print(location_list)
	for location in location_list:
		print('********************************')
		print(location['name'])
		print('********************************')
		# time.sleep(1000)
		house_list = crawler.get_all_houses(location)
