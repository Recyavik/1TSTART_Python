import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class ResizingButton(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Нажми меня', self)
        self.width = 100
        self.height = 50
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_size)
        self.timer.start(20)  # Обновление размера каждые 20 миллисекунд

    def update_size(self):
        self.width += 1
        self.height += 1
        self.button.resize(self.width, self.height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(0, 0, self.width, self.height)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ResizingButton()
    widget.resize(400, 400)
    widget.show()
    sys.exit(app.exec_())
