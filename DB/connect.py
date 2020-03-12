import mysql.connector 

mydb = mysql.connector.connect(host="localhost", user="root",passwd="root123")

myCursor = mydb.cursor()

myCursor.execute("show Databases")

for i in myCursor:
    print(i)