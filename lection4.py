#1 
for i in range(100):
	if not i % 7:
		print(i)

#2
n = int(input('>>> '))
res = n

for i in range(2, n):
	res *= i
print(res)

#3
n = int(input('>>> '))

for i in range(11):
	print(f'{n} * {i} = {n * i}')

#4
x = int(input('Width: '))
y = int(input('Height: '))

for i in range(y):
	if i == 0 or i == y - 1:
		for j in range(x):
			print('*', end='')
	else:
		print('*', end='')
		for j in range(1, x - 1):
			print(' ', end='')
		print('*', end='')
	print()

#5
for i in range (2, 100):
    flag = True
    for j in range (2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)

#6
n = int(input('N: '))

space = 0

for i in range(n, 0, -2):
	print(f"{' ' * space}{'*' * i}")
	space += 1
space -= 2
for i in range(3, n + 1, 2):
	print(f"{' ' * space}{'*' * i}")
	space -= 1
