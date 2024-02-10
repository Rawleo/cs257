from flask import Flask
from flask import render_template
import random
import psycopg2
    
def connection_info():

	conn_info = psycopg2.connect(
                host="localhost",
                port=5432,
                database="sonr",
                user="sonr",
                password="pies967beach"
	)
	
	return conn_info

def test_connection(): 

	conn = connection_info()

	if conn is not None:
		print("\nConnection to PostgreSQL Worked!\n")
	else:
		print("\nProblem with PostgreSQL Connection.\n")
	return None

def getName(pos):

    conn = connection_info()
    cur  = conn.cursor()
    sql  = '''SELECT name FROM characters ORDER BY name ASC LIMIT 1 OFFSET %s;''' % (pos - 1)

    cur.execute(sql)
    conn.commit()

    line = cur.fetchone()
    name = line[0]

    return name

def getAdjective(pos):
    
    conn = connection_info()
    cur  = conn.cursor()
    sql  = '''SELECT word FROM adjectives ORDER BY word ASC LIMIT 1 OFFSET %s;''' % (pos - 1)

    cur.execute(sql)
    conn.commit()

    line = cur.fetchone()
    adj  = line[0]

    return adj

def getRandomLocation():
    
    conn = connection_info()
    cur  = conn.cursor()
    sql  = '''SELECT city, state FROM uscitiestop1k ORDER BY city ASC;'''

    cur.execute(sql)
    conn.commit()

    line  = cur.fetchall()
    indx  = random.randint(1, len(line)) - 1
    city  = line[indx][0]
    state = line[indx][1]
    text  = city + ', ' + state

    return text

def getRandomYear():
    year = random.randint(1950,2020)
    return year

# Flask 
app = Flask(__name__)

@app.route('/')
def welcome():

    return render_template("index.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):

    low_int  = int(low)
    high_int = int(high)
    num0     = random.randint(low_int, high_int)
    num1     = random.randint(low_int, high_int)
    name     = getName(num0).capitalize()
    adj      = getAdjective(num1).capitalize()
    location = getRandomLocation()
    year     = getRandomYear()

    return render_template("character_generator.html", randName = name, randAdj = adj, randLocation = location, randYear = year)

def main():

    test_connection()
    my_port = 5133
    app.run(host='0.0.0.0', port = my_port) 

if __name__ == '__main__':

    main()