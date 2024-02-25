def my_function():
    print('Эта функция была вызвана из другого модуля')

def add(a, b):
    return a + b * 2

def multi(a, b):
    return a * b

if __name__ == '__main__':
    print('Сообщение изнутри модуля')