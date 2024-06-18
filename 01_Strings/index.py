
# Print Welcome Message
print("Hello World")


message = "Welcome to Akki's App"
print(message)


# to write a multi-line message we use ''' Abc '''

chatbot = """ ChatGPT is a chatbot and virtual assistant developed by OpenAI and launched on November 30, 2022. Based on large language models, it enables users to refine and steer a conversation towards a desired length, format, style, level """

print(chatbot)

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
#The quick brown fox jumps over the lazy dog

print(len(sentence)) 
# 43

print(sentence[7])
#c

# print(sentence[44])
#IndexError: string index out of range

print(sentence[0:3])
#The

print(sentence[:3])
#The

print(sentence[3:])
#quick brown fox jumps over the lazy dog


# Lowercase UpperCase
greet = "Namaste Akshay"
print(greet.lower())
# namaste akshay

print(greet.upper())
# NAMASTE AKSHAY



name = "Tony stark"
print(name.count("Tony")) 
#1

print(name.find("stark"))
#5


new_name = name.replace("Tony","Howard")
print(new_name)
# Howard stark     - replace tony to haward

greeting = "Hello"
user = "Rogers"
display_message = '{}, {} Welcome!'.format(greeting,user)
print(display_message)
#Hello, Rogers Welcome!


# f strings

greeting = "Hello"
user = "Rogers"
display_message = f'{greeting}, {user} Welcome!'
print(display_message)
# Hello, Rogers Welcome!

print(dir(user))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# Provides with number of operations we can do on string

# print(help(str))
print(help(str.lower))
