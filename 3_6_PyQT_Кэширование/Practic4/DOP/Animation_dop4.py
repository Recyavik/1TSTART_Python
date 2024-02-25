import sys
from PyQt5 import QtWidgets,QtCore,QtGui
import threading
import time

app = QtWidgets.QApplication(sys.argv)
windows = QtWidgets.QWidget()
window_layout = QtWidgets.QGridLayout()

def to_run():
    while True:
        donwloading_label.setStyleSheet("""
        background-color:rgba(0,0,0,0);
        border-radius:250;
        border-style:solid;
        border-color:rgba(0, 0, 0,0);
        border-width:25;
        color:rgb(255,255,255);
        font-size:30px;

        border-top-color:rgb(0, 0, 0);
        """)
        time.sleep(0.1)
        donwloading_label.setStyleSheet("""
        background-color:rgba(0,0,0,0);
        border-radius:250;
        border-style:solid;
        border-color:rgba(0, 0, 0,0);
        border-width:25;
        color:rgb(255,255,255);
        font-size:30px;

        border-right-color:rgb(0, 0, 0);
        """)
        time.sleep(0.1)
        donwloading_label.setStyleSheet("""
        background-color:rgba(0,0,0,0);
        border-radius:250;
        border-style:solid;
        border-color:rgba(0, 0, 0,0);
        border-width:25;
        color:rgb(255,255,255);
        font-size:30px;

        border-bottom-color:rgb(0, 0, 0);
        """)
        time.sleep(0.1)
        donwloading_label.setStyleSheet("""
        background-color:rgba(0,0,0,0);
        border-radius:250;
        border-style:solid;
        border-color:rgba(0, 0, 0,0);
        border-width:25;
        color:rgb(255,255,255);
        font-size:30px;

        border-left-color:rgb(0, 0, 0);
        """)
        time.sleep(0.1)


def any():
   tt = threading.Thread(target=to_run)
   tt.start()


donwloading_label = QtWidgets.QLabel()
donwloading_label.setAlignment(QtCore.Qt.AlignCenter)
donwloading_label.setText("Please Wait....")
donwloading_label.setFixedSize(500,500)
donwloading_label.setStyleSheet("""
background-color:rgba(0,0,0,0);
border-radius:250;
border-style:solid;
border-color:rgba(0, 0, 0,0);
border-width:25;
color:rgb(255,255,255);
font-size:30px;
""")

any()

window_layout.addWidget(donwloading_label)
windows.setLayout(window_layout)
windows.show()
sys.exit(app.exec_())