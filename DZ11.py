from itertools import count

t=('ab', 'abcd', 'cde', 'abc', 'def')

def search(s):
    if s in t:
        print("Yes")
search("ab")

el=input("Введите элементы кортежа без пробелов и символов:")
t2=tuple(el)
print(t2)
b=[]
for i in t2:
    if i not in b:
        print("Количество", i, "=", t2.count(i))
        b.append(i)

import random as r
winning_numbers={r.randint(1, 100) for i in range(6)}
print(winning_numbers)
print("Для выхода введите 0.")
num=int(input("Введите целое число (от 1 до 100):"))
while True:
    if num!=0:
        if num in winning_numbers:
            print("Поздравляем, вы угадали!")
            print("Попробуйте еще раз!")
            num = int(input("Введите целое число:"))
        else:
            print("Попробуйте еще раз!")
            num = int(input("Введите целое число:"))
    else:
        print("До свидания!")
        break
