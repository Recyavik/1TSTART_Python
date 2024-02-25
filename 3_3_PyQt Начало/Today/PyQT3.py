# Напишите пользовательское приложение «Дорожные знаки», в окне которого размещены метки
# и поля для ввода данных дорожных знаков: изображение дорожного знака,
# назначение знака и тип этого знака.  Разместите на форме кнопку проверки формы
# на полноту заполнения всей формы. Обеспечьте полное заполнение формы пользователем
# с загрузкой изображений через диалоговое окно загрузки файлов.
# Для ознакомления с дорожными знаками можете использовать обучающие страницы сайта:
# https://www.drom.ru/pdd/pdd/signs/


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton,
                             QLineEdit, QComboBox, QHBoxLayout, QFileDialog, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Дорожные знаки")
        self.setGeometry(600, 400, 500, 300)
        self.initUI()

    def initUI(self):
        # Создание виджетов
        self.lb_image = QLabel(self)
        self.lb_image.setFixedSize(150, 150)
        self.bt_load_image = QPushButton("Загрузить дорожный знак", self)
        self.bt_load_image.clicked.connect(self.load_image)
        self.input_text = QLineEdit(self)
        self.cb_type = QComboBox(self)
        self.cb_type.addItem("Предупреждающие знаки")
        self.cb_type.addItem("Знаки приоритета")
        self.cb_type.addItem("Запрещающие знаки")
        self.cb_type.addItem("Предписывающие знаки")
        self.cb_type.addItem("Знаки особых предписаний")
        self.cb_type.addItem("Информационные знаки")
        self.cb_type.addItem("Знаки дополнительной информации (таблички)")
        self.bt_check_form = QPushButton("Проверить форму", self)
        self.bt_check_form.clicked.connect(self.check_form)
        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.lb_image)
        layout.addWidget(self.input_text)
        layout.addWidget(self.cb_type)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.bt_load_image)
        layout_buttons.addWidget(self.bt_check_form)
        layout.addLayout(layout_buttons)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Добавим подсказки
        self.bt_load_image.setToolTip("Загрузить изображение дорожного знака")
        self.bt_check_form.setToolTip("Проверить полноту заполнения")

        # Применение стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #87CEEB;
            }
            QPushButton {
                background-color: #556B2F;
                color: white;
                border: 2px;
                padding: 10px 20px;
                font-size: 18px;
            }
            QLineEdit {
                 color: black;
                 border: 2px solid #4CAF50;
                 border-radius: 5px;
                 font-size: 18px;
                }
            QLabel {
                 color: black;
                 border: 2px solid #4CAF50;
                 font-size: 18px;
                }
            QComboBox {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
                font-size: 18px;
            }
        """)
    def load_image(self):
        # Загрузка изображения
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение знака", "", "Изображения (*.png *.xpm *.jpg *.svg)")
        pixmap = QPixmap(image_path)
        self.lb_image.setPixmap(pixmap.scaled(self.lb_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def check_form(self):
        # Получение введенного текста и выбранной позиции
        text = self.input_text.text()
        type_label = self.cb_type.currentText()
        self.msg_box = QMessageBox()
        if text != "" and type_label != "" and self.lb_image.pixmap() is not None:
            icon = QMessageBox.Icon.Information
            title = 'Поздравляю!'
            message = 'Форма заполнена полностью!'
        else:
            icon = QMessageBox.Icon.Warning
            title = 'Ошибка!'
            message = "Проверьте заполнение формы!"

        self.msg_box.setText(message)
        self.msg_box.setWindowTitle(title)
        self.msg_box.setIcon(icon)
        self.msg_box.exec()



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
