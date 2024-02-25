from PyQt6.QtWidgets import (QApplication, QGraphicsView,
                             QGraphicsPixmapItem, QGraphicsScene)
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import (QObject, QPointF, QPropertyAnimation, pyqtProperty)
import sys


class Ball(QObject):

    def __init__(self):
        super().__init__()
        self.pixmap_item = QGraphicsPixmapItem(QPixmap('img.png'))

    def _set_pos(self, pos):
        self.pixmap_item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=_set_pos)


class Example(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.initView()

    def initView(self):

        self.ball = Ball()

        self.anim = QPropertyAnimation(self.ball, b'pos')
        self.anim.setDuration(3000)

        self.anim.setStartValue(QPointF(150, 130))

        self.anim.setKeyValueAt(0.3, QPointF(280, 230))
        self.anim.setKeyValueAt(0.5, QPointF(100, 150))
        self.anim.setKeyValueAt(0.8, QPointF(180, 240))
        self.anim.setEndValue(QPointF(290, 130))

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 600, 600)
        self.scene.addItem(self.ball.pixmap_item)
        self.setScene(self.scene)

        self.setWindowTitle('Анимация')
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setGeometry(400, 300, 500, 350)

        self.anim.start()

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()