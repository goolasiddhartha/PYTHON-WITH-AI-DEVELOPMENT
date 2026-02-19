# Example 1
# import time
# import logging
# logging.basicConfig(filename="obj1.txt",level=logging.DEBUG)
# print("=== welcome to logging module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of an Application")

# Example 2
# import time
# import logging
# logging.basicConfig(filename="obj1.txt",level=logging.DEBUG,filemode="w")
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# # Example 3 on give number for leveling
# import time
# import logging
# logging.basicConfig(filename="obj1.txt",level=10,filemode="w")
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# Example 4 print from warning message
# import time
# import logging
# logging.basicConfig(filename="obj1.txt",filemode="w")
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# Example 5 will print critical information only
# import time
# import logging
# logging.basicConfig(filename="obj1.txt",level=logging.CRITICAL,filemode="w")
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# # Example 6 will information in console
# import time
# import logging
# logging.basicConfig(format=("%(levelname)s"),level=logging.DEBUG)
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# # Example 7 will message in console
# import time
# import logging
# logging.basicConfig(format=("%(message)s"),level=logging.DEBUG)
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")

# Example 8 will print time and date in console
# import time
# import logging
# logging.basicConfig(format=("%(asctime)s"),level=logging.DEBUG)
# print("=== Welcome to logging Module ===")
# logging.debug("Debug_Information")
# logging.info("Info_Information")
# logging.warning("Warning_Information")
# logging.error("Error_Information")
# logging.critical("Critical_Information")
# print()
# time.sleep(2)
# print("End of An Application")


# Example 9 use all three at a time
# import time
# import logging
# logging.basicConfig(format="%(asctime)s:%(levelname)s):%(message)s",level=logging.DEBUG)
# print("=== Welcome to logging Module ===")
# logging.debug("Debug Information")
# logging.info("Info Information")
# logging.warning("Warning Information")
# logging.error("Error Information")
# logging.critical("Critical Information")
# print()
# time.sleep(2)
# print("End of an Application")

# Example 10 display date and time in indian format
# import time
# import logging
# logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG,datefmt="%d/%m/%y %I:%M:%S %p")
# print("=== Welcome to logging Module ===")
# logging.debug("Debug Information")
# logging.info("Info Information")
# logging.warning("Warning Information")
# logging.error("Error Information")
# logging.critical("Critical Information")
# print()
# time.sleep(2)
# print("End of an Application")

# Full Application
# import time
# import logging
# logging.basicConfig(filename="obj2.txt",format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG,datefmt="%d/%m/%y %I:%M:%y %p",filemode="w")
# try:
#     x1=int(input("Enter the x1_value:"))
#     x2=int(input("Enter the value of x2:"))
#     res1=x1//x2
#     print("The result_set is:",res1)
# except ZeroDivisionError as e:
#     print("Exception Name is:",e)
#     logging.exception(e)
# except ValueError as e:
#     print("Exception Name is:",e)
#     logging.exception(e)
# print()
# print("Request Processed Succesfully")
# print()
# time.sleep(2)
# print("End of An Application")
    