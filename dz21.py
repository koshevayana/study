lst1=[-2,3,8,-11,-4,6]

def summa(lst):
    if len(lst)==0:
        return 0
    else:
        current = 1 if lst[0] < 0 else 0
        return current + summa(lst[1:])


result = summa( lst1)
print(f"Количество отрицательных чисел: {result}")
