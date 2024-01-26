from sqlalchemy import create_engine
import pandas as pd
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

def createTable():

	conn = connection_info()

	cur = conn.cursor()
	dataFile = pd.read_csv('MSP_GlobalSummary_Monthly.csv')
	engine = create_engine('conn', index=False)
	dataFile.to_sql('test', engine, index=False)













	sql = '''
		DROP TABLE IF EXISTS uscitiestop1k;
		CREATE TABLE uscitiestop1k (
			station text,
			date date,
			latitude real,
			longitude real,
			elevation real,
			name text, 
			adpt real,
			adpt_attribute ,
			aslp ,
			aslp_attribute ,
			astp ,
			astp_attribute ,
			awbt ,
			awbt_attribute ,
			awnd ,
			awnd_attribute ,
			cdsd ,
			cdsd_attribute ,
			cldd ,
			cldd_attribute 
			
		);
	'''

	#cur.execute(sql)
	
	conn.commit()

	print("Created Cities Table!")

	return None

def importData():

	conn = connection_info()
	cur = conn.cursor()

	with open('states.csv', 'r') as f:
		next(f)
		cur.copy_from(f, 'states', ',')
	
	conn.commit()

	print("Imported States Data!")

	return None

def main():

	test_connection()
	createTable()
	importData()

if __name__ == "__main__":

    main()




