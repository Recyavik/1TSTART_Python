import sqlite3
import sys
import os
from PyQt6 import QtWidgets
from modules import *
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QFileDialog, QLabel, QHBoxLayout, QLineEdit, QMessageBox, QRadioButton,
                             QCalendarWidget, QSlider)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QDate, Qt
from PyQt6 import uic

# pyuic6.exe -x table.ui -o table.py
# Form, Window = uic.loadUiType('table.ui')


class Abonents(QMainWindow):
    subscriber = ''
    def __init__(self):
        super(Abonents, self).__init__()
        self.image_path = ""
        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setGeometry(300, 50, 600, 400)
        self.setWindowTitle("Анкета абонента")
        self.setWindowIcon(QIcon("kandi.ico"))

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
        btn_load_photo = QPushButton(QIcon('Resources/photo.png'), "Загрузить фото", self)
        btn_load_photo.clicked.connect(self.load_photo)
        btn_load_photo.setToolTip('Загрузить фотографию абонента')


        btn_view_quest = QPushButton(QIcon('Resources/check.png'), "Проверить", self)
        btn_view_quest.clicked.connect(self.view)
        btn_view_quest.setToolTip('Проверить заполнение анкетных данных')

        btn_new_form = QPushButton(QIcon('Resources/new.png'), "Новый абонент", self)
        btn_new_form.clicked.connect(self.new_form)
        btn_new_form.setToolTip('Добавить нового абонента или читателя')


        btn_resource = QPushButton(QIcon('Resources/book.png'), "Выдать ресурс", self)
        btn_resource.clicked.connect(issue_resource)
        btn_resource.setToolTip('Выдать этому абоненту книгу')

        self.layout_widget_button = QHBoxLayout()
        self.layout_widget_button.addWidget(btn_new_form)
        self.layout_widget_button.addWidget(btn_view_quest)
        self.layout_widget_button.addWidget(btn_load_photo)
        self.layout_widget_button.addWidget(btn_resource)
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

        lbl_number_subscribers = QLabel("Введите № абонента:", self)
        self.subscribers_number = QLineEdit(self)

        lbl_name = QLabel("Введите имя:", self)
        self.input_name = QLineEdit(self)

        lbl_email = QLabel("Введите почту:", self)
        self.input_email = QLineEdit(self)


        self.rd_man = QRadioButton("Муж", self)
        self.rd_women = QRadioButton("Жен", self)
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
        self.layout_quest.addWidget(lbl_number_subscribers)
        self.layout_quest.addWidget(self.subscribers_number)
        self.layout_quest.addWidget(lbl_name)
        self.layout_quest.addWidget(self.input_name)
        self.layout_quest.addWidget(self.lbl_info_birthday)
        self.layout_quest.addWidget(self.lbl_age)

        self.layout_quest.addWidget(self.rd_man)
        self.layout_quest.addWidget(self.rd_women)
        self.layout_quest.addWidget(lbl_email)
        self.layout_quest.addWidget(self.input_email)

        self.layout_quest.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def widgets_bottom_button(self):
        btn_add_person_db = QPushButton(QIcon('Resources/add.png'), "Добавить", self)
        btn_add_person_db.clicked.connect(self.add_person_db)
        btn_add_person_db.setToolTip('Добавить абонента в базу данных')


        btn_del_person_db = QPushButton(QIcon('Resources/del.png'), "Удалить", self)
        btn_del_person_db.clicked.connect(self.del_person_db)
        btn_del_person_db.setToolTip('Удалить абонента из базы данных')

        btn_find_person_db = QPushButton(QIcon('Resources/find.png'), "Найти", self)
        btn_find_person_db.clicked.connect(self.find_person_db)
        btn_find_person_db.setToolTip('Найти абонента в базе данных')

        btn_update_person_db = QPushButton(QIcon('Resources/edit.png'), "Редактировать", self)
        btn_update_person_db.clicked.connect(self.update_person_db)
        btn_update_person_db.setToolTip('Изменить данные абонента и записать в базу')

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
                           font-size: 14px;
                       }
                        QRadioButton{
                           color: black;
                           font-size: 14px;
                       }
                       QPushButton {
                           background-color: #06786f;
                           color: white;
                           border-radius: 5px;
                           border: white;
                           padding: 5px 5px;
                           font-size: 14px;
                       }
                       QLineEdit {
                           border: 2px solid #06786f;
                           border-radius: 5px;
                           padding: 2px;
                           font-size: 14px;
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
        if self.input_name.text() == "" or self.subscribers_number.text() == "" or self.input_email.text() == "" \
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
        if self.subscribers_number.text() == "":
            msg.append(f"Вы не указали № абонента")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Абонент №: " + self.subscribers_number.text())
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

        self.subscribers_number.setText("")
        self.input_email.setText("")
        self.lbl_image_photo.setPixmap(QPixmap())
        self.input_name.setText("")
        self.gender = ""
        self.birthday = ""
        # Обнуляем Radio
        self.clear_radio_gender()

    def new_form(self):
        self.clear_form()
        self.conn = sqlite3.connect("library.db")
        cur = self.conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM persons")
        result = cur.fetchone()
        self.lbl_age.setText("Возраст:")
        self.image_path = ""
        self.calendar_date_birthday.setSelectedDate(QDate.currentDate())
        self.lbl_info_birthday.setText(f"Дата рождения:")

        self.subscribers_number.setText(str(result[0]+1))
        self.input_email.setText("")
        self.lbl_image_photo.setPixmap(QPixmap())
        self.input_name.setText("")
        self.gender = ""
        self.birthday = ""
        # Обнуляем Radio
        self.clear_radio_gender()
        cur.close()

    def init_db(self):
        self.conn = sqlite3.connect("library.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS persons (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT,
                        born TEXT,
                        gender TEXT,
                        number TEXT, 
                        email TEXT,
                        photo BLOB)
                        """)

        self.conn.commit()
        self.conn.close()

    def check_is_uniqueness(self) -> bool:
        flag = True
        check = self.subscribers_number.text()
        check2 = self.input_email.text()
        if check == '' or check2 == '' or check2 is None or check is None:
            message_form(f"Не заполнены обязательные поля записи: № абонента и его почта!",
                         "Ошибка!", QMessageBox.Icon.Warning)
        else:
            self.conn = sqlite3.connect("library.db")
            self.cur = self.conn.cursor()
            self.cur.execute(f"SELECT COUNT(*) FROM persons")
            result = self.cur.fetchone()
            if result[0] > 0:
                self.cur.execute(f"SELECT number, email FROM persons WHERE number = {check}  OR email = {check2}")
                result = self.cur.fetchone()
                self.conn.commit()
                self.cur.close()
                if result is not None:
                    flag = False
                    msg = []
                    message = ""
                    if check in result[0]:
                        msg.append('Абонент с таким номером уже существует!')
                    if check2 in result[1]:
                        msg.append('Абонент с такой электронной почтой уже существует!')
                    for m in msg:
                        message += f"{m}\n"
                    if check in result[0] or check2 in result[1]:
                        msg_box = QMessageBox()
                        msg_box.setText(message)
                        msg_box.setWindowTitle('Ошибка уникальности!')
                        msg_box.setIcon(QMessageBox.Icon.Information)
                        msg_box.exec()
        return flag

    def add_person_db(self):
        check = self.check_is_uniqueness()
        if check == False:
            self.view_quest("Анкета ранее уже добавлена в базу")
        if self.check_quest() == False:
            self.view_quest("Анкета не заполнена")
        elif self.check_quest() and check:
            self.conn = sqlite3.connect("library.db")
            self.cur = self.conn.cursor()
            pixmap = self.lbl_image_photo.pixmap()
            blob_photo = convert_pixmap_to_byte_array(pixmap)
            self.cur.execute("INSERT INTO persons (name, born, gender, number, email, photo) "
                             "VALUES(?, ?, ?, ?, ?, ?)",
                        (self.input_name.text(), self.birthday, self.gender,
                         self.subscribers_number.text(), self.input_email.text(), blob_photo))
            self.conn.commit()
            self.cur.close()
            self.view_quest("Анкета добавлена в БД")


    def del_person_db(self):
        index = self.subscribers_number.text()
        if index == "":
            message_form(f"Пустых записей в базе данных нет!", "Удаление невозможно", QMessageBox.Icon.Warning)
        else:
            self.conn = sqlite3.connect("library.db")
            self.find_person_db()
            self.cur = self.conn.cursor()
            self.cur.execute(f"DELETE FROM persons WHERE name = (SELECT name FROM persons WHERE number = '{index}')")
            self.conn.commit()
            self.cur.close()
            self.view_quest("Удалена анкета")
            self.new_form()

    def find_person_db(self):
        index = self.subscribers_number.text()
        self.conn = sqlite3.connect("library.db")
        self.cur = self.conn.cursor()
        self.cur.execute(f"SELECT name, born, gender, number, email, photo FROM persons WHERE number = '{index}'")
        result = self.cur.fetchone()
        self.cur.close()
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
            self.subscribers_number.setText(result[3])
            self.input_email.setText(result[4])

            self.pixmap = (convert_byte_array_to_pixmap(result[5]))
            self.lbl_image_photo.setPixmap(self.pixmap)

            self.view_quest("Анкета найдена в базе")
            scale = 100
            self.slider_scale.setValue(scale)
            self.get_scale()
        else:
            message_form(f"Анкета абонента: {self.subscribers_number.text()} не найдена в базе данных",
                         "Анкета не найдена", QMessageBox.Icon.Warning)
            self.new_form()


    def update_person_db(self):
        if self.check_quest():
            self.conn = sqlite3.connect("library.db")
            pixmap = self.lbl_image_photo.pixmap()
            blob_photo = convert_pixmap_to_byte_array(pixmap)
            self.cur = self.conn.cursor()
            sql_update = (f"UPDATE persons SET name=?, born=?, gender=?, number=?, email=?, photo=? "
                          f"WHERE number = '{self.subscribers_number.text()}'")

            self.cur.execute(sql_update, (self.input_name.text(), self.birthday, self.gender,
                                          self.subscribers_number.text(),
                                     self.input_email.text(), blob_photo))
            self.conn.commit()
            self.cur.close()
            self.view_quest("Анкета изменена и записана в БД")
            self.new_form()
        elif self.check_quest() == False:
            message_form(f"Нельзя редактировать запись c пустыми полями", "Изменение невозможно",
                         QMessageBox.Icon.Warning)

from Books import *

def issue_resource(self):
    global subscriber
    subscriber = self.input_name.text()
    if self.win is None:
        self.win = AddBook()
        self.win.show()
    else:
        self.win.close()
        self.win = None
        self.issue_resource()
