# import time 
# import mysql.connector 
# try:
#     obj1="create database Python_45_batch"
#     con=mysql.connector.connect(host="localhost",user="root",password="Sidhu@369")
#     cursor=con.cursor()
#     cursor.execute(obj1)
#     print("Database is created successfully ...")
# except mysql.connector.DatabaseError as e:
#     if con:
#         con.rollback()
#         print("Exception_Name is:",e)
# finally:
#     if cursor:
#         cursor.close()
#     elif con:
#         con.close()
# print()
# time.sleep(2)
# print("End of an application")


# import time
# import mysql.connector

# try:
#     obj1 = "CREATE DATABASE IF NOT EXISTS Python_45_Batch"
    
#     # ✅ Connect with compatible auth plugin
#     con = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Sidhu@369",
#         auth_plugin='mysql_native_password'  # force MySQL 8 compatibility
#     )

#     cursor = con.cursor()
#     cursor.execute(obj1)
#     print("Database is created successfully ...")

# except mysql.connector.DatabaseError as e:
#     # Rollback only if connection exists
#     if 'con' in locals() and con.is_connected():
#         con.rollback()
#     print("Exception_Name is:", e)

# finally:
#     # Close cursor and connection safely
#     if 'cursor' in locals() and cursor:
#         cursor.close()
#     if 'con' in locals() and con.is_connected():
#         con.close()
#         print("Connection closed")

# print()
# time.sleep(2)
# print("End of an application")


# inserting data in tables
# import time
# import mysql.connector

# con = None
# cursor = None

# try:
#     con = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Sidhu@369",  # put your actual password here
#         database="Python_45_Batch",
#         auth_plugin='mysql_native_password'
#     )
#     cursor = con.cursor()
#     sql = "CREATE TABLE Products(Pid INT, Pname VARCHAR(25), Price INT)"
#     cursor.execute(sql)
#     print("Table is created successfully")
# except mysql.connector.DatabaseError as e:
#     print("Exception_Name is:", e)
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()

# time.sleep(2)
# print("End of an application")

import time 
import mysql.connector
try:
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sidhu@369",
    )
    cursor=con.cursor()
    cursor.execute("CREATE DATABASE Python_45_batch")
    print("Database Created Successfully............")
except mysql.connector.DatabaseError as e:
    print("Error is:",e)
finally:
    if con:
        con.close()