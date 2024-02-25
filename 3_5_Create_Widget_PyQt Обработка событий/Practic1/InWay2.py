from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QVBoxLayout, QWidget, QPushButton, QLineEdit,
                             QComboBox, QHBoxLayout, QAction, QSizePolicy)
from PyQt5.QtGui import QPixmap, QKeySequence, QIntValidator, QRegExpValidator, QValidator
from PyQt5.QtCore import Qt, QRegExp

# https://pro-prof.com/forums/topic/qvalidator-qt_cplusplus

class QRV(QRegExpValidator):
    def __init__(self, reg_exp_str):
        super().__init__(QRegExp(reg_exp_str))

    def validate(self, text, pos):
        res, s, i = super().validate(text, pos)
        if res != QValidator.Acceptable:
            s = self.fixup(text)
        return res, s, i

    def fixup(self, s):
        if ',' in s:
            s = s.replace(',', '.')
        return s


def get_cost(price, discount, number):
    return (price - price * (discount / 100)) * number


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Автомобильная заправка "В ПУТЬ!" ')
        self.setGeometry(200, 200, 600, 200)
        self.fuel = {"A-92": [1500, 47.29], "A-95": [2600, 51.90], "ДТ": [1200, 55],
                     "ГАЗ": [1800, 45]}
        self.undo_stack = []
        self.text_color = Qt.black
        self.total = 0
        self.count_receipt = 1
        self.init_ui()

    def init_ui(self):
        # # Создание виджетов
        self.lbl_logo = QLabel(self)
        pixmap = QPixmap("logo.jpg")
        self.lbl_logo.setPixmap(pixmap)
        self.lbl_logo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_logo.setAlignment(Qt.AlignCenter)

        self.lbl_name = QLabel(self)
        self.lbl_name.setText("Топливо:")
        self.lbl_name.setFixedSize(100, 40)
        self.combo_box_fuel = QComboBox(self)
        for key in self.fuel.keys():
            self.combo_box_fuel.addItem(key)
        self.combo_box_fuel.setToolTip("Марка топлива")
        self.combo_box_fuel.currentIndexChanged.connect(self.update_combo)

        self.lbl_all_count = QLabel(self)
        self.lbl_all_count.setFixedSize(220, 40)
        self.lbl_all_count.setText(("Остаток: " +
                                    str(self.fuel[self.combo_box_fuel.currentText()][0])
                                    + " литров"))
        self.lbl_all_count.setToolTip("Остаток топлива на заправке")
        self.lbl_all_count.setObjectName("Count")


        self.lbl_price = QLabel(self)
        self.lbl_price.setText("Цена:")
        self.input_price = QLineEdit(self)
        pMyValidator = QRV(r'^(?:\d{1,2})[.,]\d{2}$')
        self.input_price.setValidator(pMyValidator)
        self.input_price.setText(str(self.fuel[self.combo_box_fuel.currentText()][1]))
        self.input_price.setToolTip("Введите в это поле цену")
        self.input_price.textChanged.connect(self.update)

        self.lbl_number = QLabel(self)
        self.lbl_number.setText("Количество:")
        self.input_number = QLineEdit(self)
        pIntvalidator = QIntValidator(self)
        pIntvalidator.setRange(1, 99)
        self.input_number.setValidator(pIntvalidator)
        self.input_number.setText(str("1"))
        self.input_number.setToolTip("Введите в поле количество литров от  1 до 99")
        self.input_number.textChanged.connect(self.update)

        self.lbl_discount = QLabel(self)
        self.lbl_discount.setText("Скидка:")
        self.lbl_discount.setFixedSize(100, 40)
        self.discount = [0, 1, 2, 3, 5, 10]
        self.combo_box_discont = QComboBox(self)
        for el in self.discount:
            self.combo_box_discont.addItem(str(el)+"%")
        self.combo_box_discont.setToolTip("Скидка клиента")
        self.combo_box_discont.currentIndexChanged.connect(self.update)

        self.lbl_cost = QLabel(self)
        self.lbl_cost.setFixedSize(220, 40)
        self.cost = get_cost(self.fuel[self.combo_box_fuel.currentText()][1],
                                  int(self.combo_box_discont.currentText()[:-1]),
                                  int(self.input_number.text()))
        self.lbl_cost.setText(("Стоимость: " + str(round(self.cost, 2)) + " руб."))
        self.lbl_cost.setToolTip("Стоимость заправки")
        self.lbl_cost.setObjectName("cost")

        self.lbl_itog = QLabel(self)
        self.lbl_itog.setFixedSize(280, 40)
        self.lbl_itog.setText("Итого за смену: " + "0" + " руб.")
        self.lbl_itog.setToolTip("Общая выручка за смену:")

        self.btn_cancel = QPushButton("Отменить чек", self)
        self.btn_cancel.setToolTip("Отменить последнюю продажу")
        self.btn_cancel.clicked.connect(self.cancel_trade)
        self.btn_trade = QPushButton("Чек № А-1", self)
        self.btn_trade.setToolTip("Завершить продажу")
        self.btn_trade.clicked.connect(self.trade)


        self.layout_main = QVBoxLayout()

        self.layout_name = QHBoxLayout()
        self.layout_name.addWidget(self.lbl_name)
        self.layout_name.addWidget(self.combo_box_fuel)

        self.layout_price = QHBoxLayout()
        self.layout_price.addWidget(self.lbl_price)
        self.layout_price.addWidget(self.input_price)

        self.layout_number = QHBoxLayout()
        self.layout_number.addWidget(self.lbl_number)
        self.layout_number.addWidget(self.input_number)

        self.layout_discount = QHBoxLayout()
        self.layout_discount.addWidget(self.lbl_discount)
        self.layout_discount.addWidget(self.combo_box_discont)

        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.btn_trade)
        self.layout_button.addWidget(self.btn_cancel)

        self.layout_main.addWidget(self.lbl_logo)
        self.layout_main.addLayout(self.layout_name)
        self.layout_main.addWidget(self.lbl_all_count)
        self.layout_main.addLayout(self.layout_price)
        self.layout_main.addLayout(self.layout_number)
        self.layout_main.addLayout(self.layout_discount)
        self.layout_main.addWidget(self.lbl_cost)
        self.layout_main.addWidget(self.lbl_itog)
        self.layout_main.addLayout(self.layout_button)

        central_widget = QWidget()
        central_widget.setLayout(self.layout_main)
        self.setCentralWidget(central_widget)

        # Создание действий (actions) для клавиатурных сокращений
        self.trade_action = QAction("Завершить продажу", self)
        self.trade_action.triggered.connect(self.trade)
        self.trade_action.setShortcut(QKeySequence(Qt.Key_Return))
        self.cancel_trade_action = QAction("Отменить продажу", self)
        self.cancel_trade_action.triggered.connect(self.cancel_trade)
        self.cancel_trade_action.setShortcut(QKeySequence(Qt.Key_Cancel))

        # Добавление действий в главное меню
        self.trade_menu = self.menuBar().addMenu("Продажа")
        self.trade_menu.addAction(self.trade_action)
        self.edit_menu = self.menuBar().addMenu("Редактировать")
        self.edit_menu.addAction(self.cancel_trade_action)
        # Применение стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFF8DC;
            }
            QPushButton {
                background-color: #8B0000;
                color: white;
                border-radius: 2px;
                border: 2px;
                padding: 10px 10px;
                font-size: 18px;
            }
            QLabel
            {
                color: black;
                font-size: 20px;
            }
            QComboBox {
                color: black;
                padding: 5px 5px;
                border: 2px solid #8B0000;
                border-radius: 2px;
                font-size: 18px;
                }
            QLineEdit {
                border: 2px solid #8B0000;
                border-radius: 5px;
                padding: 5px;
                font-size: 18px;
            }
        """)
    def set_cost(self):
        self.cost = get_cost(float(self.input_price.text()),
                             int(self.combo_box_discont.currentText()[:-1]),
                             int(self.input_number.text()))
    def trade(self):
        if self.check():
            # self.fuel = {"A-92": [1450, 47.29], "A-95": [2600, 51.90], "ДТ": [1200, 55], "ГАЗ": [1800, 45]}
            self.fuel[self.combo_box_fuel.currentText()][0] -= int(self.input_number.text())
            self.set_cost()
            self.total += self.cost
            self.total = round(self.total, 2)
            self.lbl_itog.setText("Итого за смену: " + str(self.total) + " руб.")
            self.lbl_all_count.setText(("Остаток: " + str(self.fuel[self.combo_box_fuel.currentText()][0]) + " литров"))

            self.undo_stack.append([self.combo_box_fuel.currentText(), float(self.input_price.text()),
                                    int(self.combo_box_discont.currentText()[:-1]),
                                    int(self.input_number.text()), round(self.cost, 2)])
            print(self.undo_stack)
            self.count_receipt += 1
            self.btn_trade.setText("Чек № А-" + str(self.count_receipt))

    def cancel_trade(self):
        if self.undo_stack:
            z = self.undo_stack[-1]
            self.combo_box_fuel.setCurrentText(z[0]) # Название
            self.combo_box_discont.setCurrentText(str(z[2])+"%") # Дисконт
            self.fuel[self.combo_box_fuel.currentText()][0] += z[3] # Возврат остаток
            self.lbl_all_count.setText(("Остаток: " + str(self.fuel[self.combo_box_fuel.currentText()][0]) + " литров"))
            self.input_price.setText(str(z[1])) # Цена
            self.input_number.setText(str(z[3])) # Количество
            self.total -= round(z[4], 2)
            self.total = round(self.total, 2)
            self.lbl_itog.setText("Итого за смену: " + str(self.total) + " руб.")
            self.undo_stack.pop()
            self.count_receipt -= 1
            self.btn_trade.setText("Чек № А-" + str(self.count_receipt))
            self.update()

    def update_combo(self):
        self.set_cost()
        self.lbl_cost.setText(("Стоимость: " + str(round(self.cost, 2)) + " руб."))

        self.input_price.setText(str(self.fuel[self.combo_box_fuel.currentText()][1]))

        self.lbl_all_count.setText(("Остаток: " + str(self.fuel[self.combo_box_fuel.currentText()][0]) + " литров"))

    def update(self):
        if self.check():
            self.set_cost()
            self.lbl_cost.setText(("Стоимость: " + str(round(self.cost, 2)) + " руб."))

    def check(self):
        if (self.input_price.text() != "" and self.input_price.text() is not None
                and self.input_number.text() != "" and self.input_number.text() is not None):
            return True
        else:
            self.lbl_cost.setText(("Стоимость: " + "0" + " руб."))
            return False


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
