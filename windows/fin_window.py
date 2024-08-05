import json
from PyQt6 import QtWidgets, QtGui, uic
from windows.first_game_window import FirstGameWindow

with open('config.json', 'r') as f:
    config = json.load(f)


class FinWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FinWindow, self).__init__()
        uic.loadUi('ui/fin_window.ui', self)

        self.fin_bkg_label.setPixmap(QtGui.QPixmap(config['images']['fin_window']))
        self.back_to_game_button.clicked.connect(self.back_to_first_game)

    def back_to_first_game(self) -> None:
        self.hide()
        self.first_game_window = FirstGameWindow()
        self.first_game_window.show()
