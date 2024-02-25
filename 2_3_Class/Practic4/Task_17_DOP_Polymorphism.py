class Figure:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print("Figure")
        print("Color: " + self.__color)


class Rectangle(Figure):

    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Area: " + str(self.area()))

    def area(self):
        return self.__width * self.__height


fig = Figure("orange")
fig.info()

rect = Rectangle(10, 20, "green")
rect.info()

# Полиморфизм — когда наследники делают все по своему, но результат работы такой же как у базового класса.
# Если наследник занимается чем-то своим и не дает результат такой, который ожидается от базового
# класса — значит с наследованием и полиморфизмом что-то не так.
# Пример: есть базовый класс автомобиль, который предположительно должен заехать в гараж.
# Создаем летающий автомобиль-наследник (как в фильме «Назад в будущее 2»).
# Какой будет результат при попытке загнать этого монстра в гараж?
# Да, он может залететь в гараж, если функция езды будет полностью заменена на функцию полета.
# А если функция полета была новым функционалом, а функция езды вообще заблокирована?
# То мы не сможем спрятать нашего летуна от непогоды.
# Это уже не будет автомобиль, это будет что-то новое.
# Результат — из-за неправильного моделирования и наследования был нарушен принцип полиморфизма
# и получился нежелательный результат.