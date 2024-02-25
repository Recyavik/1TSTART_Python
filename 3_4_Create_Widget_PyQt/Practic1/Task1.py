# При создании пользовательского интерфейса для приложения на PyQt
# можно использовать PyQt Designer или написать код вручную.
# Давайте рассмотрим процесс создания интерфейса на основе написания кода

# В начале файла с кодом приложения импортируйте необходимые модули из библиотеки PyQt:

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QIcon

# Создайте класс, наследующийся от класса QMainWindow,
# который будет представлять главное окно вашего приложения.
# Внутри класса можно определить методы и атрибуты, отвечающие за различные части интерфейса:

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.setGeometry(100, 100, 500, 200)
        self.initUI()
    # def initUI(self):
    #     # Добавьте код для создания интерфейса здесь
    #     pass
    def initUI(self):
        # Создание виджетов
        label = QLabel("Текстовая метка", self)
        # button = QPushButton("Нажми меня", self)
        button = QPushButton(QIcon('kandi5_new.ico'), 'Нажми на кнопку, получишь результат!', self)
        button.setToolTip('Это подсказка для кнопки')
        button.resize(button.sizeHint())
        # button.move(150, 50)
        # self.show()

        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication([])
    my_win = MainWindow()
    my_win.show()
    app.exec()


