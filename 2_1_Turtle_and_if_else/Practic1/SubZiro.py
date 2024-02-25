"""Инициализация и настройка:

turtle.Screen(): Создает и возвращает объект экрана.
turtle.Turtle(): Создает новый объект Turtle (черепаху).
speed(speed): Устанавливает скорость движения черепахи от 1 (очень медленно) до 10 (очень быстро)."""

"""Движение:

forward(distance) или fd(distance): Двигает черепаху вперед на указанное расстояние.
backward(distance) или bk(distance): Двигает черепаху назад на указанное расстояние.
left(angle) или lt(angle): Поворачивает черепаху налево на указанный угол.
right(angle) или rt(angle): Поворачивает черепаху направо на указанный угол."""

"""Рисование:

penup() или pu(): Поднимает перо, и черепаха перестает рисовать при движении.
pendown() или pd(): Опускает перо, и черепаха начинает рисовать при движении.
color(color_name): Устанавливает цвет пера.
begin_fill(): Начинает заливку фигуры.
end_fill(): Завершает заливку фигуры."""

"""Форма и цвет:

shape(shape_name): Устанавливает форму черепахи ("arrow", "turtle", "circle", "square", "triangle", и др.).
shapesize(stretch_wid, stretch_len, outline): Устанавливает размер и толщину контура черепахи.
fillcolor(color_name): Устанавливает цвет заливки."""

"""
Другие команды:

circle(radius, extent=None): Рисует круг или дугу указанного радиуса. Если указан extent, рисует дугу заданного угла.
goto(x, y) или setpos(x, y): Перемещает черепаху в указанную точку.
clear(): Очищает экран.
reset(): Сбросить черепаху в начальное состояние.
done(): Закрывает окно Turtle."""

"Черепаха может двигаться вперед, назад, поворачивать влево и вправо, поднимать и опускать перо."
import turtle

t = turtle.Turtle()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.right(90)
# t.backward(50)
#
#
# "Помимо простого перемещения, черепаха может рисовать круги и другие фигуры."
# t.circle(50)  # рисует круг радиусом 50
#
# "Черепаха может менять цвет своего пера и заливать фигуры разными цветами."
# t.pencolor("red")  # меняем цвет пера на красный
# t.fillcolor("yellow")  # устанавливаем желтый цвет заливки
# t.begin_fill()  # начинаем заливку
# t.circle(50)  # рисуем круг
# t.end_fill()  # заканчиваем заливку


# "простой цветок"
# import turtle
#
# # Настройка окна
# screen = turtle.Screen()
# # screen.bgcolor("skyblue")
#
# # Создаем черепаху
# flower = turtle.Turtle()
# flower.speed(5)  # Средняя скорость
#
# # Рисуем лепестки цветка
# flower.color("pink")
#
# flower.circle(50)  # Рисуем круг (лепесток)
# flower.left(90)  # Поворот на 90 градусов
#
# flower.circle(50)  # Рисуем круг (лепесток)
# flower.left(90)  # Поворот на 90 градусов
#
# flower.circle(50)  # Рисуем круг (лепесток)
# flower.left(90)  # Поворот на 90 градусов
#
# flower.circle(50)  # Рисуем круг (лепесток)
# flower.left(90)  # Поворот на 90 градусов
#
# # Рисуем стебель
# flower.color("green")
# flower.right(90)
# flower.forward(150)
#
# turtle.done()







"Солнце в углу экрана"
# import turtle
#
# # Настройка окна
# screen = turtle.Screen()
# screen.bgcolor("skyblue")
#
# # Создаем черепаху
# sun = turtle.Turtle()
# sun.speed(5)
# sun.color("yellow")
#
# # Перемещаем черепаху в верхний правый угол
# sun.penup()
# sun.goto(290, 270)
# sun.pendown()
#
# # Рисуем солнце
# sun.begin_fill()
# sun.circle(30)
# sun.end_fill()
#
# turtle.done()
#
#
#
# "Цель этого примера - создать радужную спираль с использованием цикла и изменением цвета."
# import turtle
#
# # Настройка окна
# screen = turtle.Screen()
# screen.bgcolor("black")  # Устанавливаем черный фон
#
# # Создаем черепаху
# rainbow_spiral = turtle.Turtle()
# rainbow_spiral.speed(10)  # Устанавливаем максимальную скорость
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  # Определение цветов радуги
#
# # Рисуем спираль
# for i in range(360):
#     rainbow_spiral.pencolor(colors[i % 7])  # Выбор цвета из списка
#     rainbow_spiral.width(i / 100 + 1)  # Увеличение толщины линии
#     rainbow_spiral.forward(i)
#     rainbow_spiral.left(59)
turtle.done()