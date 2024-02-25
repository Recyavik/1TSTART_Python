import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget


class ProgressIndicator(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(50)  # Обновление угла каждые 50 миллисекунд

    def update_angle(self):
        self.angle += 10
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.blue))
        painter.setPen(Qt.NoPen)

        width = self.width()
        height = self.height()
        side = min(width, height)
        x = (width - side) // 2
        y = (height - side) // 2

        painter.drawPie(x, y, side, side, self.angle * 16, 120 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ProgressIndicator()
    widget.resize(200, 200)
    widget.show()
    sys.exit(app.exec_())
