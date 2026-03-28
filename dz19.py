import re

str1='123456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'

reg=r'[\w.-]+@[\w.-]+\.\w+'

print(re.findall(reg,str1))