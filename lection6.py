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

name = input('Name: ')

res = 'Valid' if name.istitle() and name.isalpha() else 'NOT valid'

print(res)

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
