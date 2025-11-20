#Kirill
#ввод строки 
n = input("введите искомую строку: ").strip().lower()
#открытие файла из которого будем брать данные 
with open("text.txt",'r',encoding = 'UTF - 8') as file:
    lines = file.readlines()#реобразования строк в список 

listik = []
number = 0
#нахождение строки в файле 
for i,line in enumerate(lines,1):
    if n in line.lower():
        listik.append(line.strip())
        number+=1

print("список сток: " , listik)
print("колличество строк: " , number)

#исправить сортировку

#сортировка 
listik_sort =sorted(listik, key=lambda x: len(x[1]))

print(listik_sort)

    