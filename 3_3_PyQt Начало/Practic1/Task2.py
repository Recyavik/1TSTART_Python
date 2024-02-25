import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

def say_hello():
    name = text_field.text()
    message = f"Привет, {name}!"
    QMessageBox.information(window, "Приветствие", message)

# Создаем экземпляр приложения
app = QApplication(sys.argv)
# Создаем родительский виджет
window = QWidget()
# Создаем вертикальный макет
layout = QVBoxLayout()
# Создаем метку
label_name = QLabel("Введите ваше имя:")
layout.addWidget(label_name)
# Создаем текстовое поле
text_field = QLineEdit()
layout.addWidget(text_field)
# Создаем кнопку
button1 = QPushButton("Это кнопка")
layout.addWidget(button1)
# Функция-обработчик для кнопки


# Подключаем функцию-обработчик к сигналу clicked кнопки
button1.clicked.connect(say_hello)
# Устанавливаем макет для родительского виджета
window.setLayout(layout)
# Отображаем окно
window.show()
# Запускаем главный цикл приложения
sys.exit(app.exec_())
