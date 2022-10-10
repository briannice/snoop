from PyQt5 import QtGui


class Font(QtGui.QFont):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
