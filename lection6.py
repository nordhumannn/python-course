# 1
s = input('>>> ')
res = 0

for item in s:
    if item == 'b':
        res += 1

print(res)

# or

s = input('>>> ')
print(s.count('b'))

# 2
name = input('Name: ')

digit = True
n_title = True

for item in name:
    if item.isdigit():
        digit = False

if not name.istitle():
    n_title = False

if not digit or not n_title:
    print('NOT valid')
else:
    print('Valid')

# 3
s = input('>>> ')
res = 0

for item in s:
    res += ord(item)

print(res)

# 4
import math

for n in range(2, 12):
    print(f'{math.pi:.{n}f}')

# 5
s = input('>>> ')
print(max(s.split(), key=len))
