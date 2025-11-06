#Kirill
import random

list_1 = [[random.randint(-10,10) for i in range(4)] for i in range(20)]
print(list_1)
scor = 0
new_0 = list()
for i in list_1 :
    scor += 1
    if list_1[scor] != list_1[scor + 1] : 
     new_0+=list_1[scor] 

print(new_0)     



