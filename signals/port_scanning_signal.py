from PyQt5.QtCore import pyqtSignal, QObject


class PortScanningSignal(QObject):
    data = pyqtSignal(object)
