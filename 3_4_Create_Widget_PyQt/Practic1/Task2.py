# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
# from PyQt5.QtGui import QPixmap
# Пример, который позволяет добавлять кнопку, поле ввода и виджет QLabel для отображения изображений:
# Добавим модули
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
                             QPushButton, QLineEdit, QHBoxLayout, QFileDialog)
from PyQt5.QtGui import QPixmap, QPainter, QFont
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()

    def initUI(self):
        # Создание виджетов
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(300, 300)
        self.button_load_image = QPushButton("Загрузить изображение", self)
        self.button_load_image.clicked.connect(self.load_image)
        self.input_text = QLineEdit(self)
        self.button_add_text = QPushButton("Добавить текст", self)
        self.button_add_text.clicked.connect(self.add_text)
        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_load_image)
        layout_buttons.addWidget(self.input_text)
        layout_buttons.addWidget(self.button_add_text)
        layout.addLayout(layout_buttons)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение", os.getcwd(),
                                                    "Изображения (*.png *.xpm *.jpg)")
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(300, 300))

    def add_text(self):
        text = self.input_text.text()
        if text:
            pixmap = self.image_label.pixmap()
            painter = QPainter(pixmap)
            painter.setFont(QFont("Arial", 20))
            painter.drawText(pixmap.rect(), Qt.AlignCenter, text)
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    my_win = MainWindow()
    my_win.show()
    app.exec()


