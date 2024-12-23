import psycopg2
import sys

# Purpose: Associate column abbr from GSOM Airport Data with abbr information. 
# Use in Command Line: 
# python3 GSOM_Abbr_Info.py tableName
# tableName is the table you want to match info with. 

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
		print("Problem with Connection")
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

def abbrToInfo(tableName):
	
    conn = connection_info()
    cur  = conn.cursor()
	
    # Grabs column names from table and associates with abbr information
    sqlQ0 = '''

        SELECT 
            column_abbr, 
            data_type,
            column_info
        FROM (
            SELECT
                column_name,
                data_type
            FROM
                information_schema.columns
            WHERE
                table_name = '%s'
		) as t1
		JOIN gsom_abbr_info t2 on t2.column_abbr = t1.column_name;
		
    ''' % (tableName)

    cur.execute(sqlQ0)
    conn.commit()

    file = cur.fetchall()

    return file


def main(tableName):
	
    file = abbrToInfo(tableName)
	
    for row in file:
        print(row)
    

    return None

if __name__ == "__main__":
	
    main(sys.argv[1])