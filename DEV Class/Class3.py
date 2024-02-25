# Создайте класс EvenChecker и реализуйте в нем метод is_even(self, number).
# Данный метод возвращает значение типа bool и проверяет является ли число четным.
# Если переданное в метод число четное, то метод возвращает true, иначе false.
# Созданный класс расположите на месте троеточия как представлено в шаблоне кода.

class EvenChecker:

    def is_even(self, number) -> bool:
        if number % 2 == 0:
            logic_flag = True
        else:
            logic_flag = False
        return logic_flag
#TODO Здесь создайте класс
even_checker = EvenChecker()
if even_checker.is_even(24):
    print("Четное число")
else:
    print("Нечётное число")
