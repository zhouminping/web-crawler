import crawler
import db
from bs4 import BeautifulSoup
from multiprocessing import Pool
import util

add_house_sql = "INSERT INTO `test` (`house_id`, `href`, `area_id`, `location_id`, `community`, `age`, `size`, `layers`, `floor`, `facing`, `decorate`, `buy_time`, `years`, `unit_price`, `total_price`, `first_visit`, `7_days_watch`, `total_watch`) VALUES (%(house_id)s, %(href)s, %(area_id)s, %(location_id)s, %(community)s, %(age)s, %(size)s, %(layers)s, %(floor)s, %(facing)s, %(decorate)s, %(buy_time)s, %(years)s, %(unit_price)s, %(total_price)s, %(first_visit)s, %(7_days_watch)s, %(total_watch)s)"

@util.retry(10)
def get_location_id_by_name(location_name):
	connection = db.connect(db.config)
	with connection.cursor() as cursor:
		sql = "SELECT id FROM location WHERE name = %s"
		cursor.execute(sql, (location_name,))
		result = cursor.fetchone()[0]
	db.close(connection)
	return result

@util.retry(10)
def get_area_id_by_name(area_name):
	connection = db.connect(db.config)
	with connection.cursor() as cursor:
		sql = "SELECT id FROM area WHERE name = %s"
		cursor.execute(sql, (area_name,))
		result = cursor.fetchone()[0]
	db.close(connection)
	return result


area_list = crawler.get_all_areas()
# print(area_list)

def write_house_info(location, page):
	houses = crawler.get_one_page_house(location['href'] + '/d' + str(page))
	update_houses = []
	for house in houses:
		house['area_id'] = area['id']
		house['location_id'] = location['id']
		update_houses.append(house)
	print("Write to DB: " + area['name'] + location['name'] + str(page))
	connection = db.connect(db.config)
	with connection.cursor() as cursor:
		cursor.executemany(add_house_sql, update_houses)
		connection.commit()
		# db.write(add_house_sql, house, connection)
	db.close(connection)
		# print(house['house_id'] + ", done!")
	print("Write to DB: " + area['name'] + location['name'] + str(page) + " done!")

for area in area_list:
	area['id'] = get_area_id_by_name(area['name'])
	# print(area['name'] + ": " + str(get_area_id_by_name(area['name'])))
	location_list = crawler.get_all_locations(area)
	# print(location_list)
	for location in location_list:
		location['id'] = get_location_id_by_name(location['name'])
		# print(location['name'] + ": " + str(get_location_id_by_name(location['name'])))
		print('********************************')
		print(location['name'])
		print('********************************')
		pages = crawler.get_house_pages(location)
		p = Pool(100)
		for page in range(1, pages+1):
			p.apply_async(write_house_info, args=(location, page))
		p.close()
		p.join()
		print("location " + location['name'] + " done!")

