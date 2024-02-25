# Бинарные файлы, в отличие от текстовых, хранят информацию в виде набора байт.
# Для работы с ними в Python необходим встроенный модуль «pickle». Этот модуль предоставляет два метода:
# •	dump(obj, file): записывает объект obj в бинарный файл file
# •	load(file): считывает данные из бинарного файла в объект
# При открытии бинарного файла на чтение или запись также надо учитывать,
# что нам нужно применять режим "b" в дополнение к режиму записи ("w") или чтения ("r").

import pickle

file_path = "user.dat"

name = "Viktor"
age = 45

with open(file_path, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(file_path, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)


file_path = "users_list.dat"

users = [
    ["Аня", 28, True],
    ["Глеб", 23, False],
    ["Семён", 34, False]
]

with open(file_path, "wb") as file:
    pickle.dump(users, file)

with open(file_path, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:", user[1], "\tГосслужащий:", user[2])

# В зависимости от того, какой объект мы записывали функцией dump, тот же объект будет
# возвращен функцией load при считывании файла.
# Таким образом, используя методы считывания и записи данных, у нас всегда есть возможность структурированно
# хранить информацию не только в памяти компьютера, но и на различных носителях.
