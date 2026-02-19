import time
import re
f1=open("regular_expression/input.txt","r")
f2=open("output.txt","w")
for x1 in f1:
    l1=re.findall(r"[+]{1}[9]{1}[1]{1}-[6-9]\d{9}",x1)
    for l2 in l1:
        f2.write(l2+"\n")
print()
f1.close()
f2.close()
print()
time.sleep(2)
print("End of An Application")