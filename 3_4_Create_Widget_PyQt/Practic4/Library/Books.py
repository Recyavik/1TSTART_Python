import sqlite3
import sys
import os
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from modules import *
from Order_Books import *
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QFileDialog, QLabel, QHBoxLayout, QLineEdit, QMessageBox, QRadioButton,
                             QCalendarWidget, QSlider, QDialog, QTableWidget, QTableWidgetItem, QCheckBox)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QBuffer, QByteArray, QDate, QIODeviceBase, Qt, QSize
from PyQt6 import uic

class AddBook(QMainWindow):
    def __init__(self):
        super(AddBook, self).__init__()

        self.init_ui()
        self.init_db()

    def init_ui(self):
        self.setGeometry(300, 50, 400, 400)
        self.setWindowTitle("Книга в статусе: " + 'Морев Алексей')
        self.setWindowIcon(QIcon("Resources/book.png"))

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
        btn_import = QPushButton(QIcon('Resources/import.png'), "Импорт", self)
        btn_import.clicked.connect(self.import_db)
        btn_import.setToolTip('Импортирование библиотеки из Excell')

        btn_load_photo = QPushButton(QIcon('Resources/photo.png'), "Загрузить обложку", self)
        btn_load_photo.clicked.connect(self.load_photo)
        btn_load_photo.setToolTip('Загрузить обложку книги')

        btn_view_quest = QPushButton(QIcon('Resources/check.png'), "Проверить", self)
        btn_view_quest.clicked.connect(self.view)
        btn_view_quest.setToolTip('Проверить заполнение формы')

        btn_new_form = QPushButton(QIcon('Resources/new.png'), "Новая книга", self)
        btn_new_form.clicked.connect(self.new_form)
        btn_new_form.setToolTip('Поступила новая книга в библиотеку')

        self.layout_widget_button = QHBoxLayout()
        self.layout_widget_button.addWidget(btn_new_form)
        self.layout_widget_button.addWidget(btn_view_quest)
        self.layout_widget_button.addWidget(btn_load_photo)
        self.layout_widget_button.addWidget(btn_import)

        self.layout_widget_button.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def widgets_center_quest(self):
        self.slider_scale = QSlider(Qt.Orientation.Vertical, self)
        self.slider_scale.setRange(10, 200)
        self.slider_scale.setPageStep(10)
        self.slider_scale.setValue(100)
        self.slider_scale.setTickPosition(QSlider.TickPosition.TicksRight)
        self.slider_scale.valueChanged.connect(self.update_scale)

        self.lbl_image_photo = QLabel(self)
        self.lbl_image_photo.setFixedSize(250, 250)

        lbl_article = QLabel("Введите артикул книги:", self)
        self.input_article = QLineEdit(self)

        lbl_name = QLabel("Введите название книги:", self)
        self.input_name = QLineEdit(self)

        lbl_author_book = QLabel("Введите автора книги:", self)
        self.input_author = QLineEdit(self)

        lbl_year_book = QLabel("Введите год издания:", self)
        self.input_year_book = QLineEdit(self)

        self.cb_book_status = QCheckBox("Статус книги:", self)
        self.cb_book_status.setEnabled(False)
        self.cb_book_status.stateChanged.connect(self.check_book_status)
        self.check_status = self.cb_book_status.isChecked()

        self.lbl_number_subscribers = QLabel("Книга у абонента:", self)

        self.layout_photo_and_calendar = QHBoxLayout()
        self.layout_photo_and_calendar.addWidget(self.slider_scale)
        self.layout_photo_and_calendar.addWidget(self.lbl_image_photo)
        self.layout_photo_and_calendar.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout_quest = QVBoxLayout()
        self.layout_quest.addWidget(lbl_article)
        self.layout_quest.addWidget(self.input_article)
        self.layout_quest.addWidget(lbl_name)
        self.layout_quest.addWidget(self.input_name)
        self.layout_quest.addWidget(lbl_author_book)
        self.layout_quest.addWidget(self.input_author)
        self.layout_quest.addWidget(lbl_year_book)
        self.layout_quest.addWidget(self.input_year_book)
        self.layout_quest.addWidget(self.cb_book_status)
        self.layout_quest.addWidget(self.lbl_number_subscribers)

        self.layout_quest.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def widgets_bottom_button(self):
        btn_add_book_db = QPushButton(QIcon('Resources/add.png'), "Добавить", self)
        btn_add_book_db.clicked.connect(self.add_book_db)
        btn_add_book_db.setToolTip('Добавить книгу в библиотеку')

        btn_del_book_db = QPushButton(QIcon('Resources/del.png'), "Удалить", self)
        btn_del_book_db.clicked.connect(self.del_book_db)
        btn_del_book_db.setToolTip('Удалить книгу из библиотеки')

        btn_find_book_db = QPushButton(QIcon('Resources/find.png'), "Найти", self)
        btn_find_book_db.clicked.connect(self.find_book_db)
        btn_find_book_db.setToolTip('Найти книгу в библиотеке')

        btn_edit_book_db = QPushButton(QIcon('Resources/edit.png'), "Редактировать", self)
        btn_edit_book_db.clicked.connect(self.edit_book_db)
        btn_edit_book_db.setToolTip('Изменить карточку книги')

        btn_exit = QPushButton(QIcon('Resources/back.png'), "Закрыть", self)
        btn_exit.clicked.connect(self.exit_form)
        btn_exit.setToolTip('Закрыть форму')

        self.layout_button_db = QHBoxLayout()
        self.layout_button_db.addWidget(btn_add_book_db)
        self.layout_button_db.addWidget(btn_del_book_db)

        self.layout_button_db.addWidget(btn_find_book_db)
        self.layout_button_db.addWidget(btn_edit_book_db)
        self.layout_button_db.addWidget(btn_exit)


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
                       QCheckBox {
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
            if (40 <= width <= 180) or (40 <= height <= 250):
                self.resize_pixmap(self.pixmap, scale)
            elif width > 180 or height > 250:
                scale = 100 / self.slider_scale.value()
                self.slider_scale.setValue(self.slider_scale.value())
                self.pixmap = self.pixmap.scaled(180, 250)
                self.lbl_image_photo.setPixmap(self.pixmap)
        return scale

    def check_quest(self):
        result = True
        if self.input_name.text() == "" or self.input_article.text() == "" or self.input_author.text() == "" \
                or self.input_year_book == "" :
            result = False
        return result

    def view(self):
        self.view_quest("Книга")

    def view_quest(self, title):
        msg_box = QMessageBox()
        msg = []
        icon = QMessageBox.Icon.Information
        if self.input_name.text() == "":
            msg.append(f"Вы не указали название книги")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Название книги: " + self.input_name.text())
        if self.input_article.text() == "":
            msg.append(f"Вы не указали артикул")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Артикул №: " + self.input_article.text())
        if self.input_author.text() == "":
            msg.append(f"Вы не указали автора книги")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Автор: " + self.input_author.text())
        if self.input_year_book.text() == "":
            msg.append(f"Вы не указали год издания книги")
            icon = QMessageBox.Icon.Warning
        else:
            msg.append("Год издания: " + self.input_year_book.text())
        message = f""
        for m in msg:
            message += f"{m}\n"
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setIcon(icon)
        msg_box.exec()


    def clear_form(self):
        self.image_path = ""
        self.input_article.setText("")
        self.input_author.setText("")
        self.input_name.setText("")
        self.cb_book_status.stateChanged(False)

    def new_form(self):
        self.clear_form()
        self.conn = sqlite3.connect("library.db")
        cur = self.conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM persons")
        result = cur.fetchone()
        # self.lbl_age.setText("Возраст:")
        self.image_path = ""
        # self.calendar_date_birthday.setSelectedDate(QDate.currentDate())
        # self.lbl_info_birthday.setText(f"Дата рождения:")

        # self.subscribers_number.setText(str(result[0]+1))
        # self.input_email.setText("")
        self.lbl_image_photo.setPixmap(QPixmap())
        self.input_name.setText("")
        self.gender = ""
        self.birthday = ""
        # Обнуляем Radio
        # self.clear_radio_gender()
        cur.close()

    def init_db(self):
        self.conn = sqlite3.connect("library.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS books_person (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        id_persons TEXT , 
                        article TEXT,
                        name TEXT,
                        author TEXT,
                        year TEXT, 
                        status TEXT DEFAULT FALSE,
                        last_person INTEGER,
                        image BLOB)
                        """)

        self.conn.commit()
        self.conn.close()

    # def check_is_uniqueness(self) -> bool:
    #     flag = True
    #     check = self.subscribers_number.text()
    #     check2 = self.input_email.text()
    #     if check == '' or check2 == '' or check2 is None or check is None:
    #         message_form(f"Не заполнены обязательные поля записи: № абонента и его почта!",
    #                      "Ошибка!", QMessageBox.Icon.Warning)
    #     else:
    #         self.conn = sqlite3.connect("library.db")
    #         self.cur = self.conn.cursor()
    #         self.cur.execute(f"SELECT COUNT(*) FROM persons")
    #         result = self.cur.fetchone()
    #         if result[0] > 0:
    #             self.cur.execute(f"SELECT number, email FROM persons WHERE number = {check}  OR email = {check2}")
    #             result = self.cur.fetchone()
    #             self.conn.commit()
    #             self.cur.close()
    #             if result is not None:
    #                 flag = False
    #                 msg = []
    #                 message = ""
    #                 if check in result[0]:
    #                     msg.append('Абонент с таким номером уже существует!')
    #                 if check2 in result[1]:
    #                     msg.append('Абонент с такой электронной почтой уже существует!')
    #                 for m in msg:
    #                     message += f"{m}\n"
    #                 if check in result[0] or check2 in result[1]:
    #                     msg_box = QMessageBox()
    #                     msg_box.setText(message)
    #                     msg_box.setWindowTitle('Ошибка уникальности!')
    #                     msg_box.setIcon(QMessageBox.Icon.Information)
    #                     msg_box.exec()
    #     return flag
    #
    # def add_person_db(self):
    #     check = self.check_is_uniqueness()
    #     if check == False:
    #         self.view_quest("Анкета ранее уже добавлена в базу")
    #     if self.check_quest() == False:
    #         self.view_quest("Анкета не заполнена")
    #     elif self.check_quest() and check:
    #         self.conn = sqlite3.connect("library.db")
    #         self.cur = self.conn.cursor()
    #         pixmap = self.lbl_image_photo.pixmap()
    #         blob_photo = convert_pixmap_to_byte_array(pixmap)
    #         self.cur.execute("INSERT INTO persons (name, born, gender, number, email, photo) "
    #                          "VALUES(?, ?, ?, ?, ?, ?)",
    #                     (self.input_name.text(), self.birthday, self.gender,
    #                      self.subscribers_number.text(), self.input_email.text(), blob_photo))
    #         self.conn.commit()
    #         self.cur.close()
    #         self.view_quest("Анкета добавлена в БД")
    #
    #
    # def del_person_db(self):
    #     index = self.subscribers_number.text()
    #     if index == "":
    #         message_form(f"Пустых записей в базе данных нет!", "Удаление невозможно", QMessageBox.Icon.Warning)
    #     else:
    #         self.conn = sqlite3.connect("library.db")
    #         self.find_person_db()
    #         self.cur = self.conn.cursor()
    #         self.cur.execute(f"DELETE FROM persons WHERE name = (SELECT name FROM persons WHERE number = '{index}')")
    #         self.conn.commit()
    #         self.cur.close()
    #         self.view_quest("Удалена анкета")
    #         self.new_form()
    #
    # def find_person_db(self):
    #     index = self.subscribers_number.text()
    #     self.conn = sqlite3.connect("library.db")
    #     self.cur = self.conn.cursor()
    #     self.cur.execute(f"SELECT name, born, gender, number, email, photo FROM persons WHERE number = '{index}'")
    #     result = self.cur.fetchone()
    #     self.cur.close()
    #     if result is not None:
    #         self.input_name.setText(result[0])
    #         year, month, day = convert_date_year_month_day(result[1])
    #         self.calendar_date_birthday.setSelectedDate(QDate(int(year), int(month), int(day)))
    #         self.gender = str(result[2])
    #         self.clear_radio_gender()
    #         if "Муж" in self.gender:
    #             self.rd_man.setChecked(True)
    #         else:
    #             self.rd_women.setChecked(True)
    #         self.subscribers_number.setText(result[3])
    #         self.input_email.setText(result[4])
    #
    #         self.pixmap = (convert_byte_array_to_pixmap(result[5]))
    #         self.lbl_image_photo.setPixmap(self.pixmap)
    #
    #         self.view_quest("Анкета найдена в базе")
    #         scale = 100
    #         self.slider_scale.setValue(scale)
    #         self.get_scale()
    #     else:
    #         message_form(f"Анкета абонента: {self.subscribers_number.text()} не найдена в базе данных",
    #                      "Анкета не найдена", QMessageBox.Icon.Warning)
    #         self.new_form()
    #
    #
    # def update_person_db(self):
    #     if self.check_quest():
    #         self.conn = sqlite3.connect("library.db")
    #         pixmap = self.lbl_image_photo.pixmap()
    #         blob_photo = convert_pixmap_to_byte_array(pixmap)
    #         self.cur = self.conn.cursor()
    #         sql_update = (f"UPDATE persons SET name=?, born=?, gender=?, number=?, email=?, photo=? "
    #                       f"WHERE number = '{self.subscribers_number.text()}'")
    #
    #         self.cur.execute(sql_update, (self.input_name.text(), self.birthday, self.gender, self.subscribers_number.text(),
    #                                  self.input_email.text(), blob_photo))
    #         self.conn.commit()
    #         self.cur.close()
    #         self.view_quest("Анкета изменена и записана в БД")
    #         self.new_form()
    #     elif self.check_quest() == False:
    #         message_form(f"Нельзя редактировать запись c пустыми полями", "Изменение невозможно",
    #                      QMessageBox.Icon.Warning)

    def import_db(self):
        pass

    def check_book_status(self):
        pass

    def add_book_db(self):
        pass

    def del_book_db(self):
        pass

    def find_book_db(self):
        pass

    def edit_book_db(self):
        pass

    def exit_form(self):
        pass

def issue_resource(self):
    global subscriber
    subscriber = self.input_name.text()
    if self.win is None:
        self.win = OrderBook()
        self.win.show()
    else:
        self.win.close()
        self.win = None
        self.issue_resource()
