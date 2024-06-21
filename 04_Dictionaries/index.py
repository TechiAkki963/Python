student = {'name':'Akshay','age':25,'course':['Math','Sci']}

print(student)
# {'name': 'Akshay', 'age': 25, 'course': ['Math', 'Sci']}

print(student['name'])
# Akshay

print(student['course'])
# ['Math', 'Sci']

student['phone']='555-5555-55555'
print(student)
# {'name': 'Akshay', 'age': 25, 'course': ['Math', 'Sci'], 'phone': '555-5555-55555'}

print(student.get('email', 'Error'))
# Error

student.update({'name':'Jane','age':26,'course':['History','Geo']})
print(student)
# {'name': 'Jane', 'age': 26, 'course': ['History', 'Geo'], 'phone': '555-5555-55555'}

del student['age']
print(student)
# {'name': 'Jane', 'course': ['History', 'Geo'], 'phone': '555-5555-55555'}

name = student.pop('name')
print(student)
# {'course': ['History', 'Geo'], 'phone': '555-5555-55555'}
print(name)
# Jane


product ={'product_name':'apple','model':15,'type':['ipad','mobile']}
print(product)
# {'product_name': 'apple', 'model': 15, 'type': ['ipad', 'mobile']}

print(len(product))
# 3

print(product.keys())
# dict_keys(['product_name', 'model', 'type'])

print(product.values())
# dict_values(['apple', 15, ['ipad', 'mobile']])

print(product.items())
# dict_items([('product_name', 'apple'), ('model', 15), ('type', ['ipad', 'mobile'])])

for key in product:
  print(key)
# product_name
# model
# type

for key, value in product.items():
  print(key, value) 
# product_name apple
# model 15
# type ['ipad', 'mobile']