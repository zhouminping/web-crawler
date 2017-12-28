import db
import crawler

connection = db.connect(util.config)

add_area_sql = "INSERT INTO `area` (`name`, `href`) VALUES (%(name)s, %(href)s)"
add_location_sql = "INSERT INTO `location` (`name`, `href`, `area_id`) VALUES (%(name)s, %(href)s, %(area_id)s)"

area_list = crawler.get_all_areas()

for area in area_list:
	area_id = db.write(add_area_sql, area, connection)
	location_list = crawler.get_all_locations(area)
	for location in location_list:
		location['area_id'] = area_id
		db.write(add_location_sql, location, connection)

db.close(connection)