# Пример обработки события завершения программы при нажатии клавиши "q":

import turtle
def exit_on_q():
 turtle.bye()

turtle.Screen().onkeypress(exit_on_q, "q")
turtle.listen()
turtle.mainloop()

# В данном примере, функция exit_on_q() будет вызываться при нажатии клавиши "q",
# и она закроет окно turtle с помощью метода turtle.bye().
# Функция turtle.listen() необходима для активации прослушивания событий клавиатуры,
# а метод turtle.mainloop() запускает цикл обработки событий.