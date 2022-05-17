import math

#1
print("Hello, World!")

#2
print("Python")
print("is")
print("the best")

#3
length = int(input("Enter a length value: "))
width = int(input("Enter a width value: "))
area = length * width

print(f"Area of a rectangle: {area}")

#4
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(num1 + num2)
print(num1 * num2)
print(num1 - num2)
print(num1 / num2)

#5
radius = int(input("Enter a radius value: "))
pi = 3.14159

print("Diameter:", radius * 2)
print("Circumference:", 2 * pi * radius)
print("Area:", pi * radius ** 2)

--------------------------------------

#1
num3 = "123"
num3 = int(num3)

#2
num4 = 123
num4 = float(num4)

#3
num5 = 12.345
num5 = int(num5)

#4
card_num = int(input("Enter a card number: "))
print(str(card_num)[:-5:-1])

#5
num6 = int(input("Enter a 3-digit number: "))
res = (num6 // 100) + (num6 % 100 // 10) + (num6 % 10)
print(res)

6
side_a = int(input("Enter a value of side A: "))
side_b = int(input("Enter a value of side B: "))
side_c = int(input("Enter a value of side C: "))

p = (side_a + side_b + side_c) / 2
area = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

print(f"Area of a triangle: {area}")

#7
num7 = int(input("Enter a 4 digit number: "))
res = (num7 // 1000)+ (num7 % 1000 // 100) + (num7 % 100 // 10) + (num7 % 10)

print(res)

#8
num8 = int(input("Enter a number: "))
digits = len(str(num8))

print(digits)

#9
num9 = int(input("Enter a number: "))
print(str(num9)[::-1])
