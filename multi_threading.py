# Example 1 
# import time 
# from threading import *
# print("Current Thread Name is:",current_thread().getName())
# print()
# time.sleep(2)
# print("End of An Application")

# Example 2
# import time
# from threading import *
# print("Current thread Name is:",current_thread().getName())
# print()
# current_thread().setName("Siddhartha")
# print("Current Thread Name is:",current_thread().getName())
# print()
# time.sleep(2)
# print("End of An Application")


# Thread can be created using functionl Approach
# import time
# from threading import *
# def test_case1():
#     for x1 in range(5):
#         time.sleep(1)
#         print("Generative AI Application Development")
# if(__name__=="__main__"):
#     t1=Thread(target=test_case1)
#     t1.start()
#     for y1 in range(5):
#         time.sleep(1)
#         print("1.Python|Flask|Open AI Tools|JS|API")
# print()
# time.sleep(2)
# print("End of An Application")

# Creating a Threading using Inheritence Approach 
# import time
# from threading import *
# class my_Thread_1(Thread):
#     def m1(self):
#         for x1 in range (5):
#             time.sleep(1)
#             print("Generative AI")
# t1=my_Thread_1()
# t1.start()
# for y1 in range(5):
#     time.sleep(2)
#     print("Python|Flask|Open AI Tools")
# print()
# time.sleep(2)
# print("End of An Application")

# Thread Can be Created using Class Approach
# import time
# from threading import * 
# class Test_case1:
#     def m1(self):
#         time.sleep(1)
#         print("Generative AI")
# t1=Test_case1()
# t2=Thread(target=t1.m1)
# t2.start()
# for y1 in range(10):
#     time.sleep(1)
#     print("Python|Flask")
# print()
# time.sleep(2)
# print("End of An Application")

# Example 1
# import time 
# def Test_Case1(obj1):
#     for x1 in obj1:
#         time.sleep(1)
#         print("Square of a number is:",x1*x1)
# def Test_Case2(obj1):
#     for y1 in obj1:
#         time.sleep(1)
#         print("Adding_Operations are:",y1+1000)
# def Test_Case3(obj1):
#     for z1 in obj1:
#         time.sleep(1)
#         print("Multipy_Operations:",z1*15)
# def Test_Case4(obj1):
#     for a1 in obj1:
#         time.sleep(1)
#         print("Expo_value is:",a1**a1)
# if(__name__=="__main__"):
#     obj1=[1,2,3,4,5,6,7,8,9,10,12,12]
#     begin_time=time.time()
#     Test_Case1(obj1)
#     Test_Case2(obj1)
#     Test_Case3(obj1)
#     Test_Case4(obj1)
#     end_time=time.time()
#     print("Time with_out multithreading is:",end_time-begin_time)
# print()
# time.sleep(2)
# print("End of an application")


# Example 2
# import time 
# from threading import *
# def Test_Case1(obj1):
#     for x1 in obj1:
#         time.sleep(1)
#         print("Square of a number is:",x1*x1)
# def Test_Case2(obj1):
#     for y1 in obj1:
#         time.sleep(1)
#         print("Adding_Operations are:",y1+1000)
# def Test_Case3(obj1):
#     for z1 in obj1:
#         time.sleep(1)
#         print("Multipy_Operations:",z1*15)
# def Test_Case4(obj1):
#     for a1 in obj1:
#         time.sleep(1)
#         print("Expo_value is:",a1**a1)
# if(__name__=="__main__"):
#     obj1=[2,4,6]
#     begin_time=time.time()
#     t1=Thread(target=Test_Case1,args=(obj1,))
#     t2=Thread(target=Test_Case2,args=(obj1,))
#     t3=Thread(target=Test_Case3,args=(obj1,))
#     t4=Thread(target=Test_Case4,args=(obj1,))
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     end_time=time.time()
#     print("Time with multithreading is:",end_time-begin_time)
# print()
# time.sleep(2)
# print("End of an application")


