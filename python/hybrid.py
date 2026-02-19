import time
class A_class:
    def m1():
        print("A_class is to exceuted")
class B_class(A_class):
    def m2():
        print("B_class is to exceuted")
b1=B_class
b1.m1()
b1.m2()
print()
time.sleep(2)
print("End of An Application")
