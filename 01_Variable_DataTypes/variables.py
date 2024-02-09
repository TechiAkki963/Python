# A Variable is a container for a value, which can be of various types

'''
This is a multi line comment
or docstring (used to define a function purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
    - Variable names are case sensitive (name and Name are different variables).
    - Must start with a letter or an underscore.
    - Can have numbers but cannot start with one. 
"""

x=1            # Int
y=2.5          # Float
name ='Akshay' # String
is_cool = True # Boo

# Multiple Assignment
x, y, name , is_cool = (1,2.5,'Akshay', True)

print(x,y,name,is_cool)

# Basic math
a = x + y

# Check type
print(type(y))          #<class 'float'>
print(type(is_cool))    #<class 'bool'>


# Casting
x = str(x)
y = int(y)
print(type(x))          #<class 'str'>
print(type(y))          #<class 'int'>

z= float(y)
print(type(z))          #<class 'float'>
print(z)                #2.0




