import psycopg2
import sys

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

def joinCityPopStatePopTables(state):
	
    conn = connection_info()
    cur  = conn.cursor()
	
    if len(state) == 2:
        state = state.upper()
    else:
        state = state.capitalize()
	
    sqlQ0 = '''

        DROP VIEW IF EXISTS %s_pop_with_cities;
        CREATE VIEW %s_pop_with_cities AS
        SELECT 
            t3.state_1 as state, 
            t3.abb,
            t3.city,
            CAST(t3.city_pop as REAL), 
            t3.lat, 
            t3.long, 
            t4.population as state_pop,
            (t3.city_pop / t4.population) as percent_pop
        FROM (
            SELECT *
            FROM states t1
                JOIN uscitiestop1k t2 on t2.state = t1.state
            WHERE '%s' = t1.abb
                OR '%s' = t2.state
        ) as t3 (state_1, abb, city, state_2, city_pop, lat, long)
            JOIN state_populations t4 on t3.abb = t4.code
        ;

        SELECT abb, city, ROUND(CAST(((city_pop * 100) / state_pop)), 2) AS percent_pop FROM state_pop_with_cities ORDER BY percent_pop DESC LIMIT 10;

    ''' % (state, state, state, state)

    # SELECT abb, city, ROUND(CAST(((city_pop * 100) / state_pop) AS DECIMAL(20,4)), 2) AS percent_pop FROM state_pop_with_cities ORDER BY percent_pop DESC LIMIT 10;
	
    cur.execute(sqlQ0)
    conn.commit()

    file = cur.fetchall()
	
    return file

def main(stateName):
	
    file = joinCityPopStatePopTables(stateName)

    for row in file:
        print(row)

    return None

if __name__ == "__main__":
	
    main(sys.argv[1])