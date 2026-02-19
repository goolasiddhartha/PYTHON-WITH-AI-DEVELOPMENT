import time
import re

Gmail = input("Enter The Gmail Account: ")

res1 = re.fullmatch(r"[A-Za-z0-9._]+@gmail\.com", Gmail)

if res1!=None:
    print(Gmail, ": It is Valid Gmail Account")
else:
    print(Gmail, ": It is Invalid Gmail Account")

print()
time.sleep(2)
print("End of An Application")