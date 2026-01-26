# Example 1
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
# p1=product_class(190)
# print(p1)
# print()
# time.sleep(2)
# print("End of An Application")


# Example 2
# import time 
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
# p1=product_class(190)
# print("Number of items in p1 is:",p1)
# print()
# time.sleep(2)
# print("End of An Application")


# Example 3
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __add__(self,other):
#         return self.items+other.items
# p1=product_class(190)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(200)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1+p2)
# print()
# time.sleep(2)
# print("End of an application")


# Example 4
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __mul__(self,other):
#         return self.items*other.items
# p1=product_class(190)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(200)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1*p2)
# print()
# time.sleep(2)
# print("End of an application")

#example 5
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __truediv__(self,other):
#         return self.items/other.items
# p1=product_class(190)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(200)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1/p2)
# print()
# time.sleep(2)
# print("End of an application")

# Example 6
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __sub__(self,other):
#         return self.items-other.items
# p1=product_class(190)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(200)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1-p2)
# print()
# time.sleep(2)
# print("End of an application")

# Example 7
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __mod__(self,other):
#         return self.items%other.items
# p1=product_class(10)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(5)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1%p2)
# print()
# time.sleep(2)
# print("End of an application")

# Example 8
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __pow__(self,other):
#         return self.items**other.items
# p1=product_class(5)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(2)
# print("Number of items in p2 is:",p2)
# print()
# print("The result set is:",p1**p2)
# print()
# time.sleep(2)
# print("End of an application")

# Example 9
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __add__(self,other):
#         obj1=self.items+other.items
#         p1=product_class(obj1)
#         return p1
# p1=product_class(30)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(5)
# print("Number of items in p2 is:",p2)
# print()
# p3=product_class(15)
# print("Number of items in p3 is:",p3)
# print()
# p4=product_class(23)
# print("Number of items in p4 is:",p4)
# print()
# p5=product_class(27)
# print("Number of items in p4 is:",p5)
# print()
# print("The result set is:",p1+p2+p3+p4+p5)
# time.sleep(2)
# print("End of an application")

#Example 10
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __iadd__(self,others):
#         return self.items+others.items
# p1=product_class(30)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(5)
# print("Number of items in p2 is:",p2)
# print()
# p1+=p2
# print("The result set is:",p1)
# print()
# time.sleep(3)
# print("End of an Application")

# Example 11
# import time
# class product_class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __imul__(self,others):
#         return self.items*others.items
# p1=product_class(30)
# print("Number of items in p1 is:",p1)
# print()
# p2=product_class(5)
# print("Number of items in p2 is:",p2)
# print()
# p1*=p2
# print("The result set is:",p1)
# print()
# time.sleep(2)
# print("End of an application")


# Method Overloading
# Example 1
# import time
# class A_class:
#     def m1(self):
#         print("0's number of arguement")
#     def m1(self,x1):
#         print("1's number of arguement")
#     def m1(self,x1,x2):
#         print("2's number of arguement")
#     def m1(self,x1,x2,x3):
#         print("3's number of arguements")
# a1=A_class()
# a1.m1()
# print()
# a1.m1(1000)
# print()
# a1.m1(1000,2000)
# print()
# a1.m1(1000,2000,3000)
# print()
# time.sleep(2)
# print("Emd of an application")

# Example 2
# import time
# class A_class:
#     def m1(self):
#         print("0's number of arguement")
#     def m1(self,x1):
#         print("1's number of arguement")
#     def m1(self,x1,x2):
#         print("2's number of arguement")
#     def m1(self,x1,x2,x3):
#         print("3's number of arguements")
# a1=A_class()
# a1.m1(1000,2000,3000)
# print()
# time.sleep(2)
# print("Emd of an application")

# Method overloading using default argument
# import time
# class A_class:
#     def m1(self,obj1=None,obj2=None,obj3=None):
#         if(obj1!=None and obj2!=None and obj3!=None):
#             print("Sum of three number of arguments:",obj1+obj2+obj3)
#         elif(obj1!=None and obj2!=None):
#              print("Sum of two number of arugments:",obj1+obj2)
#         else:
#             print("only allow three or two number of arugments")
# a1=A_class()
# a1.m1(10,20,30)
# print()
# a1.m1(10,20)
# print()
# a1.m1(10)
# print()
# time.sleep(2)
# print("End of an application")


# Method overloading using variable length argument

# Example 1
# import time
# class A_class:
#     def m1(self,*x1):
#         print(x1)
# a1=A_class()
# a1.m1()
# a1.m1(10)
# a1.m1(10,20)
# a1.m1(10,20,30)
# a1.m1(10,20,30,40)
# print()
# time.sleep(2)
# print("End of an Application")

