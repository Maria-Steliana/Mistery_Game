import json
from PyQt6 import QtWidgets, QtGui, uic
from windows.fin2_window import FinWindow2

with open('config.json', 'r') as f:
    config = json.load(f)


class FeedbackWindow5(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FeedbackWindow5, self).__init__()
        uic.loadUi('ui/feedback_window5.ui', self)

        self.feedback2_bckg_label.setPixmap(QtGui.QPixmap(config['images']['feedback_window5']))
        self.story_2.setText(config['texts']['feedback_window5']['story'])
        self.continue_button.clicked.connect(self.continue_game)

    def continue_game(self) -> None:
        self.hide()
        self.fifth_game_window = FinWindow2()
        self.fifth_game_window.show()
