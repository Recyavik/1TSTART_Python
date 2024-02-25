def my_function():
    print("Функция вызвана из другого модуля")

def add(a, b):
    return a + b

def multi(a, b):
    return a * b

if __name__ == "__main__":
    print("Сообщение изнутри модуля")