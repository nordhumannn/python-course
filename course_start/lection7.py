#----------------------- 1st task -------------------------

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday', 
    4: 'Thursday', 
    5: 'Friday', 
    6: 'Saturday',
    7: 'Sunday'
}

num = int(input('Day number: '))

print(f'{num} - {days[num]}')

#----------------------- 2nd task -------------------------

cat = {
    'name': 'Charlie',
    'color': 'Black & white',
    'age': '1 year',
    'fav_food': 'Fish'
}

print(cat)

#----------------------- 3rd task -------------------------

s = input('>>> ')
res = {}

for i in s:
    if not res.get(i):
        res[i] = s.count(i)

for key, value in res.items():
    print(key, value)

#----------------------- 4th task -------------------------

from num2words import num2words

num = int(input('>>> '))

print(num2words(num))

#----------------------- 5th task -------------------------

num = int(input('>>> '))

ones = {
    0: '', 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"
}
tens = {
    1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"
}

if num < 10:
    print(ones[num])
else:
    o = num % 10
    t = num // 10
    print(f'{tens[t]}{ones[o]}')
