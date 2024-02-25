import random
import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer


class ProgressBarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.proc = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(20)  # Обновление размера каждую 20 миллисекунд


    def init_ui(self):
        self.resize(500, 80)
        self.setWindowTitle("Игра - поймай процент!")
        self.target = random.randint(10, 100)
        self.target_label = QLabel("Поймай " + str(self.target)+" %", self)
        self.target_label.setAlignment(Qt.AlignCenter)
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("color: blue")
        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.stop_button = QPushButton("Стоп", self)
        self.stop_button.setToolTip("Нажми, чтобы поймать!")
        self.setStyleSheet("""QLabel {font-size: 16px; }
                             QPushButton{font-size: 16px; }
                             QProgressBar{font-size: 16px;}""")
        self.stop_button.clicked.connect(self.stop_target)

        layout = QVBoxLayout()
        layout.addWidget(self.target_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def set_progress(self, value):
        self.progress_bar.setValue(value)
        self.progress_label.setText(f"{value}%")

    def update_progress(self):
        if self.proc == 0:
            self.step = 1
        elif self.proc == 100:
            self.step = -1
        self.proc = self.proc + self.step
        widget.set_progress(self.proc)

    def stop_target(self):
        if self.proc == self.target:
            QMessageBox.information(self, "Победа!" , "Вы поймали процент!")
            sys.exit()
        else:
            QMessageBox.warning(self, "Попробуй ещё!", "Вы поймали " + str(self.proc) + " %")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ProgressBarWidget()
    widget.show()
    sys.exit(app.exec_())
