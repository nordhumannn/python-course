#1
num = int(input("Enter a number: "))

if num < 0:
    print(f"Negative number: {num}")
else:
    print("Positive number")

#2
num2 = int(input("Enter a number: "))

if num2 < 20:
    print(f"{num2} is less than 20")
else:
    print(f"{num2} is greater than 20")

#3
num3 = int(input("Enter a number: "))

if num3 == 0:
    print("Given number is zero")
else:
    print("Given number is not zero")

#4
num4 = int(input("Enter a number: "))

if num4 % 2 == 0:
    print(f"{num4} is an even number")
else:
    print(f"{num4} is an odd number")

#5
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 1st number: "))
n3 = int(input("Enter 1st number: "))

max_num = n1

if n2 > max_num:
    max_num = n2
if n3 > max_num:
    max_num = n3

print(f"Max number: {max_num}")
