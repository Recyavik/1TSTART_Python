# В первой строке файла month.txt хранится словарь: ({1: "Январь", 2:"Февраль", 3: "Март", 4: "Апрель",
# 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь "}).
# Прочитайте его из файла и перезапишите его в виде списка значений в новый бинарный файл month_new.dat

import pickle


def save_binary(file_output, data):
    with open(file_output, "wb") as file:
        pickle.dump(data, file)

def open_file(file_path, mode="r", code="utf-8"):
    try:
        file = open(file_path, mode, encoding=code) # encoding="cp1252"
    except IOError as e:
        print("Ошибка открытия файла:", e)
        file = None
    return file

def read_file(file):
    if file is None:
        print("Файл не открыт")
        data = None
    else:
        data = file.read()
    return data

def close_file(file):
    if file is not None:
        file.close()
        file = None

my_file = open_file("month.txt", "r")
data_read = read_file(my_file)
print(data_read)
data_dict = dict([sub.split(': ') for sub in data_read.split(',\n')])
print(data_dict)
month_list = list()
for value in data_dict.values():
    month_list.append(value)

close_file(my_file)
print(month_list)

save_binary("month.dat", month_list)
