from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QPushButton


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(400, 100, 600, 160)
        self.setWindowTitle("Это приложение с кнопками")
        self.btn_dialog = QPushButton(self)
        self.btn_dialog.setText("Диалог")
        self.btn_dialog.setToolTip("Эта кнопка вызывает диалоговое окно")
        self.btn_dialog.setGeometry(100, 10, 100, 30)

        self.btn_test = QPushButton("Тестовая", self)
        self.btn_test.setGeometry(100, 40, 100, 30)
        self.btn_test.setToolTip("Выведет тестовое сообщение на экран приложения")

        self.btn_size = QPushButton("Размеры", self)
        self.btn_size.setGeometry(100, 70, 100, 30)
        self.btn_size.setToolTip("Изменит размеры окна")

        self.lbl_test = QLabel("Статус:", self)
        self.lbl_test.setGeometry(100, 100, 200, 30)

        self.btn_dialog.clicked.connect(self.dialog_message)
        self.btn_test.clicked.connect(self.test)
        self.btn_size.clicked.connect(self.resize_window)


    def dialog_message(self):
        QMessageBox.information(self, "Заголовок диалогового окна", "Нажата кнопка диалог")

    def test(self):
        self.lbl_test.setText("Статус: " + "была нажата кнопка тест")

    def resize_window(self):
        self.setMinimumSize(QSize(600, 180))
        self.setMaximumSize(QSize(680, 200))


if __name__ == "__main__":
    app = QApplication([])
    my_win = MyWindow()
    my_win.show()
    app.exec()

