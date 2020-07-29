import re

list = [3180676 , 20211]
print(list[1])
str ="Number of students: 31,80,676"
list = [3180676 , 20211 ,3184754 , 20194 ,3147431 , 20106]
res1 =re.sub("\D","", str)
if int(res1) in list:
    print("No of schools value is correct ")
else:
    print("Not matching in no of school ")


