import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


class FeedbackWindow2(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FeedbackWindow2, self).__init__()
        uic.loadUi('ui/feedback_window2.ui', self)

        self.feedback2_bckg_label.setPixmap(QtGui.QPixmap(config['images']['feedback_window2']))
        self.story_2.setText(config['texts']['feedback_window2']['story'])
        self.continue_button.clicked.connect(self.continue_game)

    def continue_game(self) -> None:
        self.hide()
        from windows.third_game_window import ThirdGameWindow
        self.third_game_window = ThirdGameWindow()
        self.third_game_window.show()
