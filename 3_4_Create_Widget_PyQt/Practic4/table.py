import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window1 = QMainWindow()
window2 = QMainWindow()

# здесь можно настроить окна

window1.show()
window2.show()
app.exec_()