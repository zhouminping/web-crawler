import pymysql
import util

@util.retry(3)
def connect(config):
	return pymysql.connect(**config)

def write(sql, data, connection):
	try:
		with connection.cursor() as cursor:
			cursor.execute(sql, data)
			id = cursor.lastrowid
		connection.commit()
	except Exception as e:
		print(cursor._last_executed)
		print(e.args)
	else:
		return id

def close(connection):
	connection.close()

# add_area_sql = "INSERT INTO `area` (`name`) VALUES (%(name)s)"

# area_data = {
# 	'name': '浦东'
# }

# connection = connect_to_db(config)

# cursor = connection.cursor()

# cursor.execute(add_area_sql, area_data)

# connection.commit()

# connection.close()

# try:
# 	with connection.cursor() as cursor:
# 		sql = "INSERT INTO `area` (`name`) VALUES (%s)"
# 		cursor.execute(sql, ('浦东'))
# 	connection.commit()
# finally:
# 	connection.close()




