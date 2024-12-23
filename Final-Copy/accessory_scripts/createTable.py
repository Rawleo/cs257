from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import sys

# https://dba.stackexchange.com/questions/91966/create-a-table-from-a-csv-file-with-headers
# postgresql+psycopg2://sigmondm:pies347cash@localhost:5432/sigmondm
# connecting to sigmondm database:
# ssh into stearns and enter 
# psql -d sigmondm -U sigmondm -h localhost -p 5432
# will request for password: pies347cash
# run file in command line:
# python3 createTable.py 'FileName.csv'
# will need to remove first 5 columns up to the date column for now if the csv is fresh from NOAA.


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
		return True
	else:
		print("Problem with Connection.")
		return False

def connection_info():

	conn_info = psycopg2.connect(
		host="localhost",
		port=5432,
		database="sigmondm",
		user="sigmondm",
		password="pies347cash"
	)
	
	return conn_info

def csvFileNameToTableName(fileName):
     
    fileName  = fileName.split(' ')
    tableName = fileName[0].lower() + '_weather'

    return tableName

def dropSQLTableIfExists(tableName):

	conn = connection_info()
	cur  = conn.cursor()
	sql  = ''' DROP TABLE IF EXISTS %s; ''' % tableName

	cur.execute(sql)
	conn.commit()

	return None

def alterSQLTableAllColumnDataTypes(tableName, columnNameList):

	conn = connection_info()
	cur  = conn.cursor()
	sql  = '''
		ALTER TABLE %s
	''' % tableName

	for column in columnNameList:
		if column == 'date':
			sql += '''
				ALTER COLUMN %s TYPE text
			''' % column
		elif "attributes" in column:
			sql += '''
				ALTER COLUMN %s TYPE text
			''' % column
		else:
			sql += '''
				ALTER COLUMN %s TYPE real
			''' % column
		sql += ','

	sql = sql[:-1] + ';'

	cur.execute(sql)
	conn.commit()

	return None


def createNewTableFromCSV(fileName):

	tableName    = csvFileNameToTableName(fileName)
	filePath     = '../NOAA weather data/%s' % fileName
	file         = pd.read_csv(filePath, sep=',')
	file.columns = [column.lower() for column in file.columns]
	engine       = create_engine('postgresql+psycopg2://sigmondm:pies347cash@localhost:5432/sigmondm', echo=False)
	
	dropSQLTableIfExists(tableName)
	file.to_sql(tableName, engine, index=False)
	alterSQLTableAllColumnDataTypes(tableName, file.columns)

	print("Created Table and Imported Data for %s" % tableName)

	return None

def main(fileName):

	connection = test_connection()

	if connection == True:
		createNewTableFromCSV(fileName)
	else:
		print("Connection Failure.")
	

if __name__ == "__main__":

    main(sys.argv[1])




