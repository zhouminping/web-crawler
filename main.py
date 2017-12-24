import crawler
import db
from bs4 import BeautifulSoup


connection = db.connect(db.config)

add_house_sql = "INSERT INTO `house` (`house_id`, `href`, `area_id`, `location_id`, `community`, `age`, `size`, `layers`, `floor`, `facing`, `decorate`, `buy_time`, `years`, `unit_price`, `total_price`, `first_visit`, `7_days_watch`, `total_watch`) VALUES (%(house_id)s, %(href)s, %(area_id)s, %(location_id)s, %(community)s, %(age)s, %(size)s, %(layers)s, %(floor)s, %(facing)s, %(decorate)s, %(buy_time)s, %(years)s, %(unit_price)s, %(total_price)s, %(first_visit)s, %(7_days_watch)s, %(total_watch)s)"

def get_location_id_by_name(location_name):
	sql = "SELECT id FROM location WHERE name = %s"
	with connection.cursor() as cursor:
		cursor.execute(sql, (location_name,))
		result = cursor.fetchone()[0]
	return result

def get_area_id_by_name(area_name):
	with connection.cursor() as cursor:
		sql = "SELECT id FROM area WHERE name = %s"
		cursor.execute(sql, (area_name,))
		result = cursor.fetchone()[0]
	return result


area_list = crawler.get_all_areas()
# print(area_list)

for area in area_list:
	area_id = get_area_id_by_name(area['name'])
	# print(area['name'] + ": " + str(get_area_id_by_name(area['name'])))
	location_list = crawler.get_all_locations(area)
	# print(location_list)
	for location in location_list:
		location_id = get_location_id_by_name(location['name'])
		# print(location['name'] + ": " + str(get_location_id_by_name(location['name'])))
		print('********************************')
		print(location['name'])
		print('********************************')
		pages = crawler.get_house_pages(location)
		for page in range(1, pages+1):
			houses = crawler.get_one_page_house(location['href'] + '/d' + str(page))
			print("Write to DB: " + area['name'] + location['name'] + str(page))
			for house in houses:
				house['area_id'] = area_id
				house['location_id'] = location_id
				db.write(add_house_sql, house, connection)

db.close(connection)

