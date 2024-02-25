from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QPushButton, QLineEdit,
                             QComboBox, QHBoxLayout, QFileDialog, QAction,
                             QColorDialog, QSizePolicy)
from PyQt5.QtGui import QPixmap, QPainter, QFont, QKeySequence, QColor
from PyQt5.QtCore import Qt, QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мое приложение")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()
        self.undo_stack = []
        self.text_color = Qt.black

    def initUI(self):
        # Создание виджетов
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_label.setToolTip("Изображение")
        self.button_load_image = QPushButton("Загрузить изображение", self)
        self.button_load_image.clicked.connect(self.load_image)
        self.button_load_image.setToolTip("Загрузить изображение")
        self.input_text = QLineEdit(self)
        self.input_text.setFixedSize(150,40)
        self.input_text.setToolTip("Текст")
        self.combo_box_position = QComboBox(self)
        self.combo_box_position.addItem("Верхний левый угол")
        self.combo_box_position.addItem("Верхний правый угол")
        self.combo_box_position.addItem("Нижний левый угол")
        self.combo_box_position.addItem("Нижний правый угол")
        self.combo_box_position.addItem("По центру")
        self.combo_box_position.setToolTip("Позиция на рисунке")
        self.combo_box_font = QComboBox(self)
        self.combo_box_font.addItem("Arial")
        self.combo_box_font.addItem("Times New Roman")
        self.combo_box_font.addItem("Courier New")
        self.combo_box_font.setToolTip("Шрифт")
        self.button_text_color = QPushButton("Выбрать цвет", self)
        self.button_text_color.clicked.connect(self.choose_text_color)
        self.button_text_color.setToolTip("Выбрать цвет текста")
        self.button_add_text = QPushButton("Добавить текст", self)
        self.button_add_text.clicked.connect(self.add_text)
        self.button_add_text.setToolTip("Добавить текст")
        self.button_undo = QPushButton("Отменить", self)
        self.button_undo.clicked.connect(self.undo_action)
        self.button_undo.setToolTip("Отменить последнее действие")
        self.button_save_image = QPushButton("Сохранить изображение", self)
        self.button_save_image.clicked.connect(self.save_image)
        self.button_save_image.setToolTip("Сохранить изображение")
        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_load_image)
        layout_buttons.addWidget(self.input_text)
        layout_buttons.addWidget(self.combo_box_position)
        layout_buttons.addWidget(self.combo_box_font)
        layout_buttons.addWidget(self.button_text_color)
        layout_buttons.addWidget(self.button_add_text)
        layout_buttons.addWidget(self.button_undo)
        layout_buttons.addWidget(self.button_save_image)
        layout.addLayout(layout_buttons)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # Создание действий (actions) для клавиатурных сокращений
        self.load_action = QAction("Загрузить изображение", self)
        self.load_action.triggered.connect(self.load_image)
        self.load_action.setShortcut(QKeySequence.Open)
        self.add_text_action = QAction("Добавить текст", self)
        self.add_text_action.triggered.connect(self.add_text)
        self.add_text_action.setShortcut(QKeySequence(Qt.Key_Return))
        # Добавление действий в главное меню
        file_menu = self.menuBar().addMenu("Файл")
        file_menu.addAction(self.load_action)
        edit_menu = self.menuBar().addMenu("Правка")
        edit_menu.addAction(self.add_text_action)
        # Применение стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
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
        # Загрузка изображения
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение",
                                            "", "Изображения (*.png *.xpm *.jpg)")
        if image_path:
            try:
                pixmap = QPixmap(image_path)
                if pixmap.isNull():
                    raise Exception("Ошибка загрузки изображения")
                self.image_label.setPixmap(
                    pixmap.scaled(self.image_label.size(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))
                # Добавление пиксмапа в стек отмены действий
                self.undo_stack.append(pixmap)
            except Exception as e:
                print("Ошибка загрузки изображения:", str(e))

    def add_text(self):
        # Получение введенного текста и выбранных параметров
        text = self.input_text.text()
        position = self.combo_box_position.currentText()
        font_family = self.combo_box_font.currentText()
        if text:
            # Получение текущего изображения
            pixmap = self.image_label.pixmap()
            # Настройка шрифта и позиции в зависимости от выбранной позиции
            font = QFont(font_family, 20)
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
            # Создание нового QPixmap с добавленным текстом
            new_pixmap = pixmap.copy()
            painter = QPainter(new_pixmap)
            painter.setFont(font)
            painter.setPen(self.text_color)
            painter.drawText(rect, align_flag, text)
            painter.end()
            # Замена текущего изображения новым с добавленным текстом
            layout = self.centralWidget().layout()
            layout.replaceWidget(self.image_label, QLabel(self))
            self.image_label.deleteLater()
            self.image_label = layout.itemAt(0).widget()
            self.image_label.setPixmap(new_pixmap)
            # Добавление пиксмапа в стек отмены действий
            self.undo_stack.append(new_pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def undo_action(self):
        if self.undo_stack:
            # Удаление последнего пиксмапа из стека отмены действий
            self.undo_stack.pop()
            if self.undo_stack:
                # Получение предыдущего пиксмапа из стека
                pixmap = self.undo_stack[-1]
                self.image_label.setPixmap(
                    pixmap.scaled(self.image_label.size(),
                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                # Если стек пуст, очистить метку изображения
                self.image_label.clear()

    def choose_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_color = color

    def save_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Сохранить изображение",
                                            "", "Изображения (*.png *.xpm *.jpg)")
        if file_path:
            pixmap = self.image_label.pixmap()
            if pixmap is not None:
                pixmap.save(file_path)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()