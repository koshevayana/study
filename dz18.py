str1= 'I am learning python. hello, WORLD'
h='h'
first=str1.find(h)
last=str1.rfind(h)
result=str1[:first]+str1[last+1:]
print(result)
result2 = str1[:first+1] + str1[first:last][::-1] + str1[last+1:]
print(result2)
import re
str3= '11, 23, 44, 55, 23, 22'
podstr='23'
new_str='!!!'
print(re.sub(podstr,new_str,str3))
str4='''Ежевику для ежат
Принесли два ежжа
Ежевику еле-еле
Ежата возли ели съели'''

reg=r'\b[еЕ][а-яА-ЯёЁ-]*\b'
print(len(re.findall(reg,str4)))