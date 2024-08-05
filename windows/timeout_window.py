import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


def rage_quit():
    QtWidgets.QApplication.quit()


class TimeoutWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(TimeoutWindow, self).__init__()
        uic.loadUi('ui/timeout_window.ui', self)

        self.timeout_bkg_label.setPixmap(QtGui.QPixmap(config['images']['timeout_window']))
        self.dialog_buttons.accepted.connect(self.try_again)
        self.dialog_buttons.rejected.connect(rage_quit)

    def try_again(self) -> None:
        self.hide()
        from windows.first_game_window import FirstGameWindow
        self.first_game_window = FirstGameWindow()
        self.first_game_window.show()
