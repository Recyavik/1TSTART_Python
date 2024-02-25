from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem)


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(480, 80))
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Имя","Возраст","Город"])
        self.table.setItem(0,0, QTableWidgetItem("Таня"))
        self.table.setItem(0,1, QTableWidgetItem("25"))
        self.table.setItem(0,2, QTableWidgetItem("Москва"))
        self.table.setItem(1,0, QTableWidgetItem("Андрей"))
        self.table.setItem(1,1, QTableWidgetItem("26"))
        self.table.setItem(1,2, QTableWidgetItem("Новосибирск"))
        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication([])
    mw = MyWindow()
    mw.show()
    app.exec()
