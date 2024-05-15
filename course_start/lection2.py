#1
num = int(input("Enter a number: "))
print((num < 0 and num) or "Number greater than zero")

#2
num2 = int(input("Enter a number: "))
print((num2 < 20 and f"{num2} is less than 20") or f"{num2} is greater than 20")

#3
num3 = int(input("Enter a number: "))
print(not num3)

#4
num4 = int(input("Enter a number: "))
print((num4 % 2 and 'Odd number') or 'Even number')

#5
n = input('Enter a number: ').split(',')
n = map(int, n)

print(max(n))
