import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget


class RotatingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(20)  # Обновление угла каждые 20 миллисекунд

    def update_angle(self):
        self.angle += 1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.angle)
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(-50, -50, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = RotatingWidget()
    widget.resize(400, 400)
    widget.show()
    sys.exit(app.exec_())