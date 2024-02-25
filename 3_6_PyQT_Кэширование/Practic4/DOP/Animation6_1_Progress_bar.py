import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QVBoxLayout, QScrollBar


class ProgressIndicator(QWidget):
    def __init__(self):
        super().__init__()

        self.progress_bar = QProgressBar()
        self.progress_label = QLabel()
        self.scroll_bar = QScrollBar(Qt.Horizontal)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)
        layout.addWidget(self.scroll_bar)

        self.setLayout(layout)

        self.scroll_bar.valueChanged.connect(self.update_progress)

    def update_progress(self, value):
        self.progress_bar.setValue(value)
        self.progress_label.setText(f"Progress: {value}%")

    def set_range(self, minimum, maximum):
        self.progress_bar.setRange(minimum, maximum)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    progress_indicator = ProgressIndicator()
    progress_indicator.set_range(0, 100)

    scroll_bar = progress_indicator.scroll_bar
    scroll_bar.setRange(0, 100)

    scroll_bar.setValue(0)

    progress_indicator.show()

    sys.exit(app.exec_())
