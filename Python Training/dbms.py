import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",password="")
print("Database connectiom established",myconn)
cur=myconn.cursor()
print("curser:",cur)

#Creating a database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE students")

#Creating table
import mysql.connector
mydb=mysql.connector.connect(host="localhost" , user="root", password=" ",database="students")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE syit (name VARCHAR(40),roll_no VARCHAR(50))")

#Show table
import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", password="",database="students")

cursor=db.cursor()

cursor.execute("SHOW TABLES")

for table_name in cursor:
   print(table_name)