# Example 2
# import time
# class A_class:
#     def m1(self,*x1):
#         for x1 in x1:
#             print(x1)
# a1=A_class()
# a1.m1()
# a1.m1(10)
# a1.m1(10,20)
# a1.m1(10,20,30)
# a1.m1(10,20,30,40)
# print()
# time.sleep(2)
# print("End of an application")

# Example 3
# import time
# class A_class:
#     def m1(self,*x1):
#         s1=0
#         for a1 in x1:
#             s1+=a1
#         print("Sum of an arguments:",s1)
# a1=A_class()
# a1.m1()
# a1.m1(10)
# a1.m1(10,20)
# a1.m1(10,20,30)
# a1.m1(10,20,30,40)
# print()
# time.sleep(2)
# print("End of an Application")

# Example 4
# import time
# class A_class:
#     def m1(self,*x1):
#         for a1 in x1:
#             print(a1)
# a1=A_class()
# a1.m1(1001,"Mobile_1",23000.0,"Samsung")
# print()
# a1.m1(1002,"Mobile_2",25000.0,"Samsung")
# print()
# time.sleep(2)
# print("End of an Application")

# Constructor Overloading

# Example 1
# import time 
# class A_class:
#     def __init__(self):
#         print('0-number of argument')
#     def __init__(self,a1):
#         print('1-number of argument')
#     def __init__(self,a1,a2):
#         print('2-number of argument')
#     def __init__(self,a1,a2,a3):
#         print('3-number of argument')
# a1=A_class()
# print()
# a1=A_class(10)
# print()
# a1=A_class(10,20)
# print()
# a1=A_class(10,20,30)
# print()
# time.sleep(2)
# print("End of an application")

# Example 2
# import time 
# class A_class:
#     def __init__(self):
#         print('0-number of argument')
#     def __init__(self,a1):
#         print('1-number of argument')
#     def __init__(self,a1,a2):
#         print('2-number of argument')
#     def __init__(self,a1,a2,a3):
#         print('3-number of argument')
# a1=A_class(10,20,30)
# print()
# time.sleep(2)
# print("End of an application")

# Constructor overloading using default arguments
# import time 
# class A_class:
#     def __init__(self,a1=None,a2=None,a3=None):
#         print("Constructor overloading using default argument")
# a1=A_class(10,20,30)
# print()
# a1=A_class(10,20)
# print()
# a1=A_class(10)
# print()
# time.sleep(2)
# print("End of an application")

# Method overloading using variable length argument
# import time 
# class A_class:
#     def __init__(self,*a1):
#         print("Constructor overloadind using variable_length argument")
# a1=A_class()
# print()
# a1=A_class(10)
# print()
# a1=A_class(10,20)
# print()
# a1=A_class(10,20,30)
# print()
# a1=A_class(10,20,30,40)
# print()
# a1=A_class(10,20,30,40,50)
# print()
# time.sleep(2)
# print("End of an application")


# Method overloading and constructor overloading
# import time
# class product_class_1:
#     def __init__(self,pid,pname):
#         self.pid=pid
#         self.pname=pname
#     def m1(self):
#         print("Pid is:",self.pid)
#         print("Pname is:",self.pname)
# class product_class_2(product_class_1):
#     def __init__(self, pid, pname,price,company,M_date,exp_date):
#         super().__init__(pid, pname)
#         self.price=price
#         self.company=company
#         self.M_date=M_date
#         self.exp_date=exp_date
#     def m2(self):
#         super().m1()
#         print("Price is:",self.price)
#         print("Company is:",self.company)
#         print("M_date is:",self.M_date)
#         print("Exp_date is:",self.exp_date)
# p1=product_class_2(1001,"Mobile_1",23000,"Samsung","12/07/2025","12/07/2025")
# p1.m2()
# print()
# time.sleep(2)
# print("End of an application")

# Duck Typing

# Example 1
# import time
# class IT_SERVIES:
#     def developer(self):
#         print("Develop the application bussiness logic")
#     def UI_developers(self):
#         print("UI Developers develop the frontend of web applications")
#     def Angular_developer(self):
#         print("Angular develoepr develops ERP Web Applications")
#     def tester(self):
#         print("Tester are test the code or debug the code")
# i1=IT_SERVIES()
# i1.developer()
# i1.UI_developers()
# i1.Angular_developer()
# i1.tester()
# print()
# time.sleep(2)
# print("End of An application")

