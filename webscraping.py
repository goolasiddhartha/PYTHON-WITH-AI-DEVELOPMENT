# Regular Expression

# import time 
# import re
# c1=0
# res1=re.finditer("ABC","ABCRRRRABCDDDABCFFFABC")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("Pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")



# Character Class

# [ABC] Chracter
# import time 
# import re
# c1=0
# res1=re.finditer("[ABC]","ABCD abcd_123456@gmail.com")
# for x1 in res1:
#     c1+=0
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# [A-Z] Character 
# import time 
# import re
# c1=0
# res1=re.finditer("[A-Z]", "ABCRRRRABCDDDABCFFFABC")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# [0-9] character 
# import time 
# import re
# c1=0
# res1=re.finditer("[0-9]", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# [A-Z a-z] character
# import time 
# import re
# c1=0
# res1=re.finditer("[A-Z a-z]", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# [A-Z a-z 0-9] Character
# import time 
# import re
# c1=0
# res1=re.finditer("[A-Z a-z 0-9]", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern Present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# [^A-Z a-z 0-9] character
# import time
# import re
# c1=0
# res1=re.finditer("[^A-Za-z0-9]","ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# Predefine classes

# /S except classes
# import time
# import re
# c1=0
# res1 = re.finditer(r"\S", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# /s Only spaces
# import time
# import re
# c1=0
# res1 = re.finditer(r"\s", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# /d only digits
# import time
# import re
# c1=0
# res1 = re.finditer(r"\d", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# /w alpha numerical values including "_"
# import time
# import re
# c1=0
# res1 = re.finditer(r"\w", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# \W Specail Characters
# import time
# import re
# c1=0
# res1 = re.finditer(r"\W", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# Quantifiers

# A ->  only A's
# import time
# import re
# c1=0
# res1 = re.finditer(r"\A", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# A+ -> one A's and more than one A's
# import time
# import re
# c1=0
# res1 = re.finditer(r"A+", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     c1+=1
#     print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# A*->one A's and more than A's zero number of A's with end+1
# import time
# import re
# c1=0
# res1 = re.finditer(r"A*", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     if x1.group()!="":
#         c1+=1
#         print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# A? -> only A's and zero number of A's with end+1
# import time
# import re
# c1=0
# res1 = re.finditer(r"A?", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#     if x1.group()!="":
#         c1+=1
#         print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# A$ --> whether our pattern end with A or not
# import time
# import re
# c1=0
# res1 = re.finditer(r"A$", "ABCD abcd_1234567@gmail.com")
# for x1 in res1:
#         c1+=1
#         print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# A{2,5} --? AA,AAA,AAAA,AAAAA based on input values
# import time
# import re
# c1=0
# res1 = re.finditer(r"A{2,5}", "AABCD abAAAAcd_1234567@gmail.com")
# for x1 in res1:
#         c1+=1
#         print(x1.start(),"==",x1.end(),"==",x1.group())
# print()
# print("pattern present:",c1)
# print()
# time.sleep(2)
# print("End of An Application")

# . ---> it will display the complete pattern
import time
import re
c1=0
res1 = re.finditer(r".", "ABCD abcd_1234567@gmail.com")
for x1 in res1:
        c1+=1
        print(x1.start(),"==",x1.end(),"==",x1.group())
print()
print("pattern present:",c1)
print()
time.sleep(2)
print("End of An Application")