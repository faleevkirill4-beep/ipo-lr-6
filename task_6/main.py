#Kirill
import random

list_1 = [[random.randint(-10,10) for i in range(4)] for i in range(20)]

for i,sublist in enumerate(list_1) :
    print(f"{i+1:2d}: {sublist}")



unique_combinations = list({tuple(sorted(sublist)) for sublist in list_1})

print(f"\nВсего уникальных комбинаций: {len(unique_combinations)}")
print("уникальные комбинации: ")
for i,a in enumerate(unique_combinations):
    print(f"{i+1:2d}: {a}")


s = input("введите число: ")

sum_1 = 0
count_i = 0

for i in unique_combinations :
    if(i < s):
        count_i+=1

print(coount_i)


 



