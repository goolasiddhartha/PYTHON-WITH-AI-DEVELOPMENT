import time
import re
obj1=re.subn("[0-9]","X","ABCDabcd_ 1234567@gmail.com")
print(obj1[0])
print()
print(obj1[1])
print()
print(type(obj1))
time.sleep(2)
print("End of An Application")  