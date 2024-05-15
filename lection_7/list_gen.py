length = int(input('>>> '))
a = (i ** 3 for i in range(2, length))
b = list(a)

print(b)
