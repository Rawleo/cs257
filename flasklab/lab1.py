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

def main():

	app = flask.Flask(__name__)

	@app.route('/add/<number1>/<number2>')
	def addAPI(number1, number2):
		sum = int(number1) + int(number2)
		return str(sum)

	@app.rount('/pop/<state_abbr>')
	def statePopulation(abbr):
		return None
	
	my_port = 5133
	app.run(host='0.0.0.0', port = my_port) 

if __name__ == '__main__':

	main()