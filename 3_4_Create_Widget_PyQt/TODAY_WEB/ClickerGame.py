import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import random as rnd
from PyQt6.QtCore import QTimer


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.timer = None
        self.score_label = None
        self.label = None
        self.time_label = None
        self.button = None
        self.score = 0
        self.init_ui()

    def init_ui(self):
        # Устанавливаем значение по умолчанию на дисплей
        self.score = 0
        self.setWindowTitle("Игра: 10 кликов!")
        self.setGeometry(600, 400, 640, 480)
        self.score_label = QLabel("Счёт: Начали!  ", self)
        self.label = QLabel("Время:           ", self)
        self.label.move(100, 10)
        self.score_label.move(320, 10)
        self.time_label = QLabel("            ", self)
        self.time_label.setNum(3)
        self.time_label.move(160, 10)
        self.button = QPushButton("*", self)
        self.view_button()
        self.button.clicked.connect(self.clik_button)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_timer)

    def view_button(self):
        x = rnd.randint(20, 620)
        y = rnd.randint(20, 430)
        self.button.move(x, y)
        # Стиль
        self.setStyleSheet("""
                    QWidget {
                        background-color: #effbb2;
                    }
                    QLabel{
                        color: black;
                        font-size: 16px;
                    }
                    QPushButton {
                        background-color: red;
                        color: white;
                        border: black;
                        padding: 8px 16px;
                        border-radius: 10px;
                        font: bold;
                        font-size: 12px;
                    }
                """)

    def clik_button(self):
        if self.score >= 10:
            self.timer.stop()
            self.time_label.setText("")
            self.label.setText("Победа!")
            self.time_label.setText("        ")
            self.score = 0
        else:
            self.label.setText("Время:")
            self.score += 1
            self.score_label.setText("Счёт: "+str(self.score))
            self.view_button()
            self.time_label.setNum(3)
            self.timer.stop()
            self.timer.start(1000)

    def tick_timer(self):
        time_label_value = int(self.time_label.text())
        if time_label_value > 0:
            # Устанавливаем значение на 1 меньше
            self.time_label.setNum(time_label_value-1)
        else:
            self.timer.stop()
            self.time_label.setText("")
            self.label.setText("Вы проиграли!")
            self.time_label.setText("")
            self.score = 0


def start_game():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())


start_game()
