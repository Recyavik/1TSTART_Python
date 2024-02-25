def process_list(a):
    flag = False
    s1 = 0
    s2 = 0
    i = 0
    for el in a:
        if i % 2 == 0:
            s1 += el
        else:
            s2 += el
        i += 1
        if s1 - s2 > 0:
            flag = True
        else:
            flag = False
    return flag

print(process_list([7771234, 999999996734, 9531, 4523, 1354, 77777, 999, 54]))
