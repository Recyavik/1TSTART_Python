import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QVBoxLayout
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
        self.setWindowTitle("Прогресс индикатор")
        self.progress_bar = QProgressBar()
        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignCenter)


        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = ProgressBarWidget()


    widget.show()

    sys.exit(app.exec_())
