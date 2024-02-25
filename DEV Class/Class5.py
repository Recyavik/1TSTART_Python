# Создайте класс Cat с конструктором __init__(self, name, breed, age, color), который устанавливает значения атрибутов класса согласно переданным параметрам name, breed, age, color.
# Добавьте в класс Cat метод print_info(self), который выводит в консоль всю информацию по объекту в виде: Имя: name, порода: breed, возраст: age, окрас: color.
# Создайте экземпляр класса Cat и выведите всю информацию о данном экземпляре в консоль с помощью метода print_info.

"""
Пример вывода:
Имя: Барсик, порода: дворовый, возраст: 3, окрас: рыжий.
""" #

class Cat:
    def __init__(self, name, breed, age, color):
       self.name = name
       self.bread = breed
       self.age = age
       self.color = color

    def print_info(self):
        print(f'Имя: {self.name}, порода: {self.bread}, возраст: {self.age}, окрас: {self.color}.')


cat1 = Cat('Барсик', 'дворовый', 3, 'рыжий')
cat1.print_info()



