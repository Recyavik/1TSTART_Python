from PyQt5.uic.properties import QtGui
from PyQt6.QtWidgets import (QMessageBox)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QBuffer, QByteArray, QDate, QIODeviceBase, Qt

subscriber = ''


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