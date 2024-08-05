import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


class FeedbackWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FeedbackWindow, self).__init__()
        uic.loadUi('ui/feedback_window.ui', self)

        self.feedback_background_label.setPixmap(QtGui.QPixmap(config['images']['feedback_window']))
        self.story_1.setText(config['texts']['feedback_window']['story'])
        self.continue_button.clicked.connect(self.continue_game)

    def continue_game(self) -> None:
        self.hide()
        from windows.second_game_window import SecondGameWindow
        self.second_game_window = SecondGameWindow()
        self.second_game_window.show()
