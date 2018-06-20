import mysql.connector
import re, datetime

f = open("password","r")
password = f.read()
f.close()

def gettime():
	now = datetime.datetime.now()
	print(now)

def addtosheet():
	gettime()
	
	date = now.strftime("%Y-%m-%d")
	print(date)
	
	cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='BoiseCAP073')
	cursor = cnx.cursor()

	query = ("SELECT First_name, Last_name FROM SQmembers WHERE capid={0} AND date={1};".format(userinput, date))

	cursor.execute(query)

def adduser(userinput):
	print("Adding user")
	first_name = raw_input("Please enter your First name:")
	last_name = raw_input("Please enter your Last name:")
	membertype = raw_input("Are you a cadet, senior, visiter:")

	cnx = mysql.connector.connect(user='root', password='paswsword', host='localhost', database='BoiseCAP073')
	cursor = cnx.cursor()

	query = ("INSERT INTO SQmembers (capid, First_name, Last_name, member_type) VALUES ({0}, '{1}', '{2}', '{3}');".format(userinput, first_name, last_name, membertype))

	cursor.execute(query)
	cnx.commit()
	
	cursor.close()
	cnx.close()

def readbarcode():
	userinput = raw_input("Plese enter CAP ID:")
	connect(userinput)
	
	
def connect(userinput):
	cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='BoiseCAP073')
	cursor = cnx.cursor()
	
	query = ("SELECT First_name, Last_name FROM SQmembers WHERE capid={};".format(userinput))
	
	cursor.execute(query)
	
	rows = cursor.fetchall()
	if rows == []:adduser(userinput)
	
	cursor.execute(query)
	for (Last_name) in cursor:
		name = ""
		blank = " "
		for key in Last_name:
			name = name + blank + key

		name = name + blank + userinput
		print(name)
		
	cursor.close()
	cnx.close()
	

while True:
	readbarcode()
