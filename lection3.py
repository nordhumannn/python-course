#1
apart = int(input("Номер квартиры: "))
floor = 9
entrance = 4
num = 4

total_apart = floor * num
entrance_res = (apart - 1) // total_apart + 1
floor_res = (apart % total_apart) // 4 + 1

print(entrance_res, floor_res)

#2
year = int(input('Enter a year: '))

if (not year % 4 and year % 100) or (not year % 400):
	print(f"{year}: высокосный год")
else:
    print(f"{year}: не высокосный год")

#3  
side_a = int(input("Enter a value of side A: "))
side_b = int(input("Enter a value of side B: "))
side_c = int(input("Enter a value of side C: "))

if (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_c + side_b) > side_a:
    print("This triangle exists")
else:
    print("This triangle cannot exist")
