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
		print("Connection Worked!\n")
	else:
		print("Problem with Connection\n")
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
	sql  = '''
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
	sql  = '''
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
	sql  = '''
		SELECT * 
		FROM uscitiestop1k
		WHERE 'Minnesota' = state
		ORDER BY population ASC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0]

	return city

def findEastMost():

	conn = connection_info()
	cur  = conn.cursor()
	sql  = '''
		SELECT * 
		FROM uscitiestop1k
		ORDER BY long DESC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0:2]
	str  = city[0] + ', ' + city[1]

	return str

def findWestMost():

	conn = connection_info()
	cur  = conn.cursor()
	sql  = '''
		SELECT * 
		FROM uscitiestop1k
		ORDER BY long ASC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0:2]
	str  = city[0] + ', ' + city[1]

	return str

def findNorthMost():

	conn = connection_info()
	cur  = conn.cursor()
	sql  = '''
		SELECT * 
		FROM uscitiestop1k
		ORDER BY lat DESC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0:2]
	str  = city[0] + ', ' + city[1]

	return str

def findSouthMost():

	conn = connection_info()
	cur  = conn.cursor()
	sql  = '''
		SELECT * 
		FROM uscitiestop1k
		ORDER BY lat ASC
		LIMIT 1;
	'''

	cur.execute(sql)
	conn.commit()

	city = cur.fetchone()[0:2]
	str  = city[0] + ', ' + city[1]

	return str

def findStatePop():

	conn = connection_info()
	cur  = conn.cursor()

	while True:
		state = input("What state would you like to know the total population of that includes their most populous cities? ")

		if len(state) == 2:
			state = state.upper()
		else:
			state = state.capitalize()
		
		sql = '''

			SELECT SUM(population)
			FROM (
				SELECT *
				FROM states t1
					JOIN uscitiestop1k t2 on t2.state = t1.state
				WHERE '%s' = t1.abb
					OR '%s' = t2.state
			) as populationTable;

		''' % (state, state)

		cur.execute(sql)

		line       = cur.fetchone()
		population = line[0]
		state      = line[1]

		if line == None:
			print("Please enter a valid state name or abbreviation. \n")
			continue
			
		else:
			string = state + ": " + str(population)
			break
	
	conn.commit()

	return string

def main():

	test_connection()

	if checkExisting('Northfield', 'city', 'uscitiestop1k') == True:
		print('YES, Northfield is in uscitiestop1k.csv')
	else: 
		print('NO, Northfield is not in uscitiestop1k.csv')

	print(findMostPopulousCity(), 'is the most populous city in the USA.')
	print(findLeastPopulousCityMN(), 'is the least populous city in MN.')
	print(findEastMost(), 'is the furthest East.')	
	print(findWestMost(), 'is the furthest West.')
	print(findNorthMost(), 'is the furthest North.')
	print(findSouthMost(), 'is the furthest South.')
	print(findStatePop(), 'is the total state population according to the top 1000 cities in the USA.')

if __name__ == "__main__":

    main()