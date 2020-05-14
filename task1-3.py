x = [x for x in range(220, 225+1)]
print('\n')
print(x)
print('\n')

def qwerty(a, b):
    if not isinstance(a, (list)): return False

    try:
        res = a.index(b)
    except Exception as e:
        res = False

    return (res, b)

def qwerty2(a, b):
    if not isinstance(a, (list)): return False

    start_index = 0
    stop_index = len(a)-1
    center_index = (a.__len__()) // 2

    while a[center_index] != b and start_index <= stop_index:
        if a[center_index] > b:
            stop_index = center_index - 1
        else:
            start_index = center_index + 1

        center_index = int((stop_index + start_index) / 2)

    if (start_index > stop_index):
        res = False
    else:
        res = center_index

    return (res, b)



print(qwerty(x, 221))
print(qwerty(x, 50))

print('\n')

print(qwerty2(x, 229))
print(qwerty2(x, 224))
