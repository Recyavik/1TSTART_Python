from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: rgb(0, 0, 0);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame {\n"
                                 "background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(220, 220, 220);\n"
                                 "border-radius: 10px\n"
                                 "\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.progressBar = QtWidgets.QProgressBar(self.frame)
        #        self.progressBar.setGeometry(QtCore.QRect(126, 530, 220, 30))
        # +++
        self.progressBar.setStyleSheet("""
        QProgressBar {
            background-color: #DA7B93;
            color: rgb(200, 200, 200);
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
        }
        QProgressBar::chunk {
            border-radius: 10px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
        }
        """)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        # +++
        self.progressBar.resize(self.width() - 180, 40)
        self.progressBar.move(80, 510)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, 150)
        self.progressBar.setValue(20)

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(300, 560, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 431, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Ka.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(42, 274, 391, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Ka.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "1T"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

        self.start_animation()

    def loading(self):
        self.progressBar.setValue(self.counter)
        self.counter += 1
        if self.counter == 151: self.timer.stop()

    def start_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.label)
        self.label.setGraphicsEffect(opacity_effect)
        '''
        geometry_animation = QtCore.QPropertyAnimation(
            self.label,
            b"geometry",
            duration=4700,
            startValue=QtCore.QRect(190, -260, 671, 261),
            endValue=QtCore.QRect(42, 274, 391, 231),
        )
        '''
        opacity_animation = QtCore.QPropertyAnimation(opacity_effect, b"opacity", duration=6000, startValue=0.0, endValue=1.0)

        group = QtCore.QParallelAnimationGroup(self.label)
        #        group.addAnimation(geometry_animation)
        group.addAnimation(opacity_animation)
        group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())