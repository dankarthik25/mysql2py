import mysql.connector

# Source :
# https://www.youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G

#########################
#   CONNECT MYSQL Server (host,user,passwd)
#########################

#       run mysql server before running connector
# mydb = mysql.connector.connect(
#         host="localhost",
#         user = "root",
#         passwd=""
#         )
# print(mydb)

####################################
#       CREATE DATABASE
####################################

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Python_N_Mysql")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

#########################
#   CONNECT DATABASE in MYSQL Server (host,user,passwd,database)
#########################

mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        passwd="",
        database = "Python_N_Mysql"
        )
mycursor = mydb.cursor()

#########################
#   SHOW DATABASES
#########################

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

#########################
#   CREATE TABLE
#########################

# mycursor.execute(""" CREATE TABLE students (
#                 name VARCHAR(255),
#                 age Integer(10)
#                 ) """)

#########################
#   SHOW TABLES
#########################
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
