#------ 1 ------

nums = [23, 45, 12, 67, 34, 45, 23, 78, 96]

def max_num(a):
    return max(a)

print(max_num(nums))

#------ 2 ------

def func(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, str):
        return None
    return f'{a + b}{c}'

print(func(2, 4, 'hello'))

#------ 3 ------

x, y = int(input('X: ')), int(input('Y: '))

def rectangle(x, y):
    mid = (y - 2) * f"*{' ' * (x - 2)}*\n"
    res = f"{'*' * x}\n{mid}{'*' * x}\n"
    return res

print(rectangle(x, y))

#------ 4 ------

from random import randint

nums = []
for i in range(50):
    nums.append(randint(1, 50))

num = int(input('>>> '))

def search_num(a):
    if a in nums:
        return nums.index(a)
    else:
        return -1

print(search_num(num))

#------ 4 ------

text = input('>>> ')

def words(text):
    return len(text.split())

print(words(text))
