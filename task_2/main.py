#Kirill
# #вариант 1 
import random

summ = 0
height = random.randint(4,8)
length = random.randint(4,8)
a = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

b =  [[random.choice(a) for j in range(height)] for i in range(length)]


for char in b:
    print(char)
    for i in char:
        if i % 2== 0:
           summ+=i

print(summ)


