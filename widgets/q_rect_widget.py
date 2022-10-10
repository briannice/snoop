from PyQt5 import QtCore


class QRect(QtCore.QRect):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
