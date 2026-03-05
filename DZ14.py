figure_type=input("figure type=")

if figure_type=="rhombus":
    def romb(*d):
        proizv=1
        for i in d:
            proizv*=i
        s=proizv/2
        return s
    d1=float(input("Введите d1:"))
    d2=float(input("Введите d2:"))
    print(romb(d1,d2))

if figure_type=="square":
    def squares(*c):
        for i in c:
            s=i**2
        return s
    c1=int(input("Введите c:"))
    print(squares(c1))


if figure_type=="trapezoid":
    def trapz(*a):
        b=[]
        for i in a:
            b.append(i)
        s=(b[0]+b[1])/2*b[2]
        return s
    a1=float(input("Введите a:"))
    b1=float(input("Введите b:"))
    h1=float(input("Введите h:"))
    print(trapz(a1,b1,h1))

import math
if figure_type=="cirle":
    def cirle(*r):
        for i in r:
            s=math.pi*i**2
        return s
    r1=float(input("Введите r:"))
    print(cirle(r1))

else:
        print("Invalid data")
