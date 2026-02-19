# operations which will give boolean operation
# import time
# f1=open("A1.txt","r")
# print("=== File Information ===")
# print("File Name is:",f1.name)
# print("File Mode is:",f1.mode)
# print("File Closed is:",f1.closed)
# print("File is Readable:",f1.readable())
# print("File is Writeable is:",f1.writable())
# print()
# f1.close()
# time.sleep(2)
# print("End of an Application")

# Read and Write Operation
# import time
# f1=open("A1.txt","r+")
# print("=== File Information ===")
# print("File name is:",f1.name)
# print("File Mode is:",f1.mode)
# print("File Closed is:",f1.closed)
# print("File is Readable:",f1.readable())
# print("File is writable:",f1.writable())
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of An Application")


# writable operation
# import time
# f1=open("A1.txt","w")
# print("=== File Information ===")
# print("File name is:",f1.name)
# print("File Mode is:",f1.mode)
# print("File Closed is:",f1.closed)
# print("File is Readable:",f1.readable())
# print("File is writable:",f1.writable())
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of An Application")

# Write and Read mode 
# import time
# f1=open("A1.txt","w+")
# print("=== File Information ====")
# print("File Name is:",f1.name)
# print("File Mode is:",f1.mode)
# print("File Closed is:",f1.closed)
# print("File Readable is:",f1.readable())
# print("File Writable is:",f1.writable())
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of An Application")

# # Without any mode
# import time
# f1=open("A1.txt")
# print("=== File Information ====")
# print("File Name is:",f1.name)
# print("File Mode is:",f1.mode)
# print("File Closed is:",f1.closed)
# print("File Readable is:",f1.readable())
# print("File Writable is:",f1.writable())
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of An Application")

# Write mode to add content
# It Will Give Error
# import time
# f2=open("A2.txt","w")
# f2.write(12345)
# f2.write(54321)
# f2.write(11223)
# f2.write(32211)
# print()
# print("A new file created with its content successfully")
# print()
# f2.close()
# print()
# time.sleep(2)
# print("End of An Application")

# It Will Give correct Output
# import time
# f2=open("A2.txt","w")
# f2.write("12345")
# f2.write("54321")
# f2.write("11223")
# f2.write("32211")
# print()
# print("A new file created with its content successfully")
# print()
# f2.close()
# print()
# time.sleep(2)
# print("End of An Application")

# Write() with correct mode in new line
# import time 
# f2=open("A2.txt","w")
# f2.write("12345\n")
# f2.write("54321\n")
# f2.write("11223\n")
# f2.write("32211\n")
# print()
# print("A new file is created with it's content successfully")
# print()
# f2.close()
# print()
# time.sleep(2)
# print("End of an application")

# Append mode
# import time 
# f2=open("A2.txt","a")
# f2.write("12345\n")
# f2.write("54321\n")
# f2.write("22331\n")
# f2.write("77661\n")
# print()
# print("A new file is created with it's content successfully")
# print()
# f2.close()
# print()
# time.sleep(2)
# print("End of an application")

# Exclusive mode
# import time 
# f2=open("A2.txt","x")
# f2.write("12345\n")
# f2.write("54321\n")
# f2.write("22331\n")
# f2.write("77661\n")
# print()
# print("A new file is created with it's content successfully")
# print()
# f2.close()
# print()
# time.sleep(2)
# print("End of an application")

# Writelines() mode
# it will give error because it writelines takes strings only 
# import time 
# f3=open("A4.txt","w")
# L1=[1001,"MObile_1",23000.0,"Samsung"]
# f3.writelines(L1)
# print()
# print("A file is created successfully ...")
# print()
# f3.close()
# print()
# time.sleep(2)
# print("End of an application")

# It will correct output because here it has strings
# import time 
# f3=open("A4.txt","w")
# L1=["1001\n","MObile_1\n","23000.0\n","Samsung\n"]
# f3.writelines(L1)
# print()
# print("A file is created successfully ...")
# print()
# f3.close()
# print()
# time.sleep(2)
# print("End of an application")

