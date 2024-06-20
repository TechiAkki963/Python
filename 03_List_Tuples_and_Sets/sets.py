cs_courses = {'Python','Java','Rust','Javascript'}
dsa_courses = {'Java', 'Python','C++'}

print(cs_courses)

print('Java' in cs_courses)
# True

print(cs_courses.intersection(dsa_courses))
# {'Java', 'Python'}

print(cs_courses.difference(dsa_courses))
# {'Javascript', 'Rust'}

print(cs_courses.union(dsa_courses))
# {'Python', 'Javascript', 'Java', 'Rust', 'C++'}