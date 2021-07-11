import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s,%s)"

student = ("Raj",12)

mycursor.execute(sqlFormula,student)
mydb.commit()

students = [("Raj",12),
            ("Rachel",22),
            ("Mike",32),
            ("John",14),
            ("Michelle",17),]

mycursor.executemany(sqlFormula,students)
mydb.commit()
