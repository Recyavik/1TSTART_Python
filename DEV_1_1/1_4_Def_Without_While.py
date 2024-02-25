def count_book(st):
    n, k, m = devision_space(st)
    answer = n // k
    m *= answer
    return (((n - k + 1) // m + bool((n - k + 1) % m)) * answer)

def devision_space(st):
    listok = st.split()
    return int(listok[0]), int(listok[1]), int(listok[2])


print(count_book("10 5 2"))