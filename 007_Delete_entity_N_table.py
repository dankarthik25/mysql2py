import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

def show_table():
    mycursor.execute("SELECT * FROM students")
    data = mycursor.fetchall()
    # data = mycursor.fetchone()
    for row in data:
        print(row)

# ########################
#  DELETE ENTITY
# ######################3
mycursor.execute("DELETE FROM students WHERE name='Mike'")
mydb.commit()

# ########################
#  DELETE TABLE
# ######################3
mycursor.execute("DELETE TABLE IF EXISTS students")
mydb.commit()
