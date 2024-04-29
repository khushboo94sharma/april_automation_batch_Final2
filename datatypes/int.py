""" This module file is created to practice python integer datatype
created by khushboo on 04/27/2024

Added new line of code to handle int type
"""

count = 10

print("the value of count is", count)
print("type of count is", type(count))
print("memory address of count is", id(count))

count2 = 10

print("the value of count2 is", count2)
print("type of count2 is", type(count2))
print("memory address of count2 is", id(count2))

count3 = 15

print("the value of count3 is", count3)
print("type of count3 is", type(count3))
print("memory address of count3 is", id(count3))

count = 3

print("the value of count is", count)
print("type of count is", type(count))
print("memory address of count is", id(count))

count4 = 10

print("the value of count4 is", count4)
print("type of count4 is", type(count4))
print("memory address of count4 is", id(count4))

count5 = 15

print("the value of count5 is", count5)
print("type of count5 is", type(count5))
print("memory address of count5 is", id(count5))

count6 = -15

print("the value of count6 is", count6)
print("type of count6 is", type(count6))
print("memory address of count6 is", id(count6))


print("absolute number -15 is", count6.__abs__())
print("add two number {count5} and {count6} number is", count6.__add__(count5)) #magic_methods
print("add two number {count5} and {count} number is", count6.__add__(count))   #Magic_Methods

a=16000
print("bit_cunt is", a.bit_count())  #normal methods


print("methods available in python int", dir(count))
