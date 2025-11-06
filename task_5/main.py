#Kirill
import random

a = [random.randint(-50,50) for i in range(25)]
print(a)
count_min = 0
count_plus = 0
count_zero = 0
for i in a :
    if i < 0 :
        count_min+=1
    elif i > 0 :
        count_plus+=1
    elif i == 0 :
        count_zero+=1

if count_zero > 0 :
    procent_zero = (count_zero / 25) * 100
elif count_zero == 0 :
    procent_zero = 0

if count_plus > 0 :
    procent_plus = (count_plus / 25) * 100
elif count_plus == 0 :
    procent_plus = 0

if count_min > 0 :
    procent_min = (count_min / 25) * 100
elif count_min == 0 :
    procent_min = 0


print("\n",count_plus," - ",procent_plus,"%",
      "\n",count_min," - ",procent_min,"%","\n",count_zero," - ",procent_zero,"%")      
 
min_a = min(a)
max_a = max(a)

print("минимальное значение: ",min_a,"\n","максимальное значение: ",max_a)
