d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50, 6:60}
d_union=d1|d2|d3
print(d_union)

d4={'emp1': {'name':'Jhon', 'Salary':7500},
    'emp2': {'name':'Emma', 'Salary':8000},
    'emp3': {'name':'Brad', 'Salary':6500},}

c=d4['emp1']['Salary']=6500
print(d4)

num=int(input("Количество студентов:"))
d5={}
summa=0
for key in range(num):
    d5[key]=[input("Введите имя студента:"), int(input("Введите балл студента:"))]
    print(key+1, "-й"," студент:", d5[key][0])
    print("Балл:", d5[key][1])
    summa=summa+d5[key][1]
a=round(summa/num)
print("Средний балл:", a)
b=[]
for i in d5:
    if d5[i][1]>a:
       b.append(d5[i][0])
print("Студенты с баллом выше среднего:")
if len(b)>0:
    for student in b:
        print(student)
else:
    print("Нет студентов с баллов выше среднего")

