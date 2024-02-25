# Математический тренажёр
# Консольный тренажёр задает 5 случайных примеров на сложение, вычитание, умножение и деление двух чисел
# Все ответы примера натуральные числа (целые 0, 1, 2, ..., n-1, n)
# Тренажер должен давать 3 попытки на ввод каждого ответа
# В конце 5 заданий тренажер должен выдать статистику правильно решенных примеров.

import random as rnd


print("Математический тренинг из 5 заданий")
# Количество правильных ответов
counter_correct_answers = 0
for i in range(5):
    a = rnd.randint(0, 10)
    b = rnd.randint(0, 10)
    while b == 0:
        b = rnd.randint(0, 10)
    op = ""
    result = 0
    if a < b:
        a, b = b, a
    op = rnd.choice(["+", "-", "*", ":"])
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == ":":
        result = a * b
        result, a = a, result
    print(f"\nРеши {i+1}-й пример:")
    example = f"{a}{op}{b}="
    answer = ""
    flag_result = False
    # Количество попыток
    counter_attempt = 0
    # Количество попыток
    number_attempt = 3
    while answer.isalpha() or len(answer) == 0 or not flag_result:
        answer = input(example)
        if answer.isalpha() or len(answer) == 0:
            print("Недопустимые символы ответа. Повторите ввод!")
        else:
            answer_user = int(''.join(i for i in answer if i.isdigit()))
            if answer_user == result:
                print(rnd.choice(["Молодец!", "Супер!", "Отлично!", "Правильно!"]))
                flag_result = True
                counter_correct_answers += 1
            else:
                print(rnd.choice(["Эx...!", "Жаль!", "А если подумать ?", "Не правильно!"]))
                counter_attempt += 1
                if counter_attempt == number_attempt:
                    print(f"Запомни: {example}{result}")
                    flag_result = True
                else:
                    flag_result = False
                    print("Попробуй ещё раз...")

print(f"\nЗдорово! Ты решил правильно {counter_correct_answers} из 5 заданий! \nВозвращайся еще порешаем!")
