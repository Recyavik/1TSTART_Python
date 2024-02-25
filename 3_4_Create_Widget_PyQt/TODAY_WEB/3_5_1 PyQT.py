from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QPushButton, QGridLayout, QSizePolicy)
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Розы и ромашки")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()


    def initUI(self):
        self.button_array = [QPushButton(str(i), self) for i in range(1, 26)]
        i = 0
        self.layout_array = QGridLayout(self)

        for el in self.button_array:
            self.layout_array.addWidget(el, i // 5, i % 5)
            el.clicked.connect(lambda _, ind_i=i // 5, ind_j=i % 5: self.slot(ind_i, ind_j))
            i += 1

        self.lbl_flower = QLabel(self)
        # self.lbl_flower.setFixedSize(300, 300)
        self.lbl_flower.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_flower.setAlignment(Qt.AlignCenter)

        self.layout_main = QVBoxLayout()
        self.layout_main.addLayout(self.layout_array)
        self.layout_main.addWidget(self.lbl_flower)

        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)

    def slot(self, i, j):
        number = i*5+j+1
        print(number)
        pixmap_rosa = QPixmap("rosa.png")
        pixmap_romashka = QPixmap("romashka.png")
        if number % 2 == 0:
            self.lbl_flower.setPixmap(pixmap_romashka)
        else:
            self.lbl_flower.setPixmap(pixmap_rosa)
        self.lbl_flower.setAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()