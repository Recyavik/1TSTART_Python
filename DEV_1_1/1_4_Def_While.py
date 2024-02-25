def count_book(st):
    n, k, m = devision_space(st)
    if n == 0 or k == 0 or m == 0:
        return 0
    elif m > k or k > n or m > n:
        return 0
    else:
        book = 0
        while n >= k:
            block = n // k
            book += block * (k // m)
            n -= block * (k // m) * m
        return book

def devision_space(st):
    listok = st.split()
    return int(listok[0]), int(listok[1]), int(listok[2])


print(count_book("10 5 2"))