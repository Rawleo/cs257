import psycopg2
import numpy as np 
import matplotlib.pyplot as plt  

def connection_test():

	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="sigmondm",
		user="sigmondm",
		password="pies347cash"
	)
	
	return conn

connection = connection_test()
myCursor = connection.cursor()
myCursor.execute("SELECT date, tavg FROM msp_weather;")
result = myCursor.fetchall()

Date = [1,2,3,4,5,6,7,8,9,10]
tavg = [30, 55, 70, 69, 90, -12, 39, -8, 44, 105]
 
#for i in myCursor:
 #   Date.append(i[0])
  #  tavg.append(i[1])
     
#print("Date = ", Date)
#print("Average Temp = ", tavg)
 
 
# Visualizing Data using Matplotlib
plt.plot(Date, tavg)
plt.show()





