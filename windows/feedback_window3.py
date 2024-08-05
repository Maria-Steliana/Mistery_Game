import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


class FeedbackWindow3(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FeedbackWindow3, self).__init__()
        uic.loadUi('ui/feedback_window3.ui', self)

        self.feedback3_bckg_label.setPixmap(QtGui.QPixmap(config['images']['feedback_window3']))
        self.story_3.setText(config['texts']['feedback_window3']['story'])
        self.continue_button.clicked.connect(self.continue_game)

    def continue_game(self) -> None:
        self.hide()
        from windows.fourth_game_window import FourthGameWindow
        self.fourth_game_window = FourthGameWindow()
        self.fourth_game_window.show()
