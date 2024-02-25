import random
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication,  QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.answer = None
        self.input_answer = None
        self.comment_label = None
        self.example_label = None
        self.setWindowTitle("Тренажёр таблицы умножения")
        self.setGeometry(100, 100, 300, 180)
        self.initUI()

    def initUI(self):
        self.example_label = QLabel("", self)
        self.comment_label = QLabel("Комментарий:")
        self.input_answer = QLineEdit(self)
        self.new_example()
        self.input_answer.setToolTip("Решите пример")
        check_answer_button = QPushButton("Проверить ответ")
        new_example_button = QPushButton("Новый пример")
        view_answer_button = QPushButton("Показать ответ")

        # Размещение виджетов с помощью менеджера компоновки
        layout = QVBoxLayout()
        layout_example = QHBoxLayout()
        layout_example.addWidget(self.example_label)
        layout_example.addWidget(self.input_answer)
        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(check_answer_button)
        layout_buttons.addWidget(new_example_button)
        layout_buttons.addWidget(view_answer_button)
        layout_comment = QVBoxLayout()
        layout_comment.addWidget(self.comment_label)
        layout.addLayout(layout_example)
        layout.addLayout(layout_buttons)
        layout.addLayout(layout_comment)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Назначение имен и событий нажатия
        check_answer_button.setObjectName("checkAnswer")
        check_answer_button.clicked.connect(self.check_answer)
        new_example_button.setObjectName("newExample")
        new_example_button.clicked.connect(self.new_example)
        view_answer_button.setObjectName("viewAnswer")
        view_answer_button.clicked.connect(self.view_answer)
        self.input_answer.setObjectName("inputAnswer")

        # Стиль
        self.setStyleSheet("""
            QMainWindow {
                background-color: #eaebb2;
            }
            QLabel{
                color: black;
                font-size: 16px;
            }
            QPushButton {
                background-color: #617860;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
            }
            QLineEdit {
                border: 2px solid #617860;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }
        """)

    def check_answer(self):
        list_chose_good = ["Великолепно!", "Здорово!", "Супер!", "Отлично!"]
        list_chose_bad = ["Эх!", "А если подумать?", "Нет!", "Не верно!"]
        text = self.input_answer.text()
        example_and_answer = self.example_label.text() + str(self.answer)
        if str(self.answer) == str(text).strip():
            out_text = random.choice(list_chose_good) + " Это правильный ответ: " + example_and_answer
        else:
            out_text = random.choice(list_chose_bad) + " Правильный ответ: " + example_and_answer
        self.comment_label.setText(out_text)

    def new_example(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        self.answer = a * b
        self. example_label.setText(str(a)+"*"+str(b)+"=")
        self.comment_label.setText("Решите пример. ")
        self.input_answer.clear()

    def view_answer(self):
        self.comment_label.setText("Надо запомнить: "+self.example_label.text() + str(self.answer))


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
