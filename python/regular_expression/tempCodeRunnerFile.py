import time
import re
str1=input("Enter the string object:")
res1=re.fullmatch(str1,"Django",re.I)
if(res1!=None):
    print(str1,":Pattern is matched successfully.")
else:
    print(str1,":pattern is not matched succesfully.")
print()
time.sleep(2)
print("End of An Application")