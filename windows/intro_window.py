import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


class IntroWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(IntroWindow, self).__init__()
        uic.loadUi('ui/intro_window.ui', self)

        self.intro_background_label.setPixmap(QtGui.QPixmap(config['images']['intro_window']))
        intro_texts = config['texts']['intro_window']['intro_texts']
        self.intro_label0.setText(intro_texts[0])
        self.intro_label1.setText(intro_texts[1])
        self.intro_label2.setText(intro_texts[2])
        self.intro_label3.setText(intro_texts[3])
        self.dialog_buttons.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.on_yes_clicked)
        self.dialog_buttons.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.on_cancel_clicked)

    def on_yes_clicked(self) -> None:
        self.hide()
        from windows.first_game_window import FirstGameWindow
        self.first_game_window = FirstGameWindow()
        self.first_game_window.show()

    def on_cancel_clicked(self) -> None:
        self.hide()
        from windows.fin_window import FinWindow
        self.fin_window = FinWindow()
        self.fin_window.show()
