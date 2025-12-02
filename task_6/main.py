#Kirill
import random

list_1 = [[random.randint(-10,10) for i in range(4)] for i in range(20)]

for i,sublist in enumerate(list_1) :
    print(f"{i+1:2d}: {sublist}")



unique_combinations = list({tuple(sorted(sublist)) for sublist in list_1})

print(f"\nВсего уникальных комбинаций: {len(unique_combinations)}")
print("уникальные комбинации: ")
for i,a in enumerate(unique_combinations,1):
    print(f"{i:2d}: {a}")


s = int(input("введите число: "))

count = 0
total_sum = 0
groups = []

for i in range(len(unique_combinations)):
    for j in range(i+1,len(unique_combinations)):
        total_sum = int(sum(unique_combinations[i]) + int(sum(unique_combinations[j])))

    if total_sum < s:
        count += 1
    groups.append((unique_combinations[i],unique_combinations[j],total_sum))

print(f"\Колличество пар, чья сумма меньше {s}:{count}")

if count > 0:
    print("Пары и их суммы:")
    for i, (group_1,group_2,sum_1) in enumerate(groups,1):
        if sum_1 < s:
            print(f"{i:2}: {group_1} + {group_2} = {sum_1}")
else:
    print("не найдено")



 



