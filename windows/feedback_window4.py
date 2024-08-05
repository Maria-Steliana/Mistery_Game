import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


class FeedbackWindow4(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FeedbackWindow4, self).__init__()
        uic.loadUi('ui/feedback_window4.ui', self)

        self.feedback2_bckg_label.setPixmap(QtGui.QPixmap(config['images']['feedback_window4']))
        self.story_2.setText(config['texts']['feedback_window4']['story'])
        self.continue_button.clicked.connect(self.continue_game)

    def continue_game(self) -> None:
        self.hide()
        from windows.fifth_game_window import FifthGameWindow
        self.fifth_game_window = FifthGameWindow()
        self.fifth_game_window.show()
