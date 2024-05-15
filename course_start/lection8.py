#-------- 1 --------

s1 = input('>>> ')
s2 = input('>>> ')

print(set(s1).intersection(set(s2)))

#-------- 2 --------

lis1 = [i for i in range(50) if not i % 3]
lis2 = [i for i in range(50) if not i % 5]

res = list(set(lis1).intersection(set(lis2)))

print(res)
