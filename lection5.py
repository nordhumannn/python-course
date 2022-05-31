#1
num = input('Number: ')
lis = [int(i) for i in num]
sum1, sum2 = 0, 0
n = len(num) // 2

if not len(num) % 2:
	for i in lis[:n]:
		sum1 += i
	for i in lis[n:]:
		sum2 += i
		
	if sum1 == sum2:
		print('Happy ticket')
	else:
		print('Not a happy ticket')
else:
	print('This ticket is not valid')

#2
num = input('Number: ')
lis = [int(i) for i in num]
n = len(num) // 2

part1 = lis[:n]
part2 = lis[:-n-1:-1]

if part1 == part2:
	print(f'{num} - is a Palindrome')
else:
	print(f'{num} - is NOT a Palindrome')

#3
import math

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
r = 4

xy_r = math.sqrt(x**2 + y**2)

if xy_r <= r:
	print(f'Point{x, y} belongs to circle')
else:
	print(f'Point{x, y} does NOT belong to circle')

#4
lis = [0, 5, 2, 4, 7, 1, 3, 19]
res = 0

for i in lis:
	if i % 2:
		res += 1

print(res)

#5
from random import randint

lis1 = []

for i in range(4):
	lis1.append(randint(1, 4))

lis2 = lis1[:]

for i in lis1:
	lis2.append(i * 2)

print(lis2)

#6
from random import randint

salary = []
res = 0

for i in range(12):
	salary.append(randint(7500, 15000))

for i in salary:
	res += i

print(salary)
print(f'Average salary: {res // 12}')

#7
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in matrix:
	print(i)

summ = sum(matrix[0][:] + matrix[1][:] + matrix[2][:] + matrix[3][:])

print(summ)
