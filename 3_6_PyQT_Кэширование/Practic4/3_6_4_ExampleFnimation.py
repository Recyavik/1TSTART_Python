import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt5.QtCore import Qt, QTimer, QElapsedTimer
from PyQt5.QtGui import QPainter, QPixmap


class SnowFall(QFrame):

    def __init__(self, parent: QMainWindow):
        super().__init__(parent)

        self.snowflakePixmap = QPixmap("snow.png")
        self.initUI()

    def initUI(self) -> None:
        self.snow_flakes = []
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_snow_flakes)
        self.timer.start(16)

        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_snow_flakes(qp)
        qp.end()

    def draw_snow_flakes(self, qp: QPainter):
        for x, y, size, _ in self.snow_flakes:
            scaled_pixmap = self.snowflakePixmap.scaled(size, size)
            qp.drawPixmap(int(x), int(y), scaled_pixmap)

    def update_snow_flakes(self):
        elapsed = self.elapsed_timer.elapsed()
        self.elapsed_timer.restart()

        dt = elapsed / 1000.0

        if random.choice([True, False]):
            x, y = random.randint(0, self.width()), 0
            speed = random.randint(200, 400)
            size = random.randint(15, 30)

            self.snow_flakes.append((x, y, size, speed))

        new_snow_flakes = []
        for x, y, size, speed in self.snow_flakes:
            y += speed * dt
            if y < self.height():
                new_snow_flakes.append((x, y, size, speed))

        self.snow_flakes = new_snow_flakes
        self.update()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.frame = SnowFall(self)
        self.setCentralWidget(self.frame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.showFullScreen()
    sys.exit(app.exec())