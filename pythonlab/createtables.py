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

def main():

	test_connection()
	createCitiesTable()
	createStatesTable()

if __name__ == "__main__":

    main()




