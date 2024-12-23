import psycopg2
import sys

def csvFileNameToTableName(fileName):
     
    fileName  = fileName.split(' ')
    tableName = fileName[0].lower() + '_weather'

    return tableName

def main(fileName):

    print(csvFileNameToTableName(fileName))
	
    return None

if __name__ == "__main__": 
      
    main(sys.argv[1])