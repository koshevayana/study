import re


def password (passw):
    pattern = r'^[a-zA-Z0-9\-@_]{6,18}$'
    if re.match(pattern, passw):
        print(True)
    else:
        print(False)

password('my-p@ssw0rd')

def find_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)

text1='В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков.'
print(find_dates(text1))