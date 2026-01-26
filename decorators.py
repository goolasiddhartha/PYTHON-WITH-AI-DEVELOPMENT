# Example 1
# import time 
# def Test_Case1(name):
#     print("Name of the language is:",name)
# if(__name__=="__main__"):
#     Test_Case1("Python")
# print()
# time.sleep(2)
# print("End of an application")

# Example 2
# import time
# def test_case2(func):
#     def inner(name):
#         if(name=="Python"):
#             print(name,":Meant for General Purpose application development")
#         else:
#             func(name)
#     return inner
# @test_case2
# def test_case1(name):
#     print("Name of the language is:",name)
# if(__name__=="__main__"):
#     test_case1("Python")
# print()
# time.sleep(2)
# print("End of an application")

# Example 3
# import time
# def test_case2(func):
#     def inner(name):
#         if(name=="python"):
#             print(name,"Meant for general purpose application")
#         else:
#             func(name)
#     return inner
# @test_case2
# def test_case1(name):
#     print("Name of the language is:",name)
# if(__name__=="__main__"):
#     test_case1("Python")
# print()
# time.sleep(2)
# print("End of an Application")

# Example 4
# import time
# def test_case2(test_case1):
#     def inner(name):
#         if(name=="Python"):
#             print(name,":Meant for general purpose application development")
#         else:
#             test_case1(name)
#     return inner
# @test_case2
# def test_case1(name):
#     print(name,":Meant for general purpose application development")
# if(__name__=="__main__"):
#     test_case1("Python")
# print()
# time.sleep(2)
# print("End of an Application")

# Example 5
# import time
# def test_case2(test_case1):
#     def inner(name):
#         if(name=="Python"):
#             print(name,":Meant for General Purpose Application Development")
#         elif(name=="Javascript"):
#             print(name,":Meant for client side validation")
#         elif(name=="SQL"):
#             print(name,":meant for database operation")
#         else:
#             test_case1(name)
#     return inner
# @test_case2
# def test_case1(name):
#     print("Name os the language is:",name)
# if(__name__=="__main__"):
#     test_case1("Python")
#     print()
#     test_case1("Javascript")
#     print()
#     test_case1("SQL")
# print()
# time.sleep(2)
# print("End of an Application")

# Problem 1
# import time
# def test_case1(x1,x2):
#     return x1/x2
# if(__name__=="__main__"):
#     print(test_case1(10,2))
#     print()
#     print(test_case1(20,5))
#     print()
#     print(test_case1(100,10))
#     print()
#     print(test_case1(1000,0))
#     print()
#     print(test_case1(1200,200))
#     print()
#     print(test_case1(2000,200))
#     print()
#     time.sleep(2)
#     print("End of an applications")

# SOLUTION FOR PROBLEM 1
# import time
# def test_case2(test_case1):
#     def inner(x1,x2):
#         if x2==0 :
#             print(x2,":How can Divide a number with o sorry........")
#         else:
#             return test_case1(x1,x2)
#     return inner
# @test_case2
# def test_case1(x1,x2):
#     return x1/x2
# if(__name__=="__main__"):
#     print(test_case1(10,2))
#     print()
#     print(test_case1(20,5))
#     print()
#     print(test_case1(100,10))
#     print()
#     print(test_case1(1000,0))
#     print()
#     print(test_case1(1200,200))
#     print()
#     print(test_case1(200,200))
#     print()
# time.sleep(2)
# print("End of An Application")

# Example 6
# import time
# def test_case2(test_case1):
#     def inner(name):
#         if(name=="Python"):
#             print(name,":Meant for general purpose application developmemt")
#         else:
#             test_case1(name)
#     return inner
# def test_case1(name):
#     print("Name of the language is:",name)
# decorfunction=test_case2(test_case1)
# if(__name__=="__main__"):
#     test_case1("Python")
#     print()
#     decorfunction("Python")
# print()
# time.sleep(2)
# print("End of an Application")


# Login System with correct details
# import time
# def test_login_component(test_register_component):
#     def inner(fname,lname,username,p1,p2,email):
#         if(username=="Sidhu_12345" and p1=="S_12345"):
#             print(username," ",p1,":Login Succesfully")
#         else:
#             test_register_component(fname,lname,username,p1,p2,email)
#     return inner
# @test_login_component 
# def test_register_component(fname,lname,username,p1,p2,email):
#     print("== New User Details ==")
#     print("First Name is:",fname)
#     print("Last Name:",lname)
#     print("User Name is:",username)
#     print("Password is:",p1)
#     print("Confirm Password:",p2)
#     print("Email Address:",email)
# if(__name__=="__main__"):
#     test_register_component("Sidhu_12345","G","Sidhu_12345","S_12345","S_12345","Sidhu@gmail.com")
# print()
# time.sleep(2)
# print("End of an Applications")

# Login System with incorrect Details
# import time
# def test_login_component(test_register_component):
#     def inner(fname,lname,username,p1,p2,email):
#         if(username=="Sidhu_12345" and p1=="S_1245"):
#             print(username," ",p1,":Login Succesfully")
#         else:
#             test_register_component(fname,lname,username,p1,p2,email)
#     return inner
# @test_login_component 
# def test_register_component(fname,lname,username,p1,p2,email):
#     print("== New User Details ==")
#     print("First Name is:",fname)
#     print("Last Name:",lname)
#     print("User Name is:",username)
#     print("Password is:",p1)
#     print("Confirm Password:",p2)
#     print("Email Address:",email)
# if(__name__=="__main__"):
#     test_register_component("Sidhu_12345","G","Sidhu_12345","S_12345","S_12345","Sidhu@gmail.com")
# print()
# time.sleep(2)
# print("End of an Applications")