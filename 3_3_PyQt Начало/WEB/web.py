# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QColorDialog
# import webbrowser
# from PyQt6.QtGui import QIcon
#
# class MyFirstProject(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("First Project")
#         self.setGeometry(100,100,200,300)
#
#         self.i=0
#
#         self.label = QLabel(self)
#         self.label.setText("Привет, PyQt6")
#         self.label.setGeometry(50,50,500,30)
#
#         self.button = QPushButton(self)
#         self.button.setIcon(QIcon("image.png"))
#         # self.button.setGeometry(50,100,100,30)
#         self.button.move(50,100)
#         self.button.setIconSize(self.button.size())
#         self.button.clicked.connect(self.button_click)
#
#         self.edit_text = QLineEdit(self)
#         self.edit_text.setGeometry(50,150,100,30)
#
#     def button_click(self):
#         # self.label.setText(f"hi, {self.edit_text.text()}")
#         # QMessageBox.information(self,"Сообщение","Вы нажали на кнопку")
#         # color = QColorDialog.getColor()
#         # if(color.isValid()):
#         #     self.label.setText(f"Цвет: {color.name()}, {color.getRgb()}, {color.getHsl()}, {color.getHsv()}")
#         webbrowser.open("https://google.com")
#
#         # if(self.i<5):
#         #     self.label.setText("hello")
#         # elif(self.i<10):
#         #     self.label.setText("Helllllloooooo")
#         # elif(self.i<15):
#         #     self.label.setText("hiiiiiiiiiiiiiiiiiii")
#         # elif(self.i<20):
#         #     self.label.setText("Хватит уже")
#         # self.i+=1
# app = QApplication([])
# window = MyFirstProject()
# window.show()
# app.exec()






from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QColorDialog
import webbrowser
from PyQt6.QtGui import QIcon

class OpenProject(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Open")
        self.setGeometry(500,500,800,800)

        self.button_google = QPushButton(self)
        self.button_google.setIcon(QIcon('google.png'))
        self.button_google.move(50,50)
        self.button_google.setIconSize(self.button_google.size())
        self.button_google.clicked.connect(self.open_google)

        self.button_youtube = QPushButton(self)
        self.button_youtube.setIcon(QIcon('youtube.png'))
        self.button_youtube.move(150,50)
        self.button_youtube.setIconSize(self.button_youtube.size())
        self.button_youtube.clicked.connect(self.open_youtube)

        self.button_vk = QPushButton(self)
        self.button_vk.setIcon(QIcon('vk.png'))
        self.button_vk.move(250, 50)
        self.button_vk.setIconSize(self.button_youtube.size())
        self.button_vk.clicked.connect(self.open_vk)
    def open_google(self):
        webbrowser.open("https://google.com")
    def open_youtube(self):
        webbrowser.open("https://youtube.com")
    def open_vk(self):
        webbrowser.open('https://vk.com')


app = QApplication([])
window = OpenProject()
window.show()
app.exec()