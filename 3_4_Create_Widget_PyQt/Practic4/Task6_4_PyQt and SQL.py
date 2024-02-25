import sqlite3
import sys
import os

from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QFileDialog, QLabel, QHBoxLayout, QLineEdit, QMessageBox, QRadioButton,
                             QCalendarWidget, QSlider, QDialog, QTableWidget, QTableWidgetItem)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QBuffer, QByteArray, QDate, QIODeviceBase, Qt, QSize
from PyQt6.uic import loadUi


def convert_date_year_month_day(string_date):
    # string_date format YYYY-MM-DD
    year = string_date[0:4]
    month = string_date[5:7]
    day = string_date[8:10]
    return year, month, day


def age_calculator(y, m, d):
    today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
    today_year, today_month, today_day = convert_date_year_month_day(today)
    age = 0
    if int(y) >= int(today_year):
        age = 0
    elif int(y) < int(today_year):
        age = int(today_year) - int(y)
        if int(m) > int(today_month):
            age -= 1
        elif int(m) == int(today_month):
            if int(d) > int(today_day):
                age -= 1
    return age

def message_form(msg, title, icon):
    msg_box = QMessageBox()
    msg_box.setText(msg)
    msg_box.setWindowTitle(title)
    msg_box.setIcon(icon)
    msg_box.exec()


def convert_pixmap_to_byte_array(pixmap):
    byte_array = QByteArray()
    buff = QBuffer(byte_array)
    buff.open(QIODeviceBase.OpenModeFlag.WriteOnly)
    # PNG - формат по умолчанию, можете изменить на JPEG или другой
    pixmap.save(buff, "PNG")
    pixmap_bytes = byte_array.data()
    # Получаем данные для записи в SQLite
    return pixmap_bytes


def convert_byte_array_to_pixmap(blob):
    img = QtGui.QImage.fromData(blob)
    pixmap = QtGui.QPixmap.fromImage(img)
    return pixmap

