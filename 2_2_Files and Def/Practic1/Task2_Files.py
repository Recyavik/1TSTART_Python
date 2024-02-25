# Для возврата данных из файла в виде объектов разных типов, можно определить дополнительные параметры
# для функции чтения файла `read_file` или определить отдельные специализированные методы для различных форматов данных

def open_file(file_path, mode="r", code="utf-8"):
    try:
        file = open(file_path, mode, encoding=code) # encoding="cp1252"
    except IOError as e:
        print("Ошибка открытия файла:", e)
        file = None
    return file

def read_file(file, mode_read="all", size=None):
    data = None

    if file is None:
        print("Файл не открыт")
    else:
        if mode_read == "all":
            data = file.read()
        elif mode_read == "line":
            data = file.readline()
        elif mode_read == "lines":
            data = file.readlines()
        elif mode_read == "size" and size is not None:
            data = file.read(size)
    return data

def write_file(file, data):
    if file is None:
        print("Файл не открыт.")
    else:
        file.write(data)

def close_file(file):
    if file is not None:
        file.close()
        file = None

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="all")
print(data_read)
close_file(my_file)
print()

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="line")
print(data_read)
close_file(my_file)

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="lines")
print(data_read)
close_file(my_file)

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="size", size=10)
print(data_read)
close_file(my_file)
