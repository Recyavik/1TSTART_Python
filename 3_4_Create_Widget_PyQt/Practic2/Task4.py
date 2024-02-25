from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QFont, QKeySequence
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,
                             QLineEdit, QComboBox, QHBoxLayout, QFileDialog, QSizePolicy, QAction)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()

    def initUI(self):
        # Создание виджетов
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_load_image = QPushButton("Загрузить изображение", self)
        self.button_load_image.setObjectName("loadButton")
        self.button_load_image.clicked.connect(self.load_image)
        self.input_text = QLineEdit(self)
        self.input_text.setObjectName("inputField")
        self.combo_box_position = QComboBox(self)
        self.combo_box_position.setObjectName("positionComboBox")
        self.combo_box_position.addItem("Верхний левый угол")
        self.combo_box_position.addItem("Верхний правый угол")
        self.combo_box_position.addItem("Нижний левый угол")
        self.combo_box_position.addItem("Нижний правый угол")
        self.combo_box_position.addItem("По центру")
        self.button_add_text = QPushButton("Добавить текст", self)
        self.button_add_text.setVisible(False)
        self.button_add_text.setObjectName("addTextButton")
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

        # Добавим подсказки
        self.button_load_image.setToolTip("Загрузить изображение")
        self.button_add_text.setToolTip("Добавить текст")

        # Здесь мы создаем действие (QAction) для загрузки изображения
        # с текстом "Загрузить изображение".
        # Мы подключаем событие triggered к функции load_image,
        # которая будет вызываться при выборе этого действия.
        # Мы также задаем клавиатурное сокращение с помощью setShortcut для выполнения
        # действия при нажатии определенной комбинации клавиш.
        self.load_action = QAction("Загрузить изображение", self)
        self.load_action.triggered.connect(self.load_image)
        self.load_action.setShortcut(QKeySequence.Open)

        self.add_text_action = QAction("Добавить текст", self)
        self.add_text_action.triggered.connect(self.add_text)
        self.add_text_action.setShortcut(QKeySequence(Qt.Key_Return))

        # Аналогично, мы создаем действие для добавления текста с текстом "Добавить текст".
        # Мы подключаем событие triggered к функции add_text,
        # которая будет вызываться при выборе этого действия.
        # Мы также задаем клавиатурное сокращение с помощью setShortcut для выполнения
        # действия при нажатии определенной комбинации клавиш.


        # Применение стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QPushButton#loadButton,
            QPushButton#addTextButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }
            QLineEdit#inputField {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }
        """)
    def load_image(self):
        # Загрузка изображения
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение", "", "Изображения (*.png *.xpm *.jpg)")
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.button_add_text.setVisible(True)

    def add_text(self):
        # Получение введенного текста и выбранной позиции
        text = self.input_text.text()
        position = self.combo_box_position.currentText()
        if text:
            # Получение текущего изображения
            pixmap = self.image_label.pixmap()
            # Настройка шрифта и позиции в зависимости от выбранной позиции
            font = QFont("Arial", 20)
            rect = QRect(0, 0, pixmap.width(), pixmap.height())
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
            # Создание QPainter для рисования текста на изображении
            painter = QPainter(pixmap)
            painter.setFont(font)
            painter.drawText(rect, align_flag, text)
            painter.end()
            # Отображение обновленного изображения
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
