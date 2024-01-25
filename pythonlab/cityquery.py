import psycopg2

def test_connection(): 

	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="sonr",
		user="sonr",
		password="pies967beach"
	)

	if conn is not None:
		print("Connection Worked!")
	else:
		print("Problem with Connection")
	return None

def connection_info():

	conn_info = psycopg2.connect(
                host="localhost",
                port=5432,
                database="sonr",
                user="sonr",
                password="pies967beach"
	)
	
	return conn_info

def checkExisting(itemName, columnName, tableName):

	conn = connection_info()
	cur = conn.cursor()
	
	sql = '''
		SELECT CASE WHEN EXISTS (
			SELECT %s 
			FROM %s 
			WHERE '%s' ~ %s
		) 
		THEN CAST(1 AS BIT) 
		ELSE CAST(0 AS BIT) 
		LIMIT 1
		END;
    ''', (columnName, tableName, itemName, columnName)

	cur.execute(sql, vars)
	exists = int(cur.fetchone())

	# if exists == 1:
	# 	return True
	# else:
	# 	return False


def main():

	test_connection()
	checkExisting('Northfield', 'city', 'uscitiestop1k')
	# if checkExisting('Northfield', 'city', 'uscitiestop1k'):
	# 	print('YES')
	# else: 
	# 	print('NO')


if __name__ == "__main__":

    main()