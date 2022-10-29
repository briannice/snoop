from PyQt5.QtCore import pyqtSignal, QObject


class WhoisLookupSignal(QObject):
    data = pyqtSignal(object)
