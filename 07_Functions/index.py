# Empty Function
def hello_funct():
  pass

print(hello_funct())

# Function
def hello():
  message = 'Hello Function!'
  return message

print(hello())
print(hello().upper())

def greet(greeting, name='User'):
  return '{}, {}'.format(greeting,name)
print(greet('Hi'))
# Hi, User
print(greet('HI',name='Akshay'))
# HI, Akshay


def student_info(*args,**kwargs):
  print(args)
  print(kwargs)

print(student_info('Math','Arts',name='User',age='25'))
# ('Math', 'Arts')                       args
# {'name': 'User', 'age': '25'}          kwargs

def stud_info(*args,**kwargs):
  print(args)
  print(kwargs)

courses = ['Math','Art']
info = {'name': 'User', 'age': '25'} 

stud_info(*courses,**info)
# ('Math', 'Art')
# {'name': 'User', 'age': '25'}

  