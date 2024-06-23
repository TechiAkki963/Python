# Comparison
# Equal: ==
# Not Equal : !=
# Greater than: >
# Lesser than: <
# Greater than equalto : >=
# Lesser than equal to : <=
# object identity : is

# and 
# or 
# not


# False Value
# False
# None
# Zero of numeric type
# Any empty sequence : ' ' , () , []
# Any empty mapping , { }

language = 'Python'

if language == 'Python':
  print('condition was TRUE for Python')
elif language == 'Java':
  print('condition was TRUE for JAVA')
elif language == 'C++':
  print('condition was TRUE for C++')
else:
  print('no match')


# and 
# or
# not

user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in :
  print('Admin Page')
else :
  print('Wrong Credentials')

if not logged_in:
  print('Please log in')  
else:
  print('Welcome')


