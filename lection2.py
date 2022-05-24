#1
num = int(input("Enter a number: "))
print((num < 0 and num) or "")

#2
num2 = int(input("Enter a number: "))
print((num2 < 20 and f"{num2} is less than 20") or f"{num2} is greater than 20"))

#3
num3 = int(input("Enter a number: "))
print((num3 is 0 and "Zero") or (num3 is not 0 and "Not zero"))

#4
num4 = int(input("Enter a number: "))
print((num4 % 2 is 0 and f"{num4} is an even number") or num4 % 2 is not 0 and f"{num4} is an odd number")

#5
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2st number: "))
n3 = int(input("Enter 3st number: "))

max_num = max(n1, n2, n3)

print(max_num)
