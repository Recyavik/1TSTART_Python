import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtWidgets import QApplication

# QPropertyAnimation это интерфейс, построенный на свойствах, которые можно использовать для анимации
# - или интерполяции - между начальными и конечными значениями для данного свойства.
# Используя этот интерфейс мы можем инициировать изменение и автоматически установить ряд временных значений.
# Если изменение этого свойства вызовет обновление виджета (или мы используем значение animated в paintEvent()),
# виджет будет отображаться как анимированный.
# Приведу несколько примеров использования QPropertyAnimation для анимации положения простого QWidget квадрата,
# заполненного красным цветом, в окне.


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red; border-radius:15px;")
        self.child.setGeometry(20, 40, 100, 100)

        self.anim = QPropertyAnimation(self.child, b"pos")
        # Анимация обновляет положение виджета с помощью .pos,
        # что автоматически запускает перерисовку с помощью Qt.
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        # self.anim.setEasingCurve(QEasingCurve.OutInExpo)
        # self.anim.setEasingCurve(QEasingCurve.InBack)
        # self.anim.setEasingCurve(QEasingCurve.OutBounce)
        # https://doc.qt.io/qt-5/qeasingcurve.html

        self.anim.setEndValue(QPoint(480, 480))
        self.anim.setDuration(3500)
        self.anim.start()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
# По умолчанию анимация линейная,с QWidget перемещением в конечное положение с постоянной скоростью.
# Вместо простой линейной анимации часто требуется добавить ускорение и деакселерацию к анимации.
# Это может быть полезно для создания виджетов, которые кажутся реалистичными и физическими,
# или для добавления интересных эффектов, привлекающих внимание.
# Чтобы добавить ускорение и деакселерацию к анимации, вы используете сглаживающие кривые через QEasingCurve.

# Для создания анимации с помощью QPropertyAnimation вам необходимо предоставить следующее --
#
# укажите, QPropertyAnimation какой объект мы хотим анимировать, здесь self.child
# Укажите имя свойства здесь b"pos" (должно быть указано в байтах b"value")
# [Необязательно] значение start.
# Значение end.
# [Необязательно] длительность интерполяции [в мс], по умолчанию это 250 мс.

if __name__ == "__main__":
    main()