# Example 3 
# import time
# f1=open("A5.txt","w")
# L1=["1001\n","Mobile_1\n","23000\n","Samsung\n"]
# L2=["1002\n","Mobile_2\n","24000\n","Samsung\n"]
# L3=["1003\n","Mobile_3\n","25000\n","Samsung\n"]
# L4=["1004\n","Mobile_4\n","26000\n","Samsung\n"]
# f1.writelines(L1,L2,L3,L4)
# print()
# print("A file is created is created successfully....")
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of An Application")

# Example 4
# import time
# f1=open("A5.txt","w")
# L1=["1001\n","Mobile_1\n","23000.0\n","Samsung\n"]
# L2=["1002\n","Mobile_2\n","24000.0\n","Samsung\n"]
# L3=["1003\n","Mobile_3\n","25000.0\n","Samsung\n"]
# L4=["1004\n","Mobile_4\n","26000.0\n","Samsung\n"]
# f1.writelines(L1)
# f1.writelines(L2)
# f1.writelines(L3)
# f1.writelines(L4)
# print("A file is created Successfully....")
# f1.close()
# time.sleep(2)
# print("End of an Application")

# Reading the file
# # Example 10 on Using Read() 
# import time
# f1=open("A5.txt","r")
# print("===============")
# print("File Name is:",f1.name)
# print("================")
# obj1=f1.read()
# print(obj1)
# print()
# time.sleep(2)
# print("End of An Application")

# To read Specific Character
# import time 
# f1=open("A5.txt","r")
# print("======================")
# print("File_Name is:",f1.name)
# print("========================")
# obj1=f1.read(19)
# print(obj1)
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# To read one line file
# import time 
# f1=open("A5.txt","r")
# print("======================")
# print("File_Name is:",f1.name)
# print("========================")
# obj1=f1.readline()
# print(obj1)
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# Example 4
# import time 
# f1=open("A5.txt","r")
# print("======================")
# print("File_Name is:",f1.name)
# print("========================")
# obj1=f1.readlines()
# print(obj1)
# print()
# print(type(obj1))
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# Example 5
# import time 
# f1=open("A5.txt","r")
# print("======================")
# print("File_Name is:",f1.name)
# print("========================")
# obj1=f1.readlines()
# for x1 in obj1:
#     print(x1)
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# # Example 6
# import time 
# f1=open("A5.txt","r")
# print("======================")
# print("File_Name is:",f1.name)
# print("========================")
# obj1=f1.readlines()
# for x1 in obj1:
#     print(x1,end="")
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# Example 7
# import time 
# f1=open("A5.txt","r")
# for x1 in f1:
#     print(x1)
# f1.close()
# print()
# time.sleep(2)
# print('End of an application')

# Example 8
# import time 
# f1=open("A5.txt","r")
# for x1 in f1:
#     print(x1,end="")
# f1.close()
# print()
# time.sleep(2)
# print('End of an application')


#  tell() function
# # Example 1
# import time 
# f1=open("A5.txt","r")
# res1=f1.tell()
# print("Current_File_Pointer Position is:",res1)
# print()
# res2=f1.read(6)
# print(res2)
# print()
# res3=f1.tell()
# print("Current_File_Pointer Position is:",res3)
# print()
# f1.close()
# print()
# time.sleep(2)
# print('End of an application')

# # Seek() Fucntion
# import time 
# f1=open("A5.txt","r")
# obj1=f1.tell()
# print("Current_file_pointer is:",obj1)
# print()
# obj2=f1.read(19)
# print(obj2)
# print()
# obj3=f1.tell()
# print("Current_file_pointer is:",obj3)
# print()
# obj4=f1.seek(0)
# print("Current_file_pointer is:",obj4)
# print()
# obj5=f1.read(19)
# print(obj5)
# print()
# f1.close()
# print()
# time.sleep(2)
# print("End of an application")

# Creating a file with "with_statement"
import time 
with open("A5.txt","r") as f:
    print("===File_Information===")
    print("File_name is:",f.name)
    print("File_Mode is:",f.mode)
    print("File_Closed:",f.closed)
    print("File is readable:",f.readable())
    print("File is writable or not:",f.writable())
print()
time.sleep(2)
print("End of an application")