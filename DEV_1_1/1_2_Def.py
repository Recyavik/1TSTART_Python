"""
Создайте функцию process_list(a), которая принимает на вход список a, 
заполненный значениями от 1000 до 10000. Функция должна вычислить количество элементов в списке, 
у которых сумма первых двух цифр числа больше суммы последних двух цифр. 
Функция должна вернуть общее количество таких чисел.
""" #
def process_list(a):
    count = 0
    for el in a:
        if el < 1000 or el > 10000:
            continue
        if (el // 10000 + el // 1000 + (el // 100 % 10)) > (el % 10) + ((el % 100 // 10)):
            count +=1
    return count

print(process_list([1234, 6734, 9531, 4523, 1354, 7521, 999, 456456546]))
