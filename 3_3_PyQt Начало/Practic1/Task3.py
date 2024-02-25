# PyQt предоставляет мощные инструменты, обширный набор функций Qt и широкую поддержку сообщества,
# что делает его привлекательным выбором для разработки кроссплатформенных приложений с использованием Python.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout

# Создаем экземпляр приложения
app = QApplication(sys.argv)
# Создаем родительский виджет
window = QWidget()
# Создаем вертикальный макет
layout = QVBoxLayout()
# layout = QHBoxLayout()
# Создаем виджеты
button1 = QPushButton("Кнопка 1")
button2 = QPushButton("Кнопка 2")
label = QLabel("Метка")
# Добавляем виджеты в макет
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(label)
# Устанавливаем макет для родительского виджета
window.setLayout(layout)
# Отображаем окно
window.show()
# Запускаем главный цикл приложения
sys.exit(app.exec_())

# В этом примере мы создаем родительский виджет QWidget и вертикальный макет QVBoxLayout.
# Затем мы создаем несколько виджетов QPushButton и QLabel и добавляем их в макет с помощью addWidget().
# Наконец, мы устанавливаем макет для родительского виджета window с помощью setLayout().
# Как результат, виджеты будут отображаться в вертикальной последовательности внутри окна.