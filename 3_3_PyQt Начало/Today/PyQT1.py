# PyQt предоставляет возможность использования функциональности Qt в языке программирования Python.
# Он содержит привязки к классам и функциям Qt,
# позволяющие разработчикам создавать кроссплатформенные приложения с помощью Python.
# PyQt обеспечивает простой доступ к возможностям Qt,
# включая создание графического интерфейса с помощью виджетов,
# обработку событий, работу с базами данных, работу с сетью и многое другое.

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 200, 160)
        self.button1 = QPushButton(self)
        self.button1.setGeometry(30, 10, 100, 30)
        self.button1.setText('Кнопка 1')
        self.button2 = QPushButton(self)
        self.button2.setGeometry(30, 40, 100, 30)
        self.button2.setText('Кнопка 2')
        self.button3 = QPushButton(self)
        self.button3.setGeometry(30, 70, 100, 30)
        self.button3.setText('Кнопка 3')
        self.label_info = QLabel(self)
        self.label_info.setGeometry(30, 100, 180, 30)
        self.button1.clicked.connect(self.dialog_message)
        self.button2.clicked.connect(self.button_clicked_check)
        self.button3.clicked.connect(self.block_size_window)

    def button_clicked_check(self):
        self.label_info.setText('Вы нажали кнопку №2')

    def dialog_message(self):
        QMessageBox.information(self, "Диалоговое окно", "Нажата кнопка №1")

    def block_size_window(self):
       self.setMinimumSize(QSize(480, 180))
       self.setMaximumSize(QSize(480, 180))


if __name__ == '__main__':
    app = QApplication([])
    mw = MyWindow()
    mw.show()
    app.exec()