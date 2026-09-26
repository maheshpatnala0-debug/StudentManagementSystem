import mysql.connector
from mysql.connector import Error


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mahesh@89193",
        database="student_management"
    )

    if db.is_connected():
        print("Database connected successfully")

except Error as e:
    print("Database connection failed:", e)
    exit()