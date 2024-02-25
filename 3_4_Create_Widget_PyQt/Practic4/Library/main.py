from modules import *
from PyQt6 import uic

from Abonents import *
from Order_Books import *
from Books import *


def main():
    app = QtWidgets.QApplication(sys.argv)
    w1 = Abonents()
    w2 = AddBook()
    w3 = OrderBook()
    w1.show()
    w2.show()
    w3.show()
    app.exec()


if __name__ == "__main__":
    main()