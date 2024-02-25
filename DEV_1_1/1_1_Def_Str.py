def process_list(a):
    count = 0
    for el in a:
        st = str(el)
        before = st[0]
        for i in range(1, len(st)): # Акцент -1
            if st[i] > before:
                break
            else:
                before = st[i]
        else:
            count +=1
    return count

print(process_list([1234, 6734, 9531, 4523, 1354, 7501]))
