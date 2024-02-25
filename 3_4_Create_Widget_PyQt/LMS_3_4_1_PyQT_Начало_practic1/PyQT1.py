from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
                             QPushButton, QLineEdit, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 500, 220)
        self.initUI()

    def initUI(self):
        # Создание виджетов
        self.layout_login = QHBoxLayout()
        self.layout_password = QHBoxLayout()
        self.layout_button = QVBoxLayout()

        self.lbl_login = QLabel("Логин:", self)
        self.lbl_login.setFixedSize(60, 30)
        self.layout_login.addWidget(self.lbl_login)

        self.input_login = QLineEdit(self)
        self.input_login.setFixedSize(300, 30)
        self.layout_login.addWidget(self.input_login)

        self.lbl_password = QLabel("Пароль:", self)
        self.lbl_password.setFixedSize(60, 30)
        self.layout_password.addWidget(self.lbl_password)

        self.input_password = QLineEdit(self)
        self.input_password.setFixedSize(300, 30)
        self.layout_password.addWidget(self.input_password)

        self.btn_entrance = QPushButton(self)
        self.btn_entrance.setText("Вход")
        self.btn_entrance.setToolTip("Проверить доступ")
        self.btn_entrance.resize(self.btn_entrance.sizeHint())
        self.btn_entrance.clicked.connect(self.check_pass)
        self.layout_button.addWidget(self.btn_entrance)

        self.lbl_is_entrance = QLabel("", self)
        self.layout_button.addWidget(self.lbl_is_entrance)


        main_layout = QVBoxLayout()
        main_layout.addLayout(self.layout_login)
        main_layout.addLayout(self.layout_password)
        main_layout.addLayout(self.layout_button)


        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def check_pass(self):
        if self.input_login.text() == "Администратор" and self.input_password.text() == "12345":
            self.lbl_is_entrance.setText("Доступ разрешён!")
        else:
            self.lbl_is_entrance.setText("Доступ запрещен!")


if __name__ == '__main__':
    app = QApplication([])
    my_win = MainWindow()
    my_win.show()
    app.exec()