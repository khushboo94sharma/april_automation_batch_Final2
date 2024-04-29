""" This module file is created to practice python string datatype
created by khushboo on 04/28/2024
"""

string = 'ETL'

print("The value of string is ", string)
print("type of string is ", type(string))
print("Memory of string", id(string))

string2 = "ETL"

print("The value of string2 is ", string2)
print("type of string2 is ", type(string2))
print("Memory of string2", id(string2))

string3 = """ETL"""

print("The value of string3 is ", string3)
print("type of string3 is ", type(string3))
print("Memory of string3", id(string3))

string4 = '''ETL'''

print("The value of string4 is ", string4)
print("type of string4 is ", type(string4))
print("Memory of string4", id(string4))

string = " I don't care "

print("The value of string is ", string)
print("type of string is ", type(string))

string = ' I don"t care '

print("The value of string is ", string)
print("type of string is ", type(string))
print("Memory of string", id(string))

string = """i don't care """
string = '''i don"t care '''

etl_string= '''ETL in testing means an extract, transform and load process that reads data from multiple source systems,
 transports it to a data transformation layer for further processing which includes cleaning,
consolidating, integrating, and then loading into a target database or file'''

print("The value of etl_string is ", etl_string)
print("type of etl_string is ", type(etl_string))

print("methods available in string datatype",dir(etl_string))

str7 = 'ETL Automation testing'
print("Before capitalize str7 is ", str7)
print("After capitalize str7 is", str7.capitalize())
print("After title str7 is", str7.title())

print("Before casefold str7 is ", str7)
print("After casefold str7 is", str7.casefold())
print("After lower str7 is", str7.lower())

print("After swapcase str7 is", str7.swapcase())
print("After upper str7 is", str7.upper())

txt = "ETL Testing"
x = txt.center(100)
print(x)

str8 = 'BIG DATA TESTING 1| 4342 [472534623542 '
print(f"count of a in {str8}", str8.count('a '))
print(f"count of A in {str8}", str8.count('A'))
print(f"count of | in {str8}", str8.count('|',20,30))

name = 'Sreeni'
print(f"count of en in {name} and n ", name.count('en'),name.count('n'))

print("*"*50)
#
str="Automation Testing"
#
str = input("enter str value:") # input, raw_input

print(f"str.startswith('Auto') in {str} : ",str.startswith('Auto'))
print(f"str.startswith('Auto') in {str} : ",str.startswith('auto'))
print("Ends with Testing ",str.endswith('Testing'))
print(help(str.startswith))
print(help(str.endswith))

#str ='TESTING'
print("str.find('Test')",str.find(' Test'))
print("str.find('i')",str.find('i'))
#
print("str.find('i',8)",str.find('i',8))

print("str.find('i',8,12)",str.find('i',8,12))
