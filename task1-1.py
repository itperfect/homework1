a = [x for x in range(9999999 + 1)]

def result(d):
    if not isinstance(d, (list)):
        return False, False

    cnt_even = 0
    cnt_odd = 0
    for number in d:
        if number == 0:
            continue
        elif number%2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1

    return cnt_even, cnt_odd

p1,p2 = result(a)
print(f'Even count: {p1} \n' + f'Odd count: {p2}')

