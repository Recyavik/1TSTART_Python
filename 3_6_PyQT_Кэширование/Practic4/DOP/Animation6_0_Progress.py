import sys
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget


class ProgressIndicator(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.progress = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)  # Обновление прогресса каждые 50 миллисекунд

    def update_progress(self):
        self.progress += 1
        if self.progress > 100:
            self.progress = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()
        side = min(width, height)
        x = (width - side) // 2
        y = (height - side) // 2

        # Отрисовка прогресс индикатора
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 255))
        painter.drawPie(x, y, side, side, 0, self.angle * 16)

        # Отрисовка процентов
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 12))
        text = f'{self.progress}%'
        text_width = painter.fontMetrics().width(text)
        text_height = painter.fontMetrics().height()
        text_x = x + (side - text_width) // 2
        text_y = y + (side + text_height) // 2
        painter.drawText(text_x, text_y, text)

    def sizeHint(self):
        return QSize(200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ProgressIndicator()
    widget.show()
    sys.exit(app.exec_())
