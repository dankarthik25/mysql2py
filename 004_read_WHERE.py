# where and like

import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students WHERE age =12")

# # ###############################3
#   Wild Card
# # ################################3333
mycursor.execute("SELECT * FROM students WHERE name Like 'Mi%' ")
mycursor.execute("SELECT * FROM students WHERE name Like '%ac%' ")

data = mycursor.fetchall()
# data = mycursor.fetchone()

for row in data:
    print(row)
