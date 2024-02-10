import flask
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
		print("\nConnection Worked!\n")
	else:
		print("\nProblem with Connection\n")
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

# adapted from my cityquery.py in pythonlab
def getStatePopulation(abbr):

	conn = connection_info()
	cur  = conn.cursor()

	state = abbr

	if len(state) == 2:
		state = state.upper()
	else:
		state = state.capitalize()
	
	sql = '''
		SELECT t1.state, t1.population
		FROM state_populations t1
		WHERE '%s' = t1.code
			OR '%s' = t1.state
	''' % (state, state)

	cur.execute(sql)

	line = cur.fetchone()

	if line == None:
		string = 'Please enter a valid state name or abbreviation in the site address.'
		return string

	state      = line[0]
	population = line[1]
	string     = state + "'s Population: " + str(population)

	conn.commit()

	return string

app = flask.Flask(__name__)

@app.route('/add/<number1>/<number2>')
def addAPI(number1, number2):
	sum = int(number1) + int(number2)
	return str(sum)

@app.route('/pop/<abbr>')
def statePopulation(abbr):
	population = getStatePopulation(abbr)
	return str(population)

def main():
	
	my_port = 5133
	app.run(host='0.0.0.0', port = my_port) 

if __name__ == '__main__':

	main()