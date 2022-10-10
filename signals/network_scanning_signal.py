from PyQt5.QtCore import pyqtSignal, QObject


class NetworkScanningSignal(QObject):
    data = pyqtSignal(object)
