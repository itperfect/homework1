def summ1(a, b):
    res = 0
    for cnt in range(a, b+1):
        res += cnt
    return res


def summ2(a, b):
    res = 0
    a = [x for x in range(a, b+1)]
    for cnt in a:
        res += cnt
    return res


def summ3(a, b):
    res = 0
    for cnt in [x for x in range(a, b+1)]:
        res += cnt
    return res


a = 1
b = 9124561


print(summ1(a,b))
print(summ2(a,b))
print(summ3(a,b))
