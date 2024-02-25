# В списке (['ПН', 'ВТ', 'СР', 'ЧТ','ПТ', 'СБ', 'ВС']) хранятся данные о днях недели.
# Создайте текстовый файл, в котором будет хранится этот список записанный через пробел:
# Содержимое файла должно быть таким: ПН ВТ СР ЧТ ПТ СБ ВС

def open_file(file_path, mode="r+", code="utf-8"):
    try:
        file = open(file_path, mode, encoding=code) # encoding="cp1252"
    except IOError as e:
        print("Ошибка открытия файла:", e)
        file = None
    return file

def write_file(file, data):
    if file is None:
        print("Файл не открыт.")
    else:
        file.write(data)

def close_file(file):
    if file is not None:
        file.close()
        file = None

week = ['ПН', 'ВТ', 'СР', 'ЧТ','ПТ', 'СБ', 'ВС']

mode_cs = ''
print('Как хотите разместить файлы в столбик или через пробел [col/space] ?')

while mode_cs != 'col' and mode_cs != 'space':
    mode_cs = input('Укажите col - если в столбик, space - если через пробел: ')

my_file = open_file("week.txt","w+")
data_write = ''
for el in week:
    if mode_cs == 'col':
        el = el + '\n'
    else:
        el = el + ' '
    data_write += el

print(data_write)
write_file(my_file, data_write)
close_file(my_file)

