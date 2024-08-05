import json
from PyQt6 import QtWidgets, QtGui, uic
from windows.intro_window import IntroWindow

with open('config.json', 'r') as f:
    config = json.load(f)
    """open the contents of the config.json file and loading it into a Python dictionary using the json module."""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        uic.loadUi('ui/main_window.ui', self)

        self.background_label.setPixmap(QtGui.QPixmap(config['images']['main_window']))
        self.title_label.setText(config['texts']['main_window']['title'])
        self.custom_text_label.setText(config['texts']['main_window']['custom_text'])
        self.start_button.clicked.connect(self.open_intro_window)

    def open_intro_window(self) -> None:
        self.hide()
        self.next_window = IntroWindow()
        self.next_window.show()
