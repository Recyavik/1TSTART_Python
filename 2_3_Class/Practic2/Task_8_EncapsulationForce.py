# Классы позволяют скрывать и упаковывать данные внутри объекта,
# защищая их от несанкционированного доступа и изменений.
# Инкапсуляция заключается в объединении данных (атрибутов) и методов,
# которые манипулируют данными, в одной структуре (классе).
# Это защищает данные от несанкционированного доступа
# и позволяет управлять ими только с помощью методов объекта.

class MyClass:
    def __init__(self):
        self.__private_attribute = 10

    def __private_method(self):
        return "This is a private method."


# obj = MyClass()
# obj.__private_attribute
# AttributeError: 'MyClass'object has no attribute '__private_attribute'
# obj.__private_method()
# AttributeError: 'MyClass'object has no attribute '__private_method'


obj = MyClass()
print(obj._MyClass__private_attribute)  # type: ignore
print(obj._MyClass__private_method())  # type: ignore
