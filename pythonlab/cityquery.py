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
	cur  = conn.cursor()
	
	sql = '''
		SELECT CASE WHEN EXISTS (
			SELECT %s 
			FROM %s 
			WHERE '%s' ~ %s
		) 
		THEN CAST(1 AS BIT) 
		ELSE CAST(0 AS BIT) 
		END;
    ''' % (columnName, tableName, itemName, columnName)

	cur.execute(sql)
	conn.commit()
	exists = int(cur.fetchone()[0])
	if exists == 1:
		return True
	else:
		return False
	
def findMostPopulousCity():

	conn = connection_info()
	cur  = conn.cursor()

	sql = '''
		SELECT * 
		FROM uscitiestop1k
		ORDER BY population DESC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0]

	return city

def findLeastPopulousCityMN():

	conn = connection_info()
	cur  = conn.cursor()

	sql = '''
		SELECT * 
		FROM uscitiestop1k
		WHERE 'Minnesota' = state
		ORDER BY population ASC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0]

	print(city)

	return city


def main():

	test_connection()
	if checkExisting('Northfield', 'city', 'uscitiestop1k') == True:
		print('YES, Northfield is in uscitiestop1k.csv')
	else: 
		print('NO, Northfield is not in uscitiestop1k.csv')
	print(findMostPopulousCity(), 'is the most populous city.')
	print(findLeastPopulousCityMN, 'is the least populous city in MN.')


if __name__ == "__main__":

    main()