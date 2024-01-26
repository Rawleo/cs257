from sqlalchemy import create_engine
import pandas as pd
import psycopg2

def test_connection(): 

	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="sigmondm",
		user="sigmondm",
		password="pies347cash"
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



	sql = '''
		DROP TABLE IF EXISTS uscitiestop1k;
		CREATE TABLE uscitiestop1k (
			date date,
			awnd real,
			cdsd real,
			cldd real,
			dp01 real,
			dp10 real,
			dsnd real,
			dsnw real,
			dt00 real,
			dt32 real,
			dx32 real,
			dx70 real,
			dx90 real, 
			emnt real,
			emsd real,
			emsn real,
			emxp real,
			emxt real,
			hdsd real,
			htdd real,
			prcp real,
			snow real,
			tavg real,
			tmax real,
			tmin real,
			tmin real,
			wdf1 real,
			wdf2 real,
			wdf5 real,
			wdfg real,
			wdfm real,
			wsf1 real,
			wsf2 real,
			wsf5 real,
			wsfg real,
			wsfm real	
		);
	'''
	cur.execute(sql)
	
	conn.commit()

	print("Created Cities Table!")

	return None

def importData():

	conn = connection_info()
	cur = conn.cursor()

	with open('NOAA weather data/MSP Airport GSOM.csv', 'r') as f:
		next(f)
		cur.copy_from(f, 'states', ',')
	
	conn.commit()

	print("Imported MSP Airport Data!")

	return None

def main():

	test_connection()
	createTable()
	importData()

if __name__ == "__main__":

    main()




