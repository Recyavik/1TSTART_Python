from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QPushButton, QLineEdit,
                             QComboBox, QHBoxLayout,QAction, QColorDialog)
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Цветовая схема")
        self.setGeometry(400, 200, 200, 200)
        self.initUI()

    def initUI(self):
        self.style_color = "#808080"
        self.text_color = "#000000"
        self.font = "Arial"
        self.font_size = "14"
        color_schema = ("color: " + str(self.text_color) + "; "
                        + "background-color: " + str(self.style_color) + "; "
                        "font: " + self.font + ";" + " font-size: " + self.font_size + "px;")
        # Создание виджетов
        self.button_bk_color = QPushButton(self)
        self.button_bk_color.setText("Цвет виджетов")
        self.button_bk_color.clicked.connect(self.bk_color_choose)
        self.button_bk_color.setToolTip("Выбрать цвет виджетов")
        self.button_bk_color.setObjectName("obj_button_backcolor")
        self.button_bk_color.setStyleSheet(color_schema)

        self.button_textcolor = QPushButton(self)
        self.button_textcolor.setText("Цвет текста")
        self.button_textcolor.clicked.connect(self.color_choose)
        self.button_textcolor.setToolTip("Выбрать цвет шрифта")
        self.button_textcolor.setObjectName("obj_button_textcolor")
        self.button_textcolor.setStyleSheet(color_schema)


        self.lbl_size_font = QLabel("Размер шрифта:", self)
        self.input_size_font = QLineEdit(self)
        self.input_size_font.setText(self.font_size)
        self.input_size_font.textChanged.connect(self.change_color_schema)
        self.input_size_font.setAlignment(Qt.AlignLeft)
        self.input_size_font.setToolTip("Укажите размер шрифта")
        self.input_size_font.setObjectName("obj_input_size_font")
        self.input_size_font.setStyleSheet(color_schema)

        pIntvalidator = QIntValidator(self)
        pIntvalidator.setRange(14, 32)
        self.input_size_font.setValidator(pIntvalidator)
        self.input_size_font.textChanged.connect(self.update)


        self.combo_box_font = QComboBox(self)
        self.combo_box_font.addItem("Arial")
        self.combo_box_font.addItem("Impact")
        self.combo_box_font.addItem("Comic Sans MS")
        self.combo_box_font.setToolTip("Шрифт")
        self.combo_box_font.setObjectName("obj_combo_box_font")
        self.combo_box_font.setStyleSheet(color_schema)
        self.combo_box_font.currentTextChanged.connect(self.change_color_schema)

        # Размещение виджетов с помощью менеджера компоновки
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.button_bk_color)
        layout_main.addWidget(self.button_textcolor)
        layout_input = QHBoxLayout()
        layout_input.addWidget(self.lbl_size_font)
        layout_input.addWidget(self.input_size_font)
        layout_main.addLayout(layout_input)

        layout_main.addWidget(self.combo_box_font)

        central_widget = QWidget()
        central_widget.setLayout(layout_main)
        self.setCentralWidget(central_widget)

        # Создание действий (actions) для клавиатурных сокращений
        self.bk_color_action = QAction("Цвет виджетов", self)
        self.bk_color_action.triggered.connect(self.bk_color_choose)

        self.color_action = QAction("Цвет шрифта", self)
        self.color_action.triggered.connect(self.color_choose)

                # Добавление действий в главное меню
        bk_color_menu = self.menuBar().addMenu("Цвет виджетов")
        bk_color_menu.addAction(self.bk_color_action)

        color_menu = self.menuBar().addMenu("Цвет шрифта")
        color_menu.addAction(self.color_action)

        # Применение стилей
    def bk_color_choose(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.style_color = color.name()
            self.change_color_schema()

    def color_choose(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_color = color.name()
            self.change_color_schema()

    def change_color_schema(self):
        self.font = str(self.combo_box_font.currentText())
        if len(self.input_size_font.text()) >= 2:
            self.font_size = str(self.input_size_font.text())
        color_schema =  ("color: " + str(self.text_color) + "; " + "background-color: " + str(self.style_color) + ";")
        # print(color_schema)

        self.button_textcolor.setStyleSheet(color_schema)
        self.button_bk_color.setStyleSheet(color_schema)
        self.input_size_font.setStyleSheet(color_schema)
        self.input_size_font.setStyleSheet(color_schema)
        self.combo_box_font.setStyleSheet(color_schema)

        self.button_textcolor.setFont(QFont(self.font, int(self.font_size)))
        self.button_bk_color.setFont(QFont(self.font, int(self.font_size)))
        self.input_size_font.setFont(QFont(self.font, int(self.font_size)))
        self.input_size_font.setFont(QFont(self.font, int(self.font_size)))
        self.combo_box_font.setFont(QFont(self.font, int(self.font_size)))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()