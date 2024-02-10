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

		SELECT SUM(population)
		FROM (
			SELECT *
			FROM states t1
				JOIN uscitiestop1k t2 on t2.state = t1.state
			WHERE '%s' = t1.abb
				OR '%s' = t2.state
		) as populationTable;

	''' % (state, state)

	cur.execute(sql)

	line       = cur.fetchone()
	population = line[0]
	state      = state

	if population == None:
		string = 'Please enter a valid state name or abbreviation.'
		return string

	sql = '''
		SELECT *
		FROM states
		WHERE '%s' = abb 
			OR '%s' = state
	''' % (state, state)

	cur.execute(sql)

	state  = cur.fetchone()[0]
	string = state + ": " + str(population)

	conn.commit()

	return string


def main():

	app = flask.Flask(__name__)

	@app.route('/add/<number1>/<number2>')
	def addAPI(number1, number2):
		sum = int(number1) + int(number2)
		return str(sum)

	@app.route('/pop/<abbr>')
	def statePopulation(abbr):
		population = getStatePopulation(abbr)
		return str(population)
	
	my_port = 5133
	app.run(host='0.0.0.0', port = my_port) 

if __name__ == '__main__':

	main()