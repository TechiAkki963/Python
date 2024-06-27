# import sys
# # to import only function from a module 
# from my_module import find_index as fi,test
# # import my_module as mm
import random
import math
import datetime
import calendar
import os  # acess the Operating system
courses = ['history','Math','Physics','CompSci']

random_course= random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))
# 1

today = datetime.date.today()
print(today)
# 2024-06-27

print(calendar.isleap(2020))
# True

print(os.getcwd())  #get Current Working Directory
# C:\Users\Admin\Desktop\Python\08_Import Modules and Exploring The Standard Library

# to view location of file of library
print(os.__file__)
# C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\os.py

# index = fi(courses,'Physics')
# print(index)
# print(test)

# print(sys.path)
# ['C:\\Users\\Admin\\Desktop\\Python\\08_Import Modules and Exploring The Standard Library', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']