class GridDB(QMainWindow):
    def __init__(self):
        super(GridDB, self).__init__()
        self.setMinimumSize(QSize(480, 80))
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(["Имя", "Возраст", "Город"])
        self.table.setItem(0, 0, QTableWidgetItem("Алиса"))
        self.table.setItem(0, 1, QTableWidgetItem("25"))
        self.table.setItem(0, 2, QTableWidgetItem("Лондон"))
        self.table.setItem(1, 0, QTableWidgetItem("Боб"))
        self.table.setItem(1, 1, QTableWidgetItem("30"))
        self.table.setItem(1, 2, QTableWidgetItem("Нью-Йорк"))
        self.setCentralWidget(self.table)

    def load_data_sql(self):
        self.conn = sqlite3.connect("persons.db")
        cur = self.conn.cursor()
        sqlquery = 'SELECT * FROM'

    def create_table(self):

    # Создание таблицy треков
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    language TEXT,
                    time REAL
                    )''')

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.conn = None
        self.pixmap = None
        self.layout_button_db = None
        self.layout_quest = None
        self.layout_photo_and_calendar = None
        self.lbl_age = None
        self.lbl_info_birthday = None
        self.rd_women = None
        self.rd_man = None
        self.input_post = None
        self.input_email = None
        self.input_name = None
        self.lbl_image_photo = None
        self.slider_scale = None
        self.layout_main = None
        self.calendar_date_birthday = None
        self.layout_widget_button = None
        self.image_path = ""
        self.gender = ""
        self.birthday = ""
        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setGeometry(300, 50, 600, 400)
        self.setWindowTitle("Анкета профиля")
        self.setWindowIcon(QIcon("../kandi.ico"))

        self.widgets_top_button()
        self.widgets_center_quest()
        self.widgets_bottom_button()

        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(self.layout_widget_button)
        self.layout_main.addLayout(self.layout_photo_and_calendar)
        self.layout_main.addLayout(self.layout_quest)
        self.layout_main.addLayout(self.layout_button_db)

        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)

        self.style_form()

    def widgets_top_button(self):
        btn_load_photo = QPushButton("Загрузить фото 200 * 200 px")
        btn_load_photo.clicked.connect(self.load_photo)

        btn_view_quest = QPushButton("Показать данные")
        btn_view_quest.clicked.connect(self.view)

        btn_clear_form = QPushButton("Очистить анкету")
        btn_clear_form.clicked.connect(self.clear_form)

        self.layout_widget_button = QHBoxLayout()
        self.layout_widget_button.addWidget(btn_view_quest)
        self.layout_widget_button.addWidget(btn_clear_form)
        self.layout_widget_button.addWidget(btn_load_photo)
        self.layout_widget_button.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def widgets_center_quest(self):
        self.calendar_date_birthday = QCalendarWidget()
        self.calendar_date_birthday.setGeometry(10, 10, 260, 200)
        self.calendar_date_birthday.setFixedSize(260, 200)
        today_date = QDate.currentDate()
        self.birthday = today_date.toString(Qt.DateFormat.ISODate)
        self.calendar_date_birthday.setSelectedDate(today_date)
        self.calendar_date_birthday.selectionChanged.connect(self.update_birthday)

        self.slider_scale = QSlider(Qt.Orientation.Vertical, self)
        self.slider_scale.setRange(10, 200)
        self.slider_scale.setPageStep(10)
        self.slider_scale.setValue(100)
        self.slider_scale.setTickPosition(QSlider.TickPosition.TicksRight)
        self.slider_scale.valueChanged.connect(self.update_scale)

        self.lbl_image_photo = QLabel(self)
        self.lbl_image_photo.setFixedSize(250, 250)

        lbl_name = QLabel("Введите имя:", self)
        self.input_name = QLineEdit(self)
        lbl_email = QLabel("Введите почту:", self)
        self.input_email = QLineEdit(self)
        lbl_post = QLabel("Введите должность:", self)
        self.input_post = QLineEdit(self)

        self.rd_man = QRadioButton("Мужчина", self)
        self.rd_women = QRadioButton("Женщина", self)
        self.rd_man.toggled.connect(self.update_gender)
        self.rd_women.toggled.connect(self.update_gender)

        self.lbl_info_birthday = QLabel("Дата рождения:        ", self)
        self.lbl_age = QLabel("Возраст:   ", self)

        self.layout_photo_and_calendar = QHBoxLayout()
        self.layout_photo_and_calendar.addWidget(self.calendar_date_birthday)
        self.layout_photo_and_calendar.addWidget(self.slider_scale)
        self.layout_photo_and_calendar.addWidget(self.lbl_image_photo)
        self.layout_photo_and_calendar.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout_quest = QVBoxLayout()
        self.layout_quest.addWidget(lbl_name)
        self.layout_quest.addWidget(self.input_name)
        self.layout_quest.addWidget(self.lbl_info_birthday)
        self.layout_quest.addWidget(self.lbl_age)
        self.layout_quest.addWidget(lbl_post)
        self.layout_quest.addWidget(self.input_post)
        self.layout_quest.addWidget(self.rd_man)
        self.layout_quest.addWidget(self.rd_women)
        self.layout_quest.addWidget(lbl_email)
        self.layout_quest.addWidget(self.input_email)

        self.layout_quest.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def widgets_bottom_button(self):
        btn_add_person_db = QPushButton("Добавить в БД")
        btn_add_person_db.clicked.connect(self.add_person_db)

        btn_del_person_db = QPushButton("Удалить из БД")
        btn_del_person_db.clicked.connect(self.del_person_db)

        btn_find_person_db = QPushButton("Найти в БД")
        btn_find_person_db.clicked.connect(self.find_person_db)

        btn_update_person_db = QPushButton("Редактировать")
        btn_update_person_db.clicked.connect(self.update_person_db)

        self.layout_button_db = QHBoxLayout()
        self.layout_button_db.addWidget(btn_add_person_db)
        self.layout_button_db.addWidget(btn_del_person_db)
        self.layout_button_db.addWidget(btn_find_person_db)
        self.layout_button_db.addWidget(btn_update_person_db)

    def style_form(self):
        # Стиль
        self.setStyleSheet("""
                       QMainWindow {
                           background-color: #faebb2;
                       }
                       QLabel{
                           color: black;
                           font-size: 16px;
                       }
                        QRadioButton{
                           color: black;
                           font-size: 16px;
                       }
                       QPushButton {
                           background-color: #06786f;
                           color: white;
                           border: none;
                           padding: 10px 20px;
                           font-size: 16px;
                       }
                       QLineEdit {
                           border: 2px solid #06786f;
                           border-radius: 5px;
                           padding: 5px;
                           font-size: 16px;
                       }
                   """)

    def load_photo(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Выбрать изображение", os.getcwd(),
                                                    "Изображения (*.png *.xpm *.jpg)")

        self.pixmap = QPixmap(image_path)
        self.layout_photo_and_calendar.addWidget(self.lbl_image_photo)
        self.lbl_image_photo.setPixmap(self.pixmap)
        self.slider_scale.setValue(100)
        self.get_scale()

    def resize_pixmap(self, pixmap, scale):
        width = int(self.pixmap.width() / scale)
        height = int(self.pixmap.height() / scale)
        self.lbl_image_photo.setPixmap(pixmap.scaled(width, height))
        self.lbl_image_photo.setFixedSize(width, height)

    def update_scale(self):
        self.get_scale()

    def get_scale(self):
        if self.lbl_image_photo.pixmap().isNull():
            scale = 1
            self.slider_scale.setValue(100)
        else:
            scale = 100 / self.slider_scale.value()
            width = int(self.pixmap.width() / scale)
            height = int(self.pixmap.height() / scale)
            if (40 <= width <= 250) or (40 <= height <= 250):
                self.resize_pixmap(self.pixmap, scale)
            elif width > 250 or height > 250:
                scale = 100 / self.slider_scale.value()
                self.slider_scale.setValue(self.slider_scale.value())
                self.pixmap = self.pixmap.scaled(250, 250)
                self.lbl_image_photo.setPixmap(self.pixmap)
        return scale

    def check_quest(self):
        result = True
        if self.input_name.text() == "" or self.input_post.text() == "" or self.input_email.text() == "" \
                or self.gender == "" or self.birthday == "" or self.lbl_image_photo.pixmap().isNull():
            result = False
        return result

    def view(self):
        self.view_quest("Анкета")

    def view_quest(self, title):
        msg_box = QMessageBox()
        msg = []
        icon = QMessageBox.Icon.Information
        if self.input_name.text() == "":
            msg.append(f"Вы не указали имя")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Имя: " + self.input_name.text())
        if self.input_post.text() == "":
            msg.append(f"Вы не указали должность")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Должность: " + self.input_post.text())
        if self.input_email.text() == "":
            msg.append(f"Вы не указали электронную почту")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Почта: " + self.input_email.text())
        if self.gender == "":
            msg.append(f"Вы не указали пол")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Пол: " + str(self.gender))
        if self.birthday == "":
            msg.append(f"Вы не указали дату рождения")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Дата рождения: " + self.birthday)
        if self.lbl_image_photo.pixmap().isNull():
            msg.append(f"Вы не загрузили фотографию")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Фото успешно загружено: ")
        message = f""
        for m in msg:
            message += f"{m}\n"
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setIcon(icon)
        msg_box.exec()

    def update_gender(self, _):
        rb = self.sender()
        if rb.isChecked():
            self.gender = rb.text()

    def clear_radio_gender(self):
        # Обнуляем Radio
        self.rd_man.setAutoExclusive(False)
        self.rd_women.setAutoExclusive(False)
        self.rd_man.setChecked(False)
        self.rd_women.setChecked(False)
        self.rd_man.repaint()
        self.rd_women.repaint()
        self.rd_man.setAutoExclusive(True)
        self.rd_women.setAutoExclusive(True)

    def update_birthday(self):
        today = QDate.currentDate().toString(Qt.DateFormat.ISODate)
        calendar = self.calendar_date_birthday.selectedDate().toString(Qt.DateFormat.ISODate)
        if (calendar <= today):
            self.birthday = self.calendar_date_birthday.selectedDate().toString(Qt.DateFormat.ISODate)
            year, month, day = convert_date_year_month_day(self.birthday)
            age = age_calculator(int(year), int(month), int(day))
            self.lbl_age.setText(f"Возраст: {age}")
            self.lbl_info_birthday.setText(f"Дата рождения: {day}.{month}.{year}")
        else:
            message_form(f"Не корректное значение даты", "Внимание! Ошибка!!!", QMessageBox.Icon.Warning)

    def clear_form(self):
        self.lbl_age.setText("Возраст:")
        self.image_path = ""
        self.calendar_date_birthday.setSelectedDate(QDate.currentDate())
        self.lbl_info_birthday.setText(f"Дата рождения:")

        self.input_post.setText("")
        self.input_email.setText("")
        self.lbl_image_photo.setPixmap(QPixmap())
        self.input_name.setText("")
        self.gender = ""
        self.birthday = ""
        # Обнуляем Radio
        self.clear_radio_gender()

    def init_db(self):
        self.conn = sqlite3.connect("../library.db")
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS persons (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT,
                        born TEXT,
                        gender TEXT,
                        post TEXT, 
                        email TEXT,
                        photo BLOB)
                        """)
        self.conn.commit()

    def add_person_db(self):
        if self.check_quest():
            cur = self.conn.cursor()
            pixmap = self.lbl_image_photo.pixmap()
            blob_photo = convert_pixmap_to_byte_array(pixmap)
            cur.execute("INSERT INTO persons (name, born, gender, post, email, photo)VALUES(?, ?, ?, ?, ?, ?)",
                        (self.input_name.text(), self.birthday, self.gender, self.input_post.text(),
                         self.input_email.text(), blob_photo))
            self.conn.commit()
            cur.close()
            self.view_quest("Анкета добавлена в БД")
            self.clear_form()
        else:
            self.view_quest("Анкета не заполнена")

    def del_person_db(self):
        index = self.input_email.text()
        if index == "":
            message_form(f"Пустых записей в базе данных нет!", "Удаление невозможно", QMessageBox.Icon.Warning)
        else:
            self.find_person_db()
            cur = self.conn.cursor()
            cur.execute(f"DELETE FROM persons WHERE name = (SELECT name FROM persons WHERE email = '{index}')")
            self.conn.commit()
            cur.close()
            self.view_quest("Удалена анкета")
            self.clear_form()

    def find_person_db(self):
        index = self.input_email.text()
        cur = self.conn.cursor()
        cur.execute(f"SELECT name, born, gender, post, email, photo FROM persons WHERE email = '{index}'")
        result = cur.fetchone()
        if result is not None:
            self.input_name.setText(result[0])
            year, month, day = convert_date_year_month_day(result[1])
            self.calendar_date_birthday.setSelectedDate(QDate(int(year), int(month), int(day)))
            self.gender = str(result[2])
            self.clear_radio_gender()
            if "Муж" in self.gender:
                self.rd_man.setChecked(True)
            else:
                self.rd_women.setChecked(True)
            self.input_post.setText(result[3])
            self.input_email.setText(result[4])

            self.pixmap = (convert_byte_array_to_pixmap(result[5]))
            self.lbl_image_photo.setPixmap(self.pixmap)

            self.view_quest("Анкета найдена в базе")
            scale = 100
            self.slider_scale.setValue(scale)
            self.get_scale()
        else:
            message_form(f"Анкета с email: {self.input_email.text()} не найдена в базе данных",
                         "Анкета не найдена", QMessageBox.Icon.Warning)
            self.clear_form()
        cur.close()

    def update_person_db(self):
        if self.check_quest():
            pixmap = self.lbl_image_photo.pixmap()
            blob_photo = convert_pixmap_to_byte_array(pixmap)
            cur = self.conn.cursor()
            sql_update = (f"UPDATE persons SET name=?, born=?, gender=?, post=?, email=?, photo=? "
                          f"WHERE email = '{self.input_email.text()}'")

            cur.execute(sql_update, (self.input_name.text(), self.birthday, self.gender, self.input_post.text(),
                                     self.input_email.text(), blob_photo))
            self.conn.commit()
            cur.close()
            self.view_quest("Анкета изменена и записана в БД")
            self.clear_form()

        else:
            message_form(f"Нельзя редактировать пустую запись", "Изменение невозможно", QMessageBox.Icon.Warning)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())