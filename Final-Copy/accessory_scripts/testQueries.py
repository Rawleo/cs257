import psycopg2
# For excluding null and empty cells use: WHERE columnName = null AND columnName = ""


def test_connection():
    connectionToServer = psycopg2.connect(
        host="localhost",
        port=5432,
        database="sigmondm",
        user="sigmondm",
        password="pies347cash"
    )

    if connectionToServer is not None:
        print("Connection Worked!")
        return True
        connectionToServer.close()
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

conn = test_connection()
if conn == True:
    conn = connection_info()
    cur = conn.cursor()
    print("Getting the average temperature at MSP in January and the average temperature in July.")
    cur.execute("SELECT AVG(tavg) FROM msp_weather WHERE date LIKE '%-01';")
    result = cur.fetchone()
    print("The average in January is", result[0])
    cur.execute("SELECT AVG(tavg) FROM msp_weather WHERE date LIKE '%-07';")
    result = cur.fetchone()
    print("The average in July is", result[0])
    print("Doing the same for ATL.")
    cur.execute("SELECT AVG(tavg) FROM atl_weather WHERE date LIKE '%-01';")
    result = cur.fetchone()
    print("The average in January is", result[0])
    cur.execute("SELECT AVG(tavg) FROM atl_weather WHERE date LIKE '%-07';")
    result = cur.fetchone()
    print("The average in July is", result[0])
    print("And now for BOS.")
    cur.execute("SELECT AVG(tavg) FROM bos_weather WHERE date LIKE '%-01';")
    result = cur.fetchone()
    print("The average in January is", result[0])
    cur.execute("SELECT AVG(tavg) FROM bos_weather WHERE date LIKE '%-07';")
    result = cur.fetchone()
    print("The average in July is", result[0])
    cur.execute("SELECT * FROM msp_weather WHERE snow > 0 ORDER BY snow DESC FETCH FIRST 5 ROWS ONLY;")
    print("These are the five snowiest months recorded at MSP:")
    result = cur.fetchall()
    for i in result:
        print(i[0], ":", i[21], "inches")
else:
    print("Connection has failed! Check your details")
conn.close()
