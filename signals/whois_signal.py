from PyQt5.QtCore import pyqtSignal, QObject


class WhoisSignal(QObject):
    data = pyqtSignal(object)
