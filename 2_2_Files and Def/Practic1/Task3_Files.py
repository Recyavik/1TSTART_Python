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
        file = None

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="all", return_type="string")
print(data_read)
close_file(my_file)
print()

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="all", return_type="list")
print(data_read)
close_file(my_file)
print()

my_file = open_file("some2.txt")
data_read = read_file(my_file, mode_read="all", return_type="dict")
print(data_read)
close_file(my_file)
print()

