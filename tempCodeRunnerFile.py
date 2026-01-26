import time 
import mysql.connector 
try:
    obj1="create database Python_45_batch"
    con=mysql.connector.connect(host="localhost",user="root",password="Sidhu@369")
    cursor=con.cursor()
    cursor.execute(obj1)
    print("Database is created successfully ...")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("Exception_Name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")
