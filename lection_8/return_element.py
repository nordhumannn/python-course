def return_element(start: int, stop: int, predicate):
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError('Unsupportable value')
    count = 0
    while count < stop:
        yield predicate(start)
        start += 1
        count += 1

def rule_1(item):
    return item ** 2

def rule_2(item):
    return item % 2

def rule_3(item):
    if item == 1:
        return 0
    if item == 2:
        return 1
    if item > 2:
        return rule_3(item - 1) + rule_3(item - 2)


for item in return_element(1, 10, rule_3):
    print(item)

x = return_element(1, 10, rule_1)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#-----------------------------------------------

def get_next_item(start: int | float, step: int | float, n: int, func):
    items = (func(start, step, i) for i in range(n))

    while True:
        try:
            yield next(items)
        except:
            break

def arithmetic_progression(a, dx, n):
    return a + n * dx

def geom_progression(b, q, n):
    return b * q ** (n - 1)

print(*get_next_item(1, 2, 20, arithmetic_progression))
