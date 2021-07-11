import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

####################################
#       CREATE DATABASE
####################################
def create_db():
    mycursor.execute("CREATE DATABASE Python_N_Mysql")

#########################
#   SHOW DATABASES
#########################
def show_db():
    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        print(db)

#########################
#   CREATE TABLE
#########################
def create_table():
    mycursor.execute(""" CREATE TABLE students (
                    name VARCHAR(255),
                    age Integer(10)
                    ) """)

#########################
#   SHOW TABLES
#########################
def show_table():
    mycursor.execute("SELECT * FROM students")
    data = mycursor.fetchall()
    for row in data:
        print(row)

# create_db()
show_db()
# create_table()
show_table()

################################################################33
student = ("Raj",12)
students = [("Raj",12),
            ("Rachel",22),
            ("Mike",32),
            ("John",14),
            ("Michelle",17),]

def insert_entry(stud):
    sqlFormula = "INSERT INTO students (name, age) VALUES (%s,%s)"
    mycursor.execute(sqlFormula,stud)
    mydb.commit()

insert_entry(student)
insert_entry(students)

#########################
#   Delete entry by name
#########################
def delete_entry():
    mycursor.execute("DELETE FROM students WHERE name='Mike'")
    mydb.commit()
