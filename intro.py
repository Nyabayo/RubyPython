print("Welcome to python programming")
print("lorem ipsum")
#Python syntax and comments
#Indentation
if 7>4:
    print("7 Is greater than 4")

# Python will give you an error if you skip the indentation.
# # if 7>4:
# # print("7 Is greater than 4")

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
# if 5 > 2:
#  print("Five is greater than two!")
#   print("Five is greater than two!")

# Python Variables
#In python variabs ar created when you asign values to it.
#age is of type int
age=23
#name of type  str
name="Favour"
print(age)
print(name)

#Casting: specifying te ata type of variable
age=int(19)
name=str("Favour")
print(age)
print(name)


#Get the Type : You can get the data type of a variable with the type() function.
age=34
name="joy"
print (type(age))
print(type(name))

#Single or Double Quotes?
# String variables can be declared either by using single or double quotes:
x='sit'
# is the same as
y="sit"

# Case-Sensitive
# Variable names are case-sensitive.
a=3
A='cate'
#A will not overwrite a

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# Assign Multiple Values
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)





