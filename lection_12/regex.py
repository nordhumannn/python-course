# Task 1
# 1. Напишите регулярное выражение, которое будет находить в тексте
# фрагменты, состоящие из одной буквы R, за которой следует одна или 
# более букв b, за которой одна r. Учитывать верхний и нижний регистр.

import re

text = 'Some text, sgnkrngRbrejknflwlRbr'
pattern = r'(Rb+r)'

def regex_1(text):
    match = re.findall(pattern, text)
    return match if match else 'pattern not found'

#--------------------------------------------------------------
# Task 2
# 2. Напишите функцию, выполняющую валидацию 
# номера банковской карты (9999-9999-9999-9999).

card_number = input('>>> ')
pattern = r'^(\d{4}-\d{4}-\d{4}-\d{4})$'

def regex_2(card_number):
    valid = re.search(pattern, card_number)
    return 'Valid' if valid else 'Not valid'

#--------------------------------------------------------------
# Task 3
# 3. Напишите функцию, принимающую строковые данные и выполняющую 
# проверку на их соответствие мейлу.
# Требования:
# -цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы “_” и “-”. Но они не могут 
#  быть первым символом мейла.
# -символ “-” не может повторяться.

mail = input('>>> ')
pattern = r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'

def regex_3(mail):
    match = re.search(pattern, mail)
    return 'Valid' if match else 'Not valid'

#--------------------------------------------------------------
# Task 4
# 4. Напишите функцию, проверяющую правильность логина. 
# Правильный логин – строка от 2 до 10 символов, содержащая 
# только буквы и цифры.

log = input('>>> ')
pattern_1 = r'^\w{2,10}$'
pattern_2 = r'^[a-zA-Z0-9]{2,10}$'

def regex_4(pattern, login):
    match = re.search(pattern, login)
    return 'Valid' if match else 'Not valid'

print(regex_4(pattern_1, log))
print(regex_4(pattern_2, log))
