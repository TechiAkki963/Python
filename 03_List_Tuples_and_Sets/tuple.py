# TUple - immutable

tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)
# TypeError: 'tuple' object does not support item assignment