from math import ceil

#1
apart = int(input('Flat: '))
floor, entrance, num = 9, 4, 4

total_apart = floor * num
entrance_res = (apart - 1) // total_apart + 1
floor_res = (apart % total_apart) // 4 + 1

print(f'Entrance: {entrance_res}, floor: {floor_res}')

#1.1
n = int(input('>>> '))

if n <= 4 * 9:
    print(f'Flat: {n}, entrance 1, floor: {ceil(n / 4)}')
elif 4 * 9 < n <= 4 * 9 * 2:
    print(f'Flat: {n}, entrance 2, floor: {ceil(n / 4) - 9}')
elif 4 * 9 * 2 < n <= 4 * 9 * 3:
    print(f'Flat: {n}, entrance 3, floor: {ceil(n / 4) - 18}')
elif 4 * 9 * 3 < n <= 4 * 9 * 4:
    print(f'Flat: {n}, entrance 4, floor: {ceil(n / 4) - 27}')
else:
    print('There is no such flat')

#2
year = int(input('Enter a year: '))

if (not year % 4 and year % 100) or (not year % 400):
	print(f"{year}: высокосный год")
else:
    print(f"{year}: не высокосный год")

#3  
a, b, c = map(int, input('Enter the value of the sides(3): ').split(','))
res = True if a + b > c and b + c > a and a + c > b else False

print(res)
