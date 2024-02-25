# PyQt предоставляет возможность использования функциональности Qt в языке программирования Python.
# Он содержит привязки к классам и функциям Qt,
# позволяющие разработчикам создавать кроссплатформенные приложения с помощью Python.
# PyQt обеспечивает простой доступ к возможностям Qt,
# включая создание графического интерфейса с помощью виджетов,
# обработку событий, работу с базами данных, работу с сетью и многое другое.
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


# Создаем подкласс QMainWindow
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Устанавливаем размеры окна
        self.setGeometry(100, 100, 300, 200)
        # Создаем виджет QLabel и устанавливаем текст
        self.label = QLabel(self)
        self.label.setText("Текстовая метка, PyQt!")
        # Устанавливаем позицию и размеры QLabel
        self.label.setGeometry(50, 50, 220, 30)
        # Создаем кнопку QPushButton и устанавливаем текст
        self.button = QPushButton(self)
        self.button.setText("Это кнопка - Нажми меня!")
        style_color = "#808080"
        text_color = "#000000"
        font = "Arial"
        font_size = "16"
        color_schema = ("color: " + str(text_color) + "; "
                        + "background-color: " + str(style_color) + "; "
                        "font: " + font + ";" + " font-size: " + font_size + "px;")
        self.button.setStyleSheet(color_schema)

        # Устанавливаем позицию и размеры кнопки
        self.button.setGeometry(50, 100, 210, 30)
        # Подключаем слот к сигналу нажатия кнопки
        self.button.clicked.connect(self.button_clicked_old)
        # self.button.clicked.connect(lambda: self.button_сlicked('Вы нажали кнопку'))
    # Определяем слот, который будет вызываться при нажатии кнопки
    def button_clicked_old(self):
        self.label.setText('Вы всё таки нажали кнопку!')

    def button_clicked(self, message):
        self.label.setText(message)
        
# Создаем экземпляр QApplication
if __name__ == '__main__':
    app = QApplication([])
    mw = MyWindow()
    mw.show()
    app.exec()