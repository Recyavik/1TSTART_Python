import random
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
        QLabel, QLineEdit, QPushButton, QWidget,
        QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тренажёр таблицы умножения")
        self.setGeometry(100, 100, 400, 180)
        self.initUI()

    def initUI(self):
        self.example_label = QLabel("a + b = ",self)
        self.comment_label = QLabel("Комментарий: ", self)
        self.input_answer = QLineEdit(self)
        self.input_answer.setToolTip("Введите свой ответ в это поле при решении")
        check_answer_button = QPushButton(QIcon("check.jpg")," Проверить ответ", self)

        new_example_button = QPushButton("Новый пример", self)
        view_answer_button = QPushButton("Показать ответ")

        # Размещение виджетов на макетах
        layout = QVBoxLayout()

        layout_example = QHBoxLayout()
        layout_example.addWidget(self.example_label)
        layout_example.addWidget(self.input_answer)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(check_answer_button)
        layout_buttons.addWidget(new_example_button)
        layout_buttons.addWidget(view_answer_button)

        layout_comment = QHBoxLayout()
        layout_comment.addWidget(self.comment_label)

        layout.addLayout(layout_example)
        layout.addLayout(layout_buttons)
        layout.addLayout(layout_comment)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.new_example()

        # События нажатия
        check_answer_button.clicked.connect(self.check_answer)
        new_example_button.clicked.connect(self.new_example)
        view_answer_button.clicked.connect(self.view_answer)

        # Стиль
        self.setStyleSheet("""
        QMainWindow {
            background-color: #FFA07A;
        }
        QLabel {
            color: black;
            font: bold italic large georgia;
            font-size: 18px;
        }
        QPushButton {
            background-color: #8B008B;
            color: white;
            font: bold italic large georgia;
            font-size: 16px;
            border: 2px solid white;
            padding: 10px 20px;
            border-radius: 10px;
        }
        QLineEdit {
            border: 2px solid white;
            border-radius: 10px;
            font: bold italic large georgia;
            font-size: 18px;
        }
        """)

    def check_answer(self):
        list_choice_good = ["Великолепно!", "Здорово!", "Супер!", "Отлично!", "Молодец!"]
        list_choice_bad = ["Эх!", "А если подумать?", "Не верно!", "Нет!"]
        text = self.input_answer.text()
        example_and_answer = self.example_label.text() + str( self.answer)
        if str(self.answer) == str(text).strip():
            out_text = (random.choice(list_choice_good) +
                        " Это правильный ответ: " + example_and_answer)
        else:
            out_text = (random.choice(list_choice_bad) +
                        " Правильный ответ: " + example_and_answer)
        self.comment_label.setText(out_text)


    def new_example(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        self.answer = a * b
        self.example_label.setText(str(a) + " * " + str(b) + " = ")
        self.input_answer.clear()
        self.comment_label.setText("Реши пример.")

    def view_answer(self):
        self.comment_label.setText("Надо запомнить: " +
                                   self.example_label.text() + str(self.answer))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()