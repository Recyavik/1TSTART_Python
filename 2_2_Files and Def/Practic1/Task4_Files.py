# Для возврата данных из файла в виде объектов разных типов, можно определить дополнительные параметры
# для функции чтения файла `read_file` или определить отдельные специализированные методы для различных форматов данных.

# Пример расширения функции с поддержкой чтения данных в виде строк, списков и словарей:


import json

def open_file(file_path, mode="r", code="utf-8"):
    try:
        file = open(file_path, mode, encoding=code) # encoding="cp1252"
    except IOError as e:
        print("Ошибка открытия файла:", e)
        file = None
    return file

def read_file(file, mode_read="all", size=None, return_type="string"):
    data = None
# В данном примере `read_file` получает дополнительный параметр `return_type`,
    # который указывает, в каком виде должны быть возвращены данные. Включены три возможных значения:
    #
    # - "string": возвращает данные в виде строки (по умолчанию).
    # - "list": возвращает данные в виде списка, разбив содержимое файла на строки.
    # - "dict": возвращает данные в виде словаря, предполагая, что файл содержит JSON-сериализованный объект.
# Если данные не могут быть преобразованы в словарь, выводится сообщение об ошибке, и метод возвращает `None`.

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

        if return_type == "string":
            data = str(data)
        elif return_type == "list":
            data = data.splitlines()
        elif return_type == "dict":
            try:
                data = json.loads(data)
            except (json.JSONDecodeError, TypeError):
                print("Ошибка преобразования данных в словарь!")

    return data

def write_file(file, data):
    if file is None:
        print("Файл не открыт.")
    else:
        file.write(data)


def close_file(file):
    if file is not None:
        file.close()

my_file = open_file("new_some.txt","w")
write_file(my_file, "В Python существует два типа файлов: текстовые и бинарные")
close_file(my_file)

my_file = open_file("new_some.txt","a")
write_file(my_file, "\nВ Python существует два типа файлов: текстовые и бинарные")
close_file(my_file)
