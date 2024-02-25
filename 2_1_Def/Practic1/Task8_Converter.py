def converter(a, from_n=10, in_n=2):
    dec = int(a, from_n)
    if in_n == 2:
        return str(bin(dec))[2:]
    elif in_n == 8:
        return str(oct(dec))[2:]
    elif in_n == 16:
        return str(hex(dec))[2:]
    elif in_n == 10:
        return str(dec)
    else:
        pass

print(converter('FFFF', 16, 10))