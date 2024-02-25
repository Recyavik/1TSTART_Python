from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QFont, QKeySequence
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,
                             QLineEdit, QComboBox, QHBoxLayout, QFileDialog, QSizePolicy, QAction)
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Моё приложение')
        self.setGeometry(100, 100, 500, 400)
        self.initUI()

    def initUI(self):
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(300, 300)
        self.button_load_image = QPushButton("Загрузить изображение", self)
        self.button_load_image.clicked.connect(self.load_image)
        self.input_text = QLineEdit(self)
        self.combo_box_position = QComboBox()
        self.combo_box_position.addItem('Верхний левый угол')
        self.combo_box_position.addItem('Верхний правый угол')
        self.combo_box_position.addItem('Нижний левый угол')
        self.combo_box_position.addItem('Нижний правый угол')
        self.combo_box_position.addItem('По центру')
        self.button_add_text = QPushButton("Добавить текст", self)
        self.button_add_text.setVisible(False)
        self.button_add_text.clicked.connect(self.add_text)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout_button = QHBoxLayout()
        layout_button.addWidget(self.button_load_image)
        layout_button.addWidget(self.input_text)
        layout_button.addWidget(self.combo_box_position)
        layout_button.addWidget(self.button_add_text)

        layout.addLayout(layout_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
                    QMainWindow {
                        background-color: #F0F0F0;
                    }
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border: 2px;
                        padding: 10px 20px;
                        font-size: 16px;
                    }
                    QLineEdit {
                        border: 2px solid #4CAF50;
                        border-radius: 5px;
                        padding: 5px;
                        font-size: 16px;
                    }
                """)

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, 'Выбрать изображение', os.getcwd(),
                                                    "Изображения (*.png *.jpg *.xpm)")
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(300, 300))
        self.button_add_text.setVisible(True)

    def add_text(self):
        text = self.input_text.text()
        position = self.combo_box_position.currentText()
        if text:
            pixmap = self.image_label.pixmap()
            painter = QPainter(pixmap)
            font = QFont('Arial', 20)
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

            painter.setFont(font)
            painter.drawText(rect, align_flag, text)
            painter.end()
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    my_win = MainWindow()
    my_win.show()
    app.exec()

