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
		DROP TABLE IF EXISTS uscitiestop1k;
		CREATE TABLE uscitiestop1k (
			city text,
			state text,
			population int,
			lat real,
			long real
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
			abb text
		);
	'''

	cur.execute(sql)
	
	conn.commit()

	print("Created States Table!")

	return None

def importStatesData():

	conn = connection_info()
	cur = conn.cursor()

	with open('states.csv', 'r') as f:
		next(f)
		print(f)
		cur.copy_from(f, 'states', ',')
	
	conn.commit()

	print("Imported States Data!")

	return None

def importCitiesData():

	conn = connection_info()
	cur = conn.cursor()

	with open('us-cities-top-1k.csv', 'r') as f:
		next(f)
		cur.copy_from(f, 'uscitiestop1k', ',')
	
	conn.commit()

	print("Imported Cities Data!")

	return None

def main():

	test_connection()
	createCitiesTable()
	createStatesTable()
	importStatesData()
	importCitiesData()

if __name__ == "__main__":

    main()




