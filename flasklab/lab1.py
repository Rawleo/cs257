import flask

app = flask.Flask(__name__)

@app.route('/add/<number1>/<number2>')
def addAPI(number1, number2):
    sum = int(number1) + int(number2)
    return str(sum)

if __name__ == '__main__':
    my_port = 5133
    app.run(host='0.0.0.0', port = my_port) 