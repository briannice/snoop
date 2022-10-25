from PyQt5.QtCore import pyqtSignal, QObject


class SniffingSignal(QObject):
    packet = pyqtSignal(object)
    stop = pyqtSignal(object)
