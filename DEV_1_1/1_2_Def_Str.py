def process_list(a):
    count = 0
    for el in a:
        if el < 1000:
            continue
        st = str(el)
        if int(st[0]) + int(st[1]) > int(st[-1]) + int(st[-2]):
            count +=1
    return count

print(process_list([1234, 6734, 9531, 4523, 1354, 7521]))
