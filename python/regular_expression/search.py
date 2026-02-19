import time
import re
str1=input("Enter the string object:")
res1=re.search(str1,"Django",re.I)
if(res1!=None):
    print(str1,":Pattern is There.")
else:
    print(str1,":pattern is not There.")
print()
time.sleep(2)
print("End of An Application")


# import time
# import re
# str1=input("Enter the string object:")
# res1=re.search("^A",str1,re.I)
# if(res1!=None):
#     print(str1,":Pattern starts with A|a.")
# else:
#     print(str1,":pattern is not starts with A|a.")
# print()
# time.sleep(2)
# print("End of An Application")

# import time
# import re
# str1=input("Enter the string object:")
# res1=re.search("A$",str1,re.I)
# if(res1!=None):
#     print(str1,":Pattern ends with A|a.")
# else:
#     print(str1,":pattern is not ends with A|a.")
# print()
# time.sleep(2)
# print("End of An Application")