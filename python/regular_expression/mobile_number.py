import time
import re
Mobile_number=input("Enter your Mobile NUmber:")
res1=re.fullmatch(r"[6-9]\d{9}",Mobile_number)
if(res1!=None):
    print(Mobile_number,"Valid Mobile Number")
else:
    print(Mobile_number,":Not Valid Mobile Number")
print()
time.sleep(2)
print("End of An Application")