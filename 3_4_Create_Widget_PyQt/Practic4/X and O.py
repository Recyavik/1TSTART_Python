import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QGridLayout, QVBoxLayout, QWidget, QPushButton,
                             QLineEdit, QHBoxLayout, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt

class GameX0:

    def __init__(self):
        self.table_game = np.array([['*','*','*'],['*','*','*'],['*','*','*']], str)
        self.game_account = "0:0"
        self.game_name_player1 = "Player1"
        self.game_name_player2 = "Player2"
        self.count_player1 = 0
        self.count_player2 = 0

    def view(self):
        for i in range(3):
            for j in range(3):
                print(self.table_game[i][j], end=' ')
            print()
        print()

    def turn(self, index_i, index_j, player="1"):
        if (index_i >= 0 and index_i < 3 and index_j >= 0 and index_j < 3
                and self.table_game[index_i][index_j] == "*"):
            self.table_game[index_i][index_j] = player


    def check(self, player="0"):
        player = str(player[:1])
        result = False
        for i in range(3):
            if list(self.table_game[i]).count(player) == 3:
                result = True
                break
        self.table_game = np.rot90(self.table_game,1)
        for i in range(3):
            if list(self.table_game[i]).count(player) == 3:
                result = True
                break
        self.table_game = np.rot90(self.table_game,3)
        if ((self.table_game[0,0] == player and self.table_game[1,1] == player
            and self.table_game[2,2] == player) or
            (self.table_game[0, 2] == player and self.table_game[1, 1] == player
             and self.table_game[2, 0] == player)):

            result = True
        return result

    def drawn_game(self):
        result = True
        for i in range(3):
            if list(self.table_game[i]).count("*") > 0:
                result = False
                break
        return result

    def new(self):
        self.table_game = np.array([['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']], str)


