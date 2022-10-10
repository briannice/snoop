from PyQt5.QtCore import pyqtSignal, QObject


class SniffingSignal(QObject):
    result = pyqtSignal(object)

