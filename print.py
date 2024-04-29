import sys
import datetime

name = 'Khush '
age = 20
print(f"name is {name} and age is {age} ")
print("name is", name ,"and age is", age, sep='')
print(f"name:{name},age:{age}")

source_cnt = 10
target_cnt = 20
print("source count is", source_cnt, "target count is", target_cnt, "and difference is " ,source_cnt-target_cnt)
print(f"source count is {source_cnt} and target count is {target_cnt} and difference is {source_cnt-target_cnt}")

batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

file = open(r"C:\Users\HP\PycharmProjects\april_automation_batch\text"+batch_id+".txt", 'a')
original = sys .stdout
sys.stdout = file

print(source_cnt, target_cnt, sep='-', end='\t', file=file )
print("Execution is completed!!!")
print("hello world")

for i in range(1,10):
    print(i)