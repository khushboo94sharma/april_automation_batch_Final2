""" This module file is created to practice python boolean datatype
created by khushboo on 04/28/2024
"""

c = True
print("The  value of c is", c)
print("Type of c is", type(c))
print("Memory address of c is", id(c))
b = False
print("The value of b is", b)
print("Type of b is", type(b))
print("Memory address of b is", id(b))

d = True
print("The value of d is", d)
print("Type of d is", type(d))
print("Memory address of d is", id(d))
print("methods available", dir(d))

print(f"__add__ of {c} and {d}", c.__add__(d))