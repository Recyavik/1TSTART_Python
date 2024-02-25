import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QStylePainter, QSizePolicy,
    QStyleOptionButton, QStyle, QHBoxLayout, QButtonGroup, QApplication)
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)


class RotatedButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)

        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.setFixedWidth(2*self.fontMetrics().height())

    def paintEvent(self, event):
        painter = QStylePainter(self)
        painter.rotate(-90)
        painter.translate(-self.height(), 0)
        option = QStyleOptionButton()
        self.initStyleOption(option)
        size = option.rect.size()
        size.transpose()
        option.rect.setSize(size)
        painter.drawControl(QStyle.CE_PushButton, option)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout(self)

        self.buttonGroup = QButtonGroup()
        self.attr_layout = QHBoxLayout()
        self.main_layout.addLayout(self.attr_layout)

#        self.rb0 = RotatedButton("Hello World", self, orientation="west")
        self.rb0 = RotatedButton("Hello World", self)

        self.attr_layout.addWidget(self.rb0)
        self.buttonGroup.addButton(self.rb0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.setMinimumSize(QSize(0, 400))
    w.show()
    sys.exit(app.exec_())