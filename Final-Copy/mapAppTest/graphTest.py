import psycopg2
import numpy as np 
import matplotlib.pyplot as plt  

def connection_info():

	conn_info = psycopg2.connect(
		host="localhost",
		port=5432,
		database="sigmondm",
		user="sigmondm",
		password="pies347cash"
	)
	
	return conn_info