# Example 2
# import time
# class calculator_class:
#     def Add(self,x1,x2):
#         self.x1=x1
#         self.x2=x2
#         return self.x1+self.x2
#     def Division(self,y1,y2):
#         self.y1=y1
#         self.y2=y2
#         return self.y1/self.y2
#     def Mul(self,M1,M2):
#         self.M1=M1
#         self.M2=M2
#         return self.M1*self.M2
# c1=calculator_class()
# print("Sum is:",c1.Add(121,179))
# print()
# print("Division is",c1.Division(100,2))
# print()
# print("Mul is:",c1.Mul(12,18))
# print()
# time.sleep(2)
# print("End of an Application")

# Encupsulation in Python
# import time
# class product_class:
#     def setpid(self,pid):
#         self.pid=pid
#     def getpid(self):
#         return self.pid
#     def setpname(self,pname):
#         self.pname=pname
#     def getpname(self):
#         return self.pname
#     def setprice(self,price):
#         self.price=price
#     def getprice(self):
#         return self.price
#     def setcompany(self,company):
#         self.company=company
#     def getcompany(self):
#         return self.company
# p1=product_class()
# p1.setpid(1001)
# p1.setpname("Mobile 1 ")
# p1.setprice(23000.0)
# p1.setcompany("Samsung")
# print("===Product Information===")
# print("Pid is:",p1.getpid())
# print("Pname is:",p1.getpname())
# print("Price is:",p1.getprice())
# print("Comapny is:",p1.getcompany())
# print()
# time.sleep(2)
# print("End of an application")

#  Abstrat Methods
# import time
# from abc import *
# class A_class:
#     @abstractmethod
#     def m1(self):
#         pass
# a1=A_class()
# a1.m1()
# print()
# time.sleep(2)
# print("End of An Application")

# Abstract class
# # basic syntax
# import time
# from abc import * 
# class A_class(ABC):
#     pass
# a1=A_class()
# print()
# time.sleep(2)
# print("End of an Application")

# Example 1 it will give error because we declare abstract method in abstract class,child class is responsible
# import time
# from abc import *
# class B_class(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
# b1=B_class()
# b1.m1()
# print()
# time.sleep(2)
# print("End of an application")

# Example 2
# import time
# from abc import *
# class B_class:
#     @abstractmethod
#     def m1(self):
#         pass
# class c_class(B_class):
#     def m1(self):
#         print("Parent class abstract method")
# c1=c_class()
# c1.m1()
# print()
# time.sleep(2)
# print("End of an application")

# Interface
# import time
# from abc import *
# class IHUB_APP_STORE(ABC):
#     def m1(self):
#         pass
#     def m2(self):
#         pass
# class mysql_db(IHUB_APP_STORE):
#     def m1(self):
#         print("Connceting mysql_db for indian users")
#     def m2(self):
#         print("disconnceting mysql_db for indian users")
# class mongo_db(IHUB_APP_STORE):
#     def m1(self):
#         print("connecting to mongo_db for US users")
#     def m2(self):
#         print("disconnecting to mongo_db for US users")
# class postGRESQL(IHUB_APP_STORE):
#     def m1(self):
#         print("connecting to the postGRESQL for china users")
#     def m2(self):
#         print("Disconnecting to postGRESQL for china users")
# DB_name=input("Enter the data base name:")
# x1=globals()[DB_name]
# obj1=x1()
# time.sleep(3)
# obj1.m1()
# print()
# time.sleep(3)
# obj1.m2()
# print()
# time.sleep(5)
# print("End of an application")

#concrete classes
# Example 1 it will give error because we declaring 4 methods but implementing 3 
# import time
# from abc import *
# class A_class(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     @abstractmethod
#     def m3(self):
#         pass
#     @abstractmethod
#     def m4(self):
#         pass
# class B_class(A_class):
#     def m1(self):
#         print("ABC_Method_one__")
#     def m2(self):
#         print("ABC_Method_two__")
#     def m3(self):
#         print("ABC_Method_Three___")
# b1=B_class()
# b1.m1()
# b1.m2()
# b1.m3()
# print()
# time.sleep(2)
# print("End of an application")

# Example 2
# import time
# from abc import *
# class A_class(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
#     @abstractmethod
#     def m3(self):
#         pass
#     @abstractmethod
#     def m4(self):
#         pass
# class B_class(A_class):
#     def m1(self):
#         print("ABC_Method_one___")
#     def m2(self):
#         print("ABC_Method_two__")
#     def m3(self):
#         print("ABC_Method_three___")
# class C_class(B_class):
#     def m4(self):
#         print("ABC_Method_Four___")
# c1=C_class()
# c1.m1()
# c1.m2()
# c1.m3()
# c1.m4()
# print()
# time.sleep(2)
# print("End of an application")