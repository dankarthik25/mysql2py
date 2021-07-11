import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students")
# ######################33333
#   Limit : entry
# #########################333
# mycursor.execute("SELECT * FROM students LIMIT 5")

# #########################3##
#   OFFSET : entry
# #########################
# mycursor.execute("SELECT * FROM students LIMIT 5 OFFSET 2")

data = mycursor.fetchall()
# data = mycursor.fetchone()

for row in data:
    print(row)
