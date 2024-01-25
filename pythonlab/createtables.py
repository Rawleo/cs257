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

def createCitiesTable():

	conn = connection_info()

	cur = conn.cursor()

	sql = '''
		DROP TABLE IF EXISTS usCitiesTop1K;
		CREATE TABLE usCitiesTop1K (
			city text,
			state text,
			population int,
			lat real,
			lon real
		);
	'''

	cur.execute(sql)
	
	conn.commit()

	print("Created Cities Table!")

	return None

def createStatesTable():

	conn = connection_info()

	cur = conn.cursor()

	sql = '''
		DROP TABLE IF EXISTS states;
		CREATE TABLE states (
			state text,
			abbreviation text
		);
	'''

	cur.execute(sql)
	
	conn.commit()

	print("Created States Table!")

	return None

def importStatesData():

	conn = connection_info()
	cur = conn.cursor()

	cur.copy_from('states.csv')
	
	conn.commit()

	print("Imported States Data!")

	return None

def importCitiesData():

	conn = connection_info()

	cur = conn.cursor()

	sql = '''

		COPY usCitiesTop1K FROM 'us-cities-top-1k.csv' DELIMITER ',' CSV
		
	'''

	cur.execute(sql)
	
	conn.commit()

	print("Imported Cities Data!")

	return None

def main():

	test_connection()
	createCitiesTable()
	createStatesTable()
	importStatesData()

if __name__ == "__main__":

    main()




