import time
import re
str1=input("Enter the string object:")
res1=re.match(str1,"Django",re.I)
if(res1!=None):
    print(str1,":Pattern starts from indexing position.")
else:
    print(str1,":pattern is not starts from indexing position.")
print()
time.sleep(2)
print("End of An Application")