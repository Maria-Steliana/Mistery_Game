import json
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import QTime, QTimer

with open('config.json', 'r') as f:
    config = json.load(f)


class FifthGameWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FifthGameWindow, self).__init__()
        uic.loadUi('ui/fifth_game_window.ui', self)

        self.question_image_label.setPixmap(QtGui.QPixmap(config['images']['fifth_game_window']))
        self.correct_answer = config['texts']['fifth_game_window']['correct_answer']
        self.submit_button.clicked.connect(self.check_answer)
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

    def check_answer(self) -> None:
        user_answer = self.answer_input.text().strip()
        if user_answer == self.correct_answer:
            self.timer.stop()
            self.hide()
            from windows.feedback_window5 import FeedbackWindow5
            self.feedback_window = FeedbackWindow5()
            self.feedback_window.show()
        else:
            self.result_label.setText("Wrong! Try again.")

    def time_out(self) -> None:
        self.hide()
        from windows.timeout_window import TimeoutWindow
        self.timeout_window = TimeoutWindow()
        self.timeout_window.show()
