class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, w):
        self.__width = w
        # print(f"Назначена ширина {w}")
        pass

    def get_height(self):
        return self.__height

    def set_height(self, h):
        self.__height = h
        # print(f"Назначена высота {h}")
        pass

    def area(self):
        return self.__width * self.__height


rect1 = Rectangle(10, 20)
rect1.set_width(30) # rect1.width = 30


print(rect1.area())
# print(rect1.width) # Ошибка
# print(rect1.height) Ошибка
# print(rect1.Rectangle__width) # делай так

print(rect1.get_width())
rect1.set_height(40)
print(rect1.get_height())
print(rect1.area())