class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики - Нолики")
        self.setGeometry(500, 200, 500, 500)
        self.game = GameX0()
        self.game_buttons = None
        self.turn = True
        self.initUI()


    def initUI(self):
        # Создание виджетов
        self.game_buttons = ({'0,0':QPushButton('', self), '0,1':QPushButton('', self), '0,2':QPushButton('', self),
                             '1,0':QPushButton('', self),'1,1':QPushButton('', self), '1,2':QPushButton('', self),
                             '2,0':QPushButton('', self), '2,1':QPushButton('', self), '2,2':QPushButton('', self)})
        for key in self.game_buttons.keys():
                self.game_buttons[key].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.game_buttons[key].setToolTip(key)
                self.game_buttons[key].setEnabled(True)

        self.game_buttons['0,0'].clicked.connect(lambda :self.turn_button('0,0'))
        self.game_buttons['0,1'].clicked.connect(lambda: self.turn_button('0,1'))
        self.game_buttons['0,2'].clicked.connect(lambda: self.turn_button('0,2'))
        self.game_buttons['1,0'].clicked.connect(lambda: self.turn_button('1,0'))
        self.game_buttons['1,1'].clicked.connect(lambda: self.turn_button('1,1'))
        self.game_buttons['1,2'].clicked.connect(lambda: self.turn_button('1,2'))
        self.game_buttons['2,0'].clicked.connect(lambda: self.turn_button('2,0'))
        self.game_buttons['2,1'].clicked.connect(lambda: self.turn_button('2,1'))
        self.game_buttons['2,2'].clicked.connect(lambda: self.turn_button('2,2'))

        lbl_name_player1 = QLabel("Крестики:", self)
        self.input_name_player1 = QLineEdit(self.game.game_name_player1, self)
        self.input_name_player1.textEdited.connect(self.change_player)

        lbl_name_player2 = QLabel("Нолики:  ",self)
        self.input_name_player2 = QLineEdit(self.game.game_name_player2, self)
        self.input_name_player2.textEdited.connect(self.change_player)

        btn_new = QPushButton('НОВАЯ ИГРА', self)
        btn_new.setToolTip("Начать сначала")
        btn_new.clicked.connect(self.new_game)

        self.lbl_game_account = QLabel("Общий счёт: " + self.game.game_account, self)
        self.lbl_game_account.setAlignment(Qt.AlignCenter)

        self.lbl_player_win = QLabel("Победитель: ")
        self.lbl_player_win.setObjectName("player_win_game")
        self.lbl_player_win.setStyleSheet("color: #DC143C;")
        self.lbl_player_win.setAlignment(Qt.AlignCenter)


        # Размещение
        layout_playing_field = QGridLayout()
        for key in self.game_buttons.keys():
                index_i = int(key[0])
                index_j = int(key[-1])
                layout_playing_field.addWidget(self.game_buttons[key], index_i, index_j)

        layout_player1 = QHBoxLayout()
        layout_player1.addWidget(lbl_name_player1)
        layout_player1.addWidget(self.input_name_player1)

        layout_player2 = QHBoxLayout()
        layout_player2.addWidget(lbl_name_player2)
        layout_player2.addWidget(self.input_name_player2)

        layout_main = QVBoxLayout()
        layout_main.addWidget(self.lbl_player_win)
        layout_main.addLayout(layout_playing_field)
        layout_main.addLayout(layout_player1)
        layout_main.addLayout(layout_player2)
        layout_main.addWidget(btn_new)
        layout_main.addWidget(self.lbl_game_account)


        central_widget = QWidget()
        central_widget.setLayout(layout_main)
        self.setCentralWidget(central_widget)

        # Применение стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #D8BFD8;
            }
            QPushButton {
                background-color: #4B0082;
                font: bold;
                color: white;
                border: 2px solid white;
                padding: 10px 20px;
                font-size: 24px;
            }
            QLabel
            {
                color: black;
                font-size: 24px;
            }
            QLabel#player_win_game 
            {color: #8B008B;
            font: bold;
            }
            QLineEdit {
                border: 2px solid #4B0082;
                border-radius: 5px;
                padding: 2px;
                font-size: 20px;
            }
        """)
    def change_player(self):
        self.game.game_name_player1 = self.input_name_player1.text()
        self.game.game_name_player2 = self.input_name_player2.text()
        print(self.game.game_name_player1)
        print(self.game.game_name_player2)




    def new_game(self):
        (QMessageBox.information(self, "Новая игра",
        "Первый ход крестиком играет: " + self.game.game_name_player2))
        self.turn = True
        self.game.new()
        for key in self.game_buttons.keys():
            self.game_buttons[key].setText("")
            self.game_buttons[key].setEnabled(True)

        if self.game.count_player1 > self.game.count_player2:
            self.lbl_player_win.setText("Побеждает: " + self.input_name_player1.text())
        elif self.game.count_player2 > self.game.count_player1:
            self.lbl_player_win.setText("Побеждает: " + self.input_name_player2.text())
        elif self.game.count_player1 == self.game.count_player2 == 0:
            self.lbl_player_win.setText("Победитель ещё не определён !!!")
        else:
            self.lbl_player_win.setText("Побеждает: ДРУЖБА !!!")
        self.lbl_player_win.setAlignment(Qt.AlignCenter)
        self.lbl_player_win.setStyleSheet("color: #8B008B;")
        self.swap_account()

    def swap_account(self):
        self.game.count_player1, self.game.count_player2 = self.game.count_player2, self.game.count_player1
        self.game.game_name_player1, self.game.game_name_player2 =\
            self.game.game_name_player2,  self.game.game_name_player1
        self.input_name_player1.setText(str(self.game.game_name_player1))
        self.input_name_player2.setText(str(self.game.game_name_player2))
        self.game_account()

    def turn_button(self, index):
        self.game_buttons[index].setEnabled(False)
        if self.turn == True:
            self.game.turn(int(index[0]), int(index[-1]), "1")
            self.game_buttons[index].setText("X")
        else:
            self.game.turn(int(index[0]), int(index[-1]), "0")
            self.game_buttons[index].setText("0")
        self.turn = not self.turn
        # self.game.view()
        self.check_win()

    def check_win(self):
        if self.game.check("1"):
            self.lbl_player_win.setText("Победитель: " + self.input_name_player1.text())
            self.game.count_player1 += 1
            self.game_account()
            for key in self.game_buttons.keys():
                self.game_buttons[key].setEnabled(False)
                self.lbl_player_win.setStyleSheet("color: #DC143C;")
        if self.game.check("0"):
            self.lbl_player_win.setText("Победитель: " + self.input_name_player2.text())
            self.game.count_player2 += 1
            self.game_account()
            self.lbl_player_win.setStyleSheet("color: #DC143C;")
            for key in self.game_buttons.keys():
                self.game_buttons[key].setEnabled(False)
        if self.game.drawn_game() and self.game.check("0") is not None and self.game.check("1") is not None:
            self.lbl_player_win.setText("Ничья!!!")
            self.lbl_player_win.setStyleSheet("color: #DC143C;")


    def game_account(self):
        self.game.game_account = str(self.game.count_player1) + ":" + str(self.game.count_player2)
        self.lbl_game_account.setText("Общий счёт: " + self.game.game_account)
        self.lbl_game_account.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()