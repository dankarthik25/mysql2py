import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()
def read_table():
    mycursor.execute("SELECT * FROM students")
    data = mycursor.fetchall()
    # data = mycursor.fetchone()
    for row in data:
        print(row)

print("Table before Update")
read_table()
mycursor.execute("UPDATE students SET age=13 WHERE name = 'Raj'")
mydb.commit()

print("Table after Update")
read_table()
