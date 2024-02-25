import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Логин и Пароль')

        self.username_label = QLabel('Логин:')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Пароль:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.submit_button = QPushButton('Войти')
        self.submit_button.clicked.connect(self.check_credentials)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Здесь добавьте логику проверки логина и пароля
        if username == 'user' and password == 'password':
            print('Успешный вход')
        else:
            print('Неверные учетные данные')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())