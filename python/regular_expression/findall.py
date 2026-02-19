import time
import re
obj1=re.findall(r"\d","ABcd_ 1234567@gmail.com")
print(obj1)
print()
print(type(obj1))
print()
for x1 in obj1:
    print(x1)
print()
time.sleep(2)
print("End of An Application")