from PyQt5 import QtCore


class QSize(QtCore.QSize):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
