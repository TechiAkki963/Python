# List
courses = ["English","Hindi","Sanskrit","German","Physics","Chemistry","Math-1","Math-2","Bio"]
print(courses)

print(courses[0])

print(courses[-1])
# Bio   -1 gives the last item from the list

print(courses[1:3])
# ['Hindi', 'Sanskrit']

print(courses[:3])
# ['English', 'Hindi', 'Sanskrit']

print(courses[2:5])
# ['Sanskrit', 'German', 'CS']

# to add an item to the end of the list
courses.append("geo")
print(courses)
# ['English', 'Hindi', 'Sanskrit', 'German', 'Physics', 'Chemistry', 'Math-1', 'Math-2', 'Bio', 'geo']

# to add an item to a specific location
courses.insert(0,"french")
print(courses)
# ['french', 'English', 'Hindi', 'Sanskrit', 'German', 'Physics', 'Chemistry', 'Math-1', 'Math-2', 'Bio', 'geo']


# to combine two lists
courses_2=['Marathi','CS','Electronics']
courses.extend(courses_2)
print(courses)
# ['french', 'English', 'Hindi', 'Sanskrit', 'German', 'Physics', 'Chemistry', 'Math-1', 'Math-2', 'Bio', 'geo', 'Marathi', 'CS', 'Electronics']

# to remove the last item from the list
popped = courses.pop()

print(popped)
# Electronics
print(courses)
# ['french', 'English', 'Hindi', 'Sanskrit', 'German', 'Physics', 'Chemistry', 'Math-1', 'Math-2', 'Bio', 'geo', 'Marathi', 'CS']

#  to reverse a list
courses.reverse()
print(courses)
# ['CS', 'Marathi', 'geo', 'Bio', 'Math-2', 'Math-1', 'Chemistry', 'Physics', 'German', 'Sanskrit', 'Hindi', 'English', 'french']


# Sorting in List
letters = ["b","c","d","a","e","i","o","u"]
nums = [1,2,3,4,5,6]

letters.sort()
nums.sort()

print(letters) 
# ['a', 'b', 'c', 'd', 'e', 'i', 'o', 'u']

print(nums)
# [1, 2, 3, 4, 5, 6]

# to reverse sort
letters.sort(reverse=True)
nums.sort(reverse=True)

print(letters) 
# ['u', 'o', 'i', 'e', 'd', 'c', 'b', 'a']
print(nums)
# [6, 5, 4, 3, 2, 1]
 

#  To sort list without affecting ORIGINAL LIST
sorted_letters = sorted(letters)
print(letters)
# ['u', 'o', 'i', 'e', 'd', 'c', 'b', 'a']
print(sorted_letters)
# ['a', 'b', 'c', 'd', 'e', 'i', 'o', 'u']

# to find the MIN VALUE in List
print(min(nums))
#1

# to find the MAX VALUE in List 
print(max(nums))
#6

# to print the SUM of List
print(sum(nums))
# 21

# To get the Index of item in the List
print(courses.index("Bio"))
# 3

# print(courses.index("Art"))
# ValueError: 'Art' is not in list

print("German" in courses)
# True

print("Art" in courses)
# False

for i in courses:
  print(i)

# CS
# Marathi
# geo
# Bio
# Math-2
# Math-1
# Chemistry
# Physics
# German
# Sanskrit
# Hindi
# English
# french

for index, course in enumerate(courses, start=1):
  print(index,course)
# 0 CS
# 1 Marathi
# 2 geo
# 3 Bio
# 4 Math-2
# 5 Math-1
# 6 Chemistry
# 7 Physics
# 8 German
# 9 Sanskrit
# 10 Hindi
# 11 English
# 12 french

fruits = ["apple","mango","banana","oranges"]

fruits_str=','.join(fruits)

print(fruits_str)
# apple,mango,banana,oranges

fruits_str=' - '.join(fruits)
print(fruits_str)
# apple-mango-banana-oranges  

new_list = fruits_str.split(' - ')
print(new_list)
# ['apple', 'mango', 'banana', 'oranges']