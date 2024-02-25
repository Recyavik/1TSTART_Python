from PyQt5 import QtWidgets, QtCore, QtGui
import sys

pen = QtGui.QPen(QtGui.QColor(0, 24, 128, 200), 10, style=QtCore.Qt.SolidLine, cap=QtCore.Qt.SquareCap)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        central_widget = QtWidgets.QWidget()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.view.setSceneRect(self.view.mapToScene(self.view.viewport().rect()).boundingRect())
        self.btn = QtWidgets.QPushButton('Rotate')
        self.btn.clicked.connect(self.animateRotation)
        h_box = QtWidgets.QHBoxLayout(central_widget)
        h_box.addWidget(self.view)
        h_box.addWidget(self.btn)
        self.scene.addEllipse(QtCore.QRectF(0, 0, 100, 250), pen=pen)
        self.view.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.CrossPattern))
        self.setCentralWidget(central_widget)
        print(self.scene.items()[0])

    def rot(self, angle: QtCore.QVariant) -> None:
        self.view.rotate(self.scene.items()[0].rotation() - angle)
        self.scene.items()[0].setRotation(angle)

    @QtCore.pyqtSlot()
    def animateRotation(self):
        animation = QtCore.QVariantAnimation(self)
        animation.setStartValue(QtCore.QVariant(0))
        animation.setEndValue(QtCore.QVariant(45))
        animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        animation.valueChanged.connect(self.rot)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())