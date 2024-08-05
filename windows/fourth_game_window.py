import json
import random
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import QTime, QTimer

with open('config.json', 'r') as f:
    config = json.load(f)


class FourthGameWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FourthGameWindow, self).__init__()
        uic.loadUi('ui/fourth_game_window.ui', self)

        self.bckg_label.setPixmap(QtGui.QPixmap(config['images']['fourth_game_window']))
        self.riddle_label.setText(config['texts']['fourth_game_window']['riddle'])
        self.images = config['texts']['fourth_game_window']['images']
        self.correct_image = config['texts']['fourth_game_window']['correct_image']
        random.shuffle(self.images)
        """Shuffles the list of images randomly."""
        self.image_index = 0
        """Initializes the index of the current image to 0."""
        self.update_image()
        self.next_button.clicked.connect(self.show_next_image)
        self.ok_button.clicked.connect(self.check_answer)
        self.timer_duration = 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.start_timer()

    def start_timer(self) -> None:
        self.time_left = QTime(0, 1, 0)
        self.timer.start(1000)
        self.update_timer()

    def update_timer(self) -> None:
        self.time_left = self.time_left.addSecs(-1)
        self.timer_label.setText(self.time_left.toString("mm:ss"))
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.time_out()

    def update_image(self) -> None:
        self.image_label.setPixmap(QtGui.QPixmap(self.images[self.image_index]))
        """Updates the displayed image based on the current index."""

    def show_next_image(self) -> None:
        self.image_index = (self.image_index + 1) % len(self.images)
        self.update_image()
        """Advances to the next image and updates the display
        the operator '%' is used for when the last image is reached, the first image appears again """

    def check_answer(self) -> None:
        if self.images[self.image_index] == self.correct_image:
            self.timer.stop()
            self.hide()
            from windows.feedback_window4 import FeedbackWindow4
            self.feedback_window = FeedbackWindow4()
            self.feedback_window.show()
        else:
            self.timer.stop()
            self.hide()
            from windows.timeout_window import TimeoutWindow
            self.timeout_window = TimeoutWindow()
            self.timeout_window.show()

    def time_out(self) -> None:
        self.hide()
        from windows.timeout_window import TimeoutWindow
        self.timeout_window = TimeoutWindow()
        self.timeout_window.show()
