import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students ORDER BY name DESC")
# mycursor.execute("SELECT * FROM students ORDER BY name")
# mycursor.execute("SELECT * FROM students ORDER BY age DESC")

data = mycursor.fetchall()
# data = mycursor.fetchone()

for row in data:
    print(row)
