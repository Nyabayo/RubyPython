#Data types
# There are three numeric types in Python:
# int
# float
# complex
from operator import truediv
from random import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex

my_college="eMobolis"
my_int=6
my_float=3.78
my_complex=2j
my_bool=True
my_bool2=False
my_list=["Erick", "Favour", "Mary"]
my_tuple=("banana", "oranges", "apple")
my_range=range(6)
my_set={"toyota", "nissan", "sbaru"}
my_dictionary={"name":"Erick","age":56}

print(f"{my_int} is an integer is {type(my_int)}")
print(f"{my_float} is an float is {(type(my_float))}")
print(f"{my_complex} is an complex is {(type(my_complex))}")
print(f"{my_bool} is an bool is {(type(my_bool))}")
print(f"{my_list} is a list is {(type(my_list))}")
print(f"{my_tuple} is a tuple is {(type(my_tuple))}")
print(f"{my_range} is a range is {(type(my_range))}")
print(f"{my_set} is a set is {(type(my_set))}")
print(f"{my_dictionary} is a dictionary is {(type(my_dictionary))})")

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float
a = float(x)
#convert from float to int
b = int(y)
#convert from int to complex
c = complex(z)
print(a)
print(b)
print(c)


# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

import random
print(random.randrange(1, 10))

# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
#
# 'hello' is the same as "hello".
#
# You can display a string literal with the print() function:
print("ernest")
print('ernest')

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua. """
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
#
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[7])

# Looping Through a String
# Since strings are arrays,
# we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)

# String Length
# To get the length of a string, use the len() function
# spaces are also counted
d="My name is Ernest"
print(len(d))

# Check String
# To check if a certain phrase or character is present in a string,
# we can use the keyword in.
txt="The most important thing i life are not free"
print("free" in txt)
print("money" not in txt)

