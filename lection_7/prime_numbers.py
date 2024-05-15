def prime_nums(n):
    x = 1

    while x <= n:
        flag = True
        for i in range(2, x):
            if not x % i:
                flag = False
                break
        if flag:
            yield x
        x += 1

prime_nums = list(item for item in prime_nums(100))

print(prime_nums)

#-----------------------------

def prime_nums(stop):
    for n in range(1, stop):
        for i in range(2, n):
            if not n % i:
                break
        else:
            yield n
