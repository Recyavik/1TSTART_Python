from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,
                             QPushButton, QLineEdit, QHBoxLayout, QComboBox, QFileDialog)
from PyQt5.QtGui import QPainter, QFont
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
        self.combo_box_position = QComboBox(self)
        self.combo_box_position.addItem("Верхний левый угол")
        self.combo_box_position.addItem("Верхний правый угол")
        self.combo_box_position.addItem("Нижний левый угол")
        self.combo_box_position.addItem("Нижний правый угол")
        self.combo_box_position.addItem("По центру")
        self.button_add_text = QPushButton("Добавить текст", self)
        self.button_add_text.setVisible(False)
        self.button_add_text.clicked.connect(self.add_text)
        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_load_image)
        layout_buttons.addWidget(self.input_text)
        layout_buttons.addWidget(self.combo_box_position)
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
        self.button_add_text.setVisible(True)


    def add_text(self):
        # Получение введенного текста и выбранной позиции
        text = self.input_text.text()
        position = self.combo_box_position.currentText()
        if text:
            # Получение текущего изображения и создание QPainter для рисования текста
            pixmap = self.image_label.pixmap()
            painter = QPainter(pixmap)
            # Настройка шрифта и позиции в зависимости от выбранной позиции
            font = QFont("Arial", 20)
            rect = pixmap.rect()
            if position == "Верхний левый угол":
                align_flag = Qt.AlignTop | Qt.AlignLeft
            elif position == "Верхний правый угол":
                align_flag = Qt.AlignTop | Qt.AlignRight
            elif position == "Нижний левый угол":
                align_flag = Qt.AlignBottom | Qt.AlignLeft
            elif position == "Нижний правый угол":
                align_flag = Qt.AlignBottom | Qt.AlignRight
            else:
                align_flag = Qt.AlignCenter
                # Рисование текста на изображении
            painter.setFont(font)
            painter.drawText(rect, align_flag, text)
            painter.end()
            # Отображение обновленного изображения
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    my_win = MainWindow()
    my_win.show()
    app.exec()