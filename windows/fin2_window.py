import json
from PyQt6 import QtWidgets, QtGui, uic

with open('config.json', 'r') as f:
    config = json.load(f)


def close_application():
    QtWidgets.QApplication.instance().quit()


class FinWindow2(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(FinWindow2, self).__init__()
        uic.loadUi('ui/fin2_window.ui', self)

        self.fin2_bkg_label.setPixmap(QtGui.QPixmap(config['images']['fin_window2']))
