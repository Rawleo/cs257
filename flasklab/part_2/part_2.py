from flask import Flask
from flask import render_template
import random

def main():
    
    app = Flask(__name__)

    @app.route('/')
    def welcome():
        return render_template("index.html")

    @app.route('/rand/<low>/<high>')
    def rand(low, high):
        low_int = int(low)
        high_int = int(high)
        
        num = random.randint(low_int, high_int)
        return render_template("character_generator.html", randNum = num)
    
    @app.route()
    def random_adjective():
        num = rand

    my_port = 5133
    app.run(host='0.0.0.0', port = my_port) 

if __name__ == '__main__':

    main()