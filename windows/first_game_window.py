import json
import random
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import QTime, QTimer

with open('config.json', 'r') as f:
    config = json.load(f)


class FirstGameWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FirstGameWindow, self).__init__()
        uic.loadUi('ui/first_game_window.ui', self)

        self.first_game_background_label.setPixmap(QtGui.QPixmap(config['images']['first_game_window']))
        self.questions = config['texts']['first_game_window']['questions']
        self.current_question, self.correct_answer = random.choice(self.questions)
        self.question_label.setText(self.current_question)
        self.submit_button.clicked.connect(self.check_answer)
        self.timer_duration = 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        """
        Connect the 'timeout' signal of the timer to the 'update_timer' method.
        This means that when the timer times out (every second in this case), the 'update_timer' method will be called.
        """
        self.start_timer()

    def start_timer(self) -> None:
        self.time_left = QTime(0, 0, 15)
        """
        Initialize the countdown time to 15 seconds (00:00:15).
        """
        self.timer.start(1000)
        """
        Start the timer with a timeout interval of 1000 milliseconds (1 second).
        """
        self.update_timer()

    def update_timer(self) -> None:
        self.time_left = self.time_left.addSecs(-1)
        """
        Subtract one second from the remaining time.
        """
        self.timer_label.setText(self.time_left.toString("mm:ss"))
        if self.time_left == QTime(0, 0, 0):
            self.timer.stop()
            self.time_out()
            """
            If the time runs out (reaches 00:00:00), stop the timer and call the 'time_out' 
            method to handle the timeout event.
            """

    def check_answer(self) -> None:
        user_answer = self.answer_input.text().strip().lower()

        if user_answer == self.correct_answer:
            self.timer.stop()
            self.hide()
            from windows.feedback_window import FeedbackWindow
            self.feedback_window = FeedbackWindow()
            self.feedback_window.show()
            """
            If the user's answer is correct:
            - Stop the timer.
            - Hide the current game window.
            - Create an instance of 'FeedbackWindow'.
            - Show the feedback window, which provides feedback and possibly moves to the next part of the game.
            """

        else:
            self.result_label.setText("Wrong! Try again.")

    def time_out(self) -> None:
        self.hide()
        from windows.timeout_window import TimeoutWindow
        self.timeout_window = TimeoutWindow()
        self.timeout_window.show()
